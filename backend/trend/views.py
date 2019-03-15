# Create your views here.
import requests
from haystack.inputs import Clean
from haystack.query import SearchQuerySet
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from hackertrend.settings import XMashapeKey
from .models import Story
from .serializers import StorySerializer, SearchResultSerializer


# This Class Featch data from hackernews's topstories api that gives some list of `id`'s
# then we will get full details of those `id`'s.
# while doing that we then also calculate its sentiment analysis by another api from
# mashape's sentiment analysis api against the title and then store it into the database.
# also this include pagination and elastic search support.
class ListApi(generics.ListAPIView):
    pagination_class = PageNumberPagination
    queryset = Story.objects.order_by('-score').all()
    serializer_class = StorySerializer

    def list(self, request, *args, **kwargs):
        list_api_response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
        list_api_json = list_api_response.json()
        details_endpoint = 'https://hacker-news.firebaseio.com/v0/item/{uId}.json'
        results_to_fetch = int(request.GET.get('page', 1)) * self.pagination_class.page_size

        reindex_haystack = False
        for index, story_id in enumerate(list_api_json):
            if index > results_to_fetch:
                break
            story = Story.objects.filter(story_id=story_id)
            if not story.exists():
                reindex_haystack = True
                url = details_endpoint.format(uId=story_id)
                trend_api = requests.get(url)
                data = trend_api.json()
                sentiment_api = requests.post(
                    "https://twinword-sentiment-analysis.p.mashape.com/analyze/",
                    headers={
                        "X-Mashape-Key": XMashapeKey,
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Accept": "application/json"
                    },
                    params={
                        "text": data['title']
                    }
                )
                sentiment_api_json = sentiment_api.json()
                if 'type' in sentiment_api_json:
                    sentiment = sentiment_api_json['type']
                else:
                    sentiment = 'Unknown/API_Error'

                Story.objects.create(
                    story_id=story_id,
                    username=data['by'],
                    title=data['title'],
                    url=data['url'] if 'url' in data else None,
                    score=data['score'],
                    sentiment=sentiment
                )
        if reindex_haystack:
            from haystack.management.commands import update_index
            update_index.Command().handle()
        return super().list(request, *args, **kwargs)

# this class is used to search through already featched results.
class SearchApi(generics.ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = SearchResultSerializer

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        return SearchQuerySet().filter(content=Clean(q))

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
