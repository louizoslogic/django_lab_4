from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('register/', views.register, name="register"),
    path('login_page/', views.login_page, name="login_page"),
    path('login_form/', views.login_form, name="login_form"),
    path('', views.home, name="home"),
    path('logout/', views.logout_user, name="logout")
    ]
