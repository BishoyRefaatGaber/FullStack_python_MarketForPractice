from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch
from visitors_manager.models import Visitors

class TestVisitorsManager(TestCase):

    @patch('home_page.views.get_client_ip', return_value=('197.38.106.86', True))
    @patch('home_page.views.DbIpCity.get')
    def test_IpLocation(self, mock_get_ip_data, mock_get_client_ip):
        # Simulate a response from DbIpCity.get() with a mocked country and city
        mock_get_ip_data.return_value.country = 'EG'
        mock_get_ip_data.return_value.city = 'Cairo'
        
        client = Client()
        response = client.get(reverse('home'))

        # Check response status code
        self.assertEquals(response.status_code, 200)

        # Check if a Visitors object has been created with the correct IP and location
        visitor = Visitors.objects.filter(ip='197.38.106.86').first()
        self.assertIsNotNone(visitor)
        self.assertEquals(visitor.location, 'EG,Cairo')
