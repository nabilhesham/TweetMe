
from django.urls import path, include
from .views import (
    TweetListView,
    TweetCreateView,
    TweetDetailView,
    TweetUpdateView,
    TweetDeleteView,
)

app_name = 'tweets'

urlpatterns = [
    # path('',views.tweet_list_view, name='list'),
    # path('1/',views.tweet_detail_view, name='detail'),
    path('', TweetListView.as_view(), name='list'),
    path('create/', TweetCreateView.as_view(), name='create'),
    path('<int:pk>/', TweetDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),

]
