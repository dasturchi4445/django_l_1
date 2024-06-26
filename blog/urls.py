from django.urls import path
from blog.views import home, login, register, main

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('main/', main, name='main'),
]
