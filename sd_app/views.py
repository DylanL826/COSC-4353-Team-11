from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

class LoginPageView(TemplateView):
    template_name = 'sd_app/login.html'

class HomePageView(TemplateView):
    template_name = 'sd_app/home.html'

class ProfilePageView(TemplateView):
    template_name = 'sd_app/profile.html'

def registerPage(request):
    '''Prompt user to register, after registering redirect to login page'''
    return render(request, 'register.html')

def buyPage(request):
    '''Prompt user to buy, after buying refresh page.
    Display total price of transaction.
    Link to logout.'''
    return render(request, 'buy.html')

def buyPageCalculation(request):
    '''Calculate total price of transaction'''
    if request.method == 'POST':
        quantity = request.POST['quantity']
        price = request.POST['price']
        total = float(quantity) * float(price)
        request.session['total'] = total # store total in session
        return redirect(request, 'buy.html', {'total': total}) # 
