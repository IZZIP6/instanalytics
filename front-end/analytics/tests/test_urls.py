from django.test import SimpleTestCase
from django.urls import resolve, reverse
from analytics import views as v

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url=reverse('index')
        self.assertEquals(resolve(url).func,v.index)

    def test_login_url_is_resolved(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,v.log)

    def test_register_url_is_resolved(self):
        url=reverse('register')
        self.assertEquals(resolve(url).func,v.register)

    def test_logout_url_is_resolved(self):
        url=reverse('logout')
        self.assertEquals(resolve(url).func,v.logoutUser)

    def test_start_url_is_resolved(self):
        url=reverse('start',args=['sarapizzz'])
        self.assertEquals(resolve(url).func,v.start)
