from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from webapp.models import Profile


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField( required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField( max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField( max_length=50, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'password1','password2','first_name','last_name','email')
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs )
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'
   

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['contact','profile_picture']
