from django.test import TestCase, Client
from django.urls import reverse
import json


class TestViews(TestCase):

    def test_index_view(self):
        client=Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'analytics/index.html')

    def test_login_view(self):
        client=Client()
        response = client.get(reverse('login'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'analytics/login.html')

    def test_register_view(self):
        client=Client()
        response = client.get(reverse('register'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'analytics/register.html')

    def test_logout_view(self):
        client=Client()
        response = client.get(reverse('logout'))
        self.assertEquals(response.status_code,302)

    def test_start_view(self):
        client=Client()
        response = client.get(reverse('start',args=['sarapizzz']))
        self.assertEquals(response.status_code,200)
