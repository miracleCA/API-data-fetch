from django.forms import ModelForm
from .models import Crypto

class UpdateForm(ModelForm):
    class Meta:
        model = Crypto
        fields = ['cryptocurrency', 'price']