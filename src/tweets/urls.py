
from django.urls import path, include
from .views import (
    RetweetView,
    TweetListView,
    TweetCreateView,
    TweetDetailView,
    TweetUpdateView,
    TweetDeleteView,
)

from django.views.generic.base import RedirectView

app_name = 'tweets'

urlpatterns = [
    # path('',views.tweet_list_view, name='list'),
    # path('1/',views.tweet_detail_view, name='detail'),
    path('', RedirectView.as_view( url = "/")),
    path('search/', TweetListView.as_view(), name='list'),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<int:pk>/', TweetDetailView.as_view(), name='detail'),
    path('<int:pk>/retweet/', RetweetView.as_view(), name='retweet'),
    path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),

]
