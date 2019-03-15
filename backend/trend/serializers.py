from rest_framework import serializers

from .models import Story

#this serializer provide story list response structure.
class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('story_id', 'username', 'title', 'score', 'url', 'sentiment')

#this serializer provide search result response structure as well as update/create method for searchApi in views.py.
class SearchResultSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    story_id = serializers.CharField(source='object.story_id')
    username = serializers.CharField(source='object.username')
    title = serializers.CharField(source='object.title')
    score = serializers.CharField(source='object.score')
    url = serializers.URLField(source='object.url')
    sentiment = serializers.URLField(source='object.sentiment')
