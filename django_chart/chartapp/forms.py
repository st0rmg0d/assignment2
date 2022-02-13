from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'Balance': forms.TextInput(attrs={'class': 'form-control'}),
        }
