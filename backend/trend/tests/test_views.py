from django.test import TestCase, Client
from django.urls  import reverse

class TestViews(TestCase):
    
    #this method runs before every single test method
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('List')

    #testing get api for list via 'List' urls
    def test_story_list_get(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)

