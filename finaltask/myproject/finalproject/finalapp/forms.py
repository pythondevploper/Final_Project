from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django import forms


from django.forms.widgets import PasswordInput,TextInput
from . models import Movie
from .models import Review
#Registering a user
class Createuser(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

#login

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
     

#create movie
class CreateMovieForm(forms.ModelForm):

    class Meta:

        model=Movie
        fields=['movie_title','poster','description','release_date','cast','category','youtube_trailer_link']

#update movie

class UpdateMovieForm(forms.ModelForm):

    class Meta:

        model=Movie
        fields=['movie_title','poster','description','release_date','cast','category','youtube_trailer_link']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }




