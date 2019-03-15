from django.test import SimpleTestCase
from django.urls import reverse, resolve
from trend.views import ListApi, SearchApi

class TestUrls(SimpleTestCase):
    
    #this method test urls for 'List' api 
    def test_list_url_resolves(self):
        url = reverse('List')
        self.assertEquals(resolve(url).func.view_class, ListApi)
    
    #this method test urls for 'Search' api 
    def test_search_api_url_resolves(self):
        url = reverse('search_api')
        self.assertEquals(resolve(url).func.view_class, SearchApi)