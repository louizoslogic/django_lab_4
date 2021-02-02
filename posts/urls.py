from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
        path('', views.index, name='index'),
        path('like/<int:id>', views.oneup, name='oneup'),
        path('post/', views.makechirp, name='makechirp'),
        path('user/<str:username>', views.user_home, name='users')
        ]
