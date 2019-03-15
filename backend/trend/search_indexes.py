from haystack import indexes

from .models import Story

#Function is used to manage serach index in elastic search
class StoryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(
        document=True, use_template=True, template_name="search/story_search.txt", model_attr='title', boost=1.1
    )

    def get_model(self):
        return Story

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
