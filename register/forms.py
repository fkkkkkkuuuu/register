from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import TextInput, Textarea, ModelForm
from .models import UserRole

User = get_user_model()


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),

    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ('role',)
