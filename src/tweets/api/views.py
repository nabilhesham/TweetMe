from rest_framework import generics
from rest_framework import permissions
from .serializers import TweetModelSerializer
from tweets.models import Tweet
from django.db.models import Q
from .pagination import StandardResultsPagination

from rest_framework.views import  APIView
from rest_framework.response import Response



class RetweetAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        message = "Not Allowed"
        if tweet_qs.exists() and tweet_qs.count() == 1:
            new_tweet = Tweet.objects.retweet(request.user, tweet_qs.first())
            if new_tweet is not None:
                data = TweetModelSerializer(new_tweet).data
                return Response(data)
            message = "Cannot Retweet the same in 1 Day"
        return Response({"message":message}, status=400)
        

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        permission_classes=[permissions.IsAuthenticated]



class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class  = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        im_following = self.request.user.profile.get_following()
        queryset1 = Tweet.objects.filter(user__in=im_following)
        queryset2 = Tweet.objects.filter(user=self.request.user)
        queryset = ( queryset1 | queryset2 ).distinct().order_by("-timestamp")
        print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains = query)|
                Q(user__username__icontains = query)
            )
        return queryset