from django.test import TestCase
from django.urls import reverse



# Create your tests here.
def quick_test():
    return "This is a quick test function."

class QuickTestCase(TestCase):
    def test_quick_test(self):
        self.assertEqual(quick_test(), "This is a quick test function.")

class URLTests(TestCase):
    def test_reverse_url(self):
        url = reverse('your_view_name')
        self.assertEqual(url, '/expected/url/')