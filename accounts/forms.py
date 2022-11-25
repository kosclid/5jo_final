from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import User


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "gender",
            "age",
        )

    field_order = ["username", "password1", "password2", "gender", "age"]


class UsereditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "gender", "age")

    field_order = ["username", "email", "gender", "age"]
