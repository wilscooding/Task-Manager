from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, max_length=150)
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput, max_length=150
    )
