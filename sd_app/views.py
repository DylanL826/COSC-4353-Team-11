from django.shortcuts import render
from django.http import HttpResponse


def loginPage(request):
    '''Prompt user to login, link to registration page'''
    return render(request, 'login.html')

def registerPage(request):
    '''Prompt user to register, after registering redirect to login page'''
    return render(request, 'register.html')

def buyPage(request):
    '''Prompt user to buy, after buying refresh page.
    Display total price of transaction.
    Link to logout.'''
    return render(request, 'buy.html')

def homePageView(request):
    '''Display home page, link to login page'''
    return HttpResponse('Hello, world. You are at the home page.')