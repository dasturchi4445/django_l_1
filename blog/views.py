from django.shortcuts import render


def home(request):
    return render(request, 'home_page.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def main(request):
    return render(request, 'main.html')


def payment(request):
    return render(request, 'payment.html')


def group(request):
    return render(request, 'group.html')


def guardians(request):
    return render(request, 'guardians.html')


def rating(request):
    return render(request, 'rating.html')


def settings(request):
    return render(request, 'settings.html')
