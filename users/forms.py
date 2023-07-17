from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserRegisterForm(UserCreationForm):
    '''Форма для регистрации пользователя'''
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class UserProfileForm(UserChangeForm):
    '''Форма для просмотра и изменения данных пользователя'''
    class Meta:
        model = User
        fields = ('email', 'full_name',)

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
