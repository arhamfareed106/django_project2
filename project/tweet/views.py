import re
from django.shortcuts import render
from .models import tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = tweet.objects.all().order_by('-craeted_at')  # Use 'craeted_at' instead of 'created_at'
    return render(request, 'tweet_list.html', {'tweets': tweets})
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            new_tweet = form.save(commit=False)  # Renamed to new_tweet
            new_tweet.user = request.user
            new_tweet.save()  # Save the new_tweet instance
            return redirect("tweet_list")
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    existing_tweet = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=existing_tweet)
        if form.is_valid():
            updated_tweet = form.save(commit=False)  # Renamed to updated_tweet
            updated_tweet.user = request.user
            updated_tweet.save()  # Save the updated_tweet instance
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=existing_tweet)
    return render(request, 'tweet_form.html', {'form': form})

def tweet_delete(request, tweet_id):
    existing_tweet = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        existing_tweet.delete()
        return redirect("tweet_list")
    return render(request, 'tweet_confirm_delete.html', {'tweet': existing_tweet})




def register(request):
    if request.method == 'POST':
     form = UserRegistrationForm(request.POST)  
     if form.is_valid():
         user = form.save(commit=False)
         user.set_password(form.cleaned_data['password1'])
         user.save()
         login(request,user)
         return redirect('tweet_list')
    else:
        form= UserRegistrationForm



    return render(request, 'registration/register.html', {'form': form})
