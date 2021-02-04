# (c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2021.
# See the LICENSE file for more details.

from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse
from django.test import RequestFactory, TestCase

from django_epflmisc.decorators import cache_anonymous_user


class CacheDecoratorTest(TestCase):

    factory = RequestFactory()

    def test_cache_anonymous_user(self):
        @cache_anonymous_user(timeout=60 * 2, cache="default")
        def a_view(request):
            return HttpResponse()

        anonymous = AnonymousUser()
        request = self.factory.get("/")
        request.user = anonymous
        request.LANGUAGE_CODE = "en"

        response = a_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Cache-Control" in response)
        self.assertEqual(response["Cache-Control"], "max-age=120")

        request = self.factory.get("/")
        request.user = User.objects.create_user(
            username="enrico",
            email="enrico.pallazzo@epfl.ch",
            password="Hey, It's Enrico Pallazzo!",
        )
        request.LANGUAGE_CODE = "fr"
        response = a_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertFalse("Cache-Control" in response)
