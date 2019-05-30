from wtforms_alchemy import ModelForm
from app import User

class UserForm(ModelForm):
    class Meta:
        model = User
