from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile, Transaction



# Creates a form for the user to register a new user account.
class NewUserForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {  'username': 'Username', 'password1': 'Password', 
                    'password2': 'Confirm Password'}    
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)		
        if commit:
            user.save()
        return user

# Create a form for the user to update their profile information.
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile 
        fields = ('full_name', 'address', 'city', 'state', 'zip_code')      

class BuyForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('amount', 'location', 'date', 'delivery_date')