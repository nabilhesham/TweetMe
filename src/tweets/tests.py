from django.test import TestCase
from .models import Tweet
from django.contrib.auth.models import User
from django.urls import reverse

class TweetModelTestCase(TestCase):
    
    def setUp(self):
        some_random_user = User.objects.create(username='test1')

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user = User.objects.first(),
            content = "some random content"
            )
        absolute_url = reverse('tweets:detail', kwargs={'pk':1})
        self.assertTrue(obj.content == "some random content")
        self.assertTrue(obj.id == 1)
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user = User.objects.first(),
            content = "some random content"
            )
        absolute_url = reverse('tweets:detail', kwargs={'pk':obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
            
