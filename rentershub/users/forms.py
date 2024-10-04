from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


#form for registering a new user
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("email", "first_name", "last_name","phone_number", "age", "gender", "city",)



