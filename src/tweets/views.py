from django import forms
from django.forms.utils import ErrorList
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse


from .mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import TweetModelForm
from .models import *




###################  class based view ########################

class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = '/tweets/'

    # def form_valid(self, form):
    #     if self.request.user.is_authenticated:
    #         print(self.request.user)
    #         form.instance.user = self.request.user
    #         return super(TweetCreateView, self).form_valid(form)
        # else:
        #     form._erroes[forms.forms.NON_FIELD_ERRORS] = ErrorList['User must be logged in to continue']
        #     return self.form_invalid(form)


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    # success_url = reverse_lazy('tweets:list')


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('tweets:list')    



class TweetDetailView (DetailView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/detail_view.html'

    # def get_object(self):
    #     print(self.kwargs)
    #     tweet_pk  = self.kwargs.get("pk")
    #     print(tweet_pk)
    #     tweet = get_object_or_404(Tweet, pk=tweet_pk)
    #     return tweet

class TweetListView (ListView):
    template_name = 'tweets/list_view.html'
    
    def get_queryset(self):
        queryset = Tweet.objects.all()
        # print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains = query)|
                Q(user__username__icontains = query)
            )
        return queryset



    # def get_context_data(self, *args, **kwargs):
        # context = super(TweetListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     context['anotherlist'] = Tweet.objects.all()
        # return context




###################  function based view ########################

# def tweet_create_view(request):
#     if request.method=="POST":
#         form = TweetModelForm(request.POST or None)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             return redirect('list')
#     else:
#         form = TweetModelForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'tweets/create_view.html, context')

# def tweet_detail_view(request, id=1):
#     tweet = Tweet.objects.get(id=id)
#     context =  {
#         'tweet' : tweet
#     }
#     return render(request, 'tweets/detail_view.html', context)

# def tweet_list_view(request):
#     tweets = Tweet.objects.all()
#     context = {
#         'tweets' : tweets
#     }
#     return render(request, 'tweets/list_view.html', context)
