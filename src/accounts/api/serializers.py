from rest_framework import serializers
from django.contrib.auth.models import User

class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            # 'email',
            'follower_count',
        ]

    def get_follower_count(self, obj):
        return 0