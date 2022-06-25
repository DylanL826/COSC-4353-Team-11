from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

class LoginPageView(TemplateView):
    template_name = 'sd_app/login.html'

class HomePageView(TemplateView):
    template_name = 'sd_app/home.html'

class ProfilePageView(TemplateView):
    template_name = 'sd_app/profile.html'

def registerPage(request):
    # '''Prompt user to register, after registering redirect to login page'''
    # return render(request, 'registration/register.html')
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("sd_app:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})


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
        return redirect(request, 'buy.html', {'total': total})
