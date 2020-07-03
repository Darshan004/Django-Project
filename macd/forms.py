from django.forms import ModelForm
from .models import values


class InputsForm(ModelForm):
    class Meta:
        model = values
        fields = '__all__'
