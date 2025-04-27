from django.contrib.auth.forms import UserCreationForm

from password_manager.models import PasswordDataUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = PasswordDataUser
        fields = ('username', 'password1', 'password2')
