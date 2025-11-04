from django import forms

from user_app.models import User


class Userregister(forms.ModelForm):

    class Meta:

        model = User

        fields = ['username', 'email', 'password']

