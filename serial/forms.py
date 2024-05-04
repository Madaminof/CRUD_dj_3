from django.forms import ModelForm
from .models import Get_Actior


class ProductForm(ModelForm):
    class Meta:
        model = Get_Actior
        fields = '__all__'