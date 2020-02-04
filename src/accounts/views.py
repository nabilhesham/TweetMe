from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.views import View
from .models import UserProfile

class UserDetailview(DetailView):
    queryset = User.objects.all()
    template_name = 'accounts/user_detail.html'
    # lookup = 'username' 
    def get_object(self):
        return get_object_or_404(
            User,
            username__iexact = self.kwargs.get('username')
            )

    def get_context_data(self, **kwargs):
        context = super(UserDetailview, self).get_context_data(**kwargs)
        following = UserProfile.objects.is_following(self.request.user, self.get_object())
        context['following'] = following
        return context


class UserFollowView(View):
    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact = username)
        if request.user.is_authenticated:
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect("profiles:detail", username=username)
