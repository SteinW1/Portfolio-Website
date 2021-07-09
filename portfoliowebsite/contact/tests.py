from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from http import HTTPStatus
from .forms import ContactForm

# Create your tests here.
class ContactFormTests(TestCase):
    def setUp(self):
        self.client = Client()
        
    def tearDown(self):
        pass
        
    def test_contact_form_invalid_email(self):
        '''Test to make sure the form won't accept invalid email'''
        form = ContactForm(data={'from_name': 'testname',
                                    'from_email': 'testthisform&&gmail.com',
                                    'subject': 'test subject',
                                    'contact_message': 'random words for testing',
                                    })
        self.assertEqual(
            form.errors["from_email"], ["Enter a valid email address."]
        )
        
class ContactViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        
    def tearDown(self):
        pass
    
    def test_contact_form_get(self):
        '''Test if the form page loads properly'''
        ip = settings.WEBSITE_IP
        response = self.client.get('/contact/')
        self.assertEqual(
            response.status_code, 200
        )
    
    def test_contact_form_post_success(self):
        '''Test if the form will can take valid information'''
        data = {'from_name': 'testname',
                    'from_email': 'testthisform@gmail.com',
                    'subject': 'test subject',
                    'contact_message': 'random words for testing',
                    }
        form = ContactForm(data)
        self.assertEqual(form.is_valid(), True)