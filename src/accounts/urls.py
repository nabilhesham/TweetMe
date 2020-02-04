
from django.urls import path, include
from .views import (
    UserDetailview,
    UserFollowView,
)

from django.views.generic.base import RedirectView

app_name = 'accounts'

urlpatterns = [
    # path('',views.tweet_list_view, name='list'),
    # path('1/',views.tweet_detail_view, name='detail'),
    # path('', RedirectView.as_view( url = "/")),
    # path('', TweetListAPIView.as_view(), name='list'),
    # path('create/', TweetCreateAPIView.as_view(), name='create'),
    path('<username>/', UserDetailview.as_view(), name='detail'),
    path('<username>/follow/', UserFollowView.as_view(), name='follow'),
    # path('<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),

]
