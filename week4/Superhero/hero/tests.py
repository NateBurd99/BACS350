from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_admin_page_status_code(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)

from django.test import TestCase

class Tests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)