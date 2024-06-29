from django.urls import path
from blog.views import home, login, register, main, payment, group, guardians, rating, settings

urlpatterns = [
    path('', home, name='home_page'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('main/', main, name='main'),
    path('payment/', payment, name='payment'),
    path('group/', group, name='group'),
    path('guardians/', guardians, name='guardians'),
    path('rating/', rating, name='rating'),
    path('settings/', settings, name='settings'),

]
