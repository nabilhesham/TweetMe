from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.urls import reverse

from .validators import validate_content

class Tweet(models.Model):
    user        =   models.ForeignKey(User, on_delete = models.CASCADE)
    content     =   models.CharField(max_length=140, validators=[validate_content])
    timestamp   =   models.DateTimeField(auto_now_add=True)
    updated     =   models.DateTimeField(auto_now=True)

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