from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Chirps
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):

    posts = Chirps.objects.all()

    context = {

            'posts': posts

            }

    return render(request, 'posts/index.html', context)

@login_required
def oneup(request, id):

    obj = get_object_or_404(Chirps, pk=id)
    obj.likes = obj.likes + 1
    obj.save()

    return HttpResponseRedirect(reverse('posts:index'))

@login_required
def makechirp(request):
    message = request.POST['message']
    user = request.user
     
    chirp = Chirps(user=user,  date=timezone.now(), message=message)
    chirp.save()
    return HttpResponseRedirect(reverse('posts:index'))

def user_home(request, username):
    user = get_object_or_404(User, username=username)
    user_posts = Chirps.objects.filter(user=user)
    return render(request,'posts/users.html', {'posts': user_posts})
		
