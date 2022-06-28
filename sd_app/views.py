from django.shortcuts import render, redirect


from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import NewUserForm, ProfileForm


class LoginPageView(TemplateView):
    template_name = 'sd_app/login.html'

class HomePageView(TemplateView):
    template_name = 'sd_app/home.html'
    #print("\t\tHome page rendered\n")

@login_required
def profilePage(request):
    '''Display user profile information and allow them to update profile information'''
    if request.method == 'POST': # Form has been submitted
        print("\t\tPOST request received\n")
        #user_form = NewUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if profile_form.is_valid():
            print("\t\tForms are valid\n")
            #user_form.save()
            profile_form.save()            
            return redirect('sd_app:profile')
        else:
            print("\t\tForms are invalid\n")
    else: # GET request, display current information
        print("\t\tGET request received\n") 
        profile_form = ProfileForm(instance=request.user.userprofile)
    context = {'profile_form': profile_form}
    return render(request, 'sd_app/profile.html', context)    

def registerPage(request):
    # '''Prompt user to register, after registering redirect to login page'''
    # return render(request, 'registration/register.html')  
    #print("\t\tRegister page view call\n")
    if request.method != 'POST':
        # Display a blank registration form.
        #print("\t\tGET request received\n")
        form = NewUserForm()
    if request.method == "POST":
        #print("\t\tPOST request received\n")
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            print("\t\tForm is valid\n")
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("sd_app:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    
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
