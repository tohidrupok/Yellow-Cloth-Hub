from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import UserReview
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'first_name', 'last_name', 'email', 'password1', 'password2']
        
              
class UserProfileUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email'] 
        

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = [ 'rating',  'review_text' ]       