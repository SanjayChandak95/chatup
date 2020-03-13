from django import forms
from .models import User,ChatTable

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
        'email',
        'password',
        'securityQuestion',
        'securityQuesAnswer',
        ]
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data["email"]
        if len(User.objects.filter(email = email)) > 0:
            raise forms.ValidationError("Email should be unique")
        else:
            return email

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
        'email',
        'password'
        ]

#we can make this in signup form also as both are same but to not to be confused we are adding it
class ForgetPassword(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
        'email',
        'password',
        'securityQuestion',
        'securityQuesAnswer',
        ]

class ChatTableForm(forms.ModelForm):
    class Meta:
        model = ChatTable
        fields = [
        'message',
        ]
