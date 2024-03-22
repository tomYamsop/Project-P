from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserLoginForms(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')