from django.urls import path

from . import views

#App's urls goes here.
urlpatterns = [
    path('', views.ListApi.as_view(), name='List'),
    path('search/', views.SearchApi.as_view(), name='search_api'),
]
