from django import forms
from django.core import validators
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
#from project_app.models import Usr


class UserForm(forms.ModelForm):
#    name=forms.CharField(max_length=128,help_text="Name")
    password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    confirm_password=forms.CharField(widget=forms.PasswordInput)
#    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model=User
        fields=("username","first_name","last_name","email","password")

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class fform(forms.Form):
    email=forms.EmailField()
