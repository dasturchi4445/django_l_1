from django.shortcuts import render


def home(request):
    return render(request, 'home_page.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def main(request):
    return render(request, 'main.html')
 