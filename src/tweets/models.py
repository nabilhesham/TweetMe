import re

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from django.db.models.signals import post_save

from .validators import validate_content

class TweetManager(models.Manager):
    def retweet(self, user, parent_obj):
        if parent_obj.parent:
            og_parent = parent_obj.parent
        else:
            og_parent = parent_obj

        queryset = self.get_queryset().filter(
            user=user, parent=og_parent).filter(
                timestamp__year = timezone.now().year,
                timestamp__month = timezone.now().month,
                timestamp__day = timezone.now().day,
            )
        if queryset.exists():
            return None

        obj = self.model(
            parent = og_parent,
            user = user,
            content = parent_obj.content,
        )
        obj.save()

        return obj

class Tweet(models.Model):
    parent      =   models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)
    user        =   models.ForeignKey(User, on_delete = models.CASCADE)
    content     =   models.CharField(max_length=140, validators=[validate_content])
    timestamp   =   models.DateTimeField(auto_now_add=True)
    updated     =   models.DateTimeField(auto_now=True)

    objects = TweetManager()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('tweets:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-timestamp']

    # def clean(self, *args, **kwgars):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("content canot be abc")
    #     return super(Tweet, self).clean(*args, **kwargs)


def tweet_save_receiver(sender, instance, created, *args, **kwargs):
    if created and not instance.parent:
        # notify a user
        user_regex = r'@(?P<username>[\w.@+-]+)'
        usernames = re.findall(user_regex, instance.content)
        # if usernames:
            # print(usernames)

        # send notification to user 
        hash_regex = r'#(?P<hashtag>[\w\d-]+)'
        hashtags = re.findall(hash_regex, instance.content)
        # if hashtags:
            # print(hashtags)
            
        # send hashtag signal to user

post_save.connect(tweet_save_receiver, sender=Tweet)