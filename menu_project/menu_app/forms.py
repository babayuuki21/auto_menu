from django import forms
from .models import Menu

class EditMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menu_name', 'menu_category_code', 'cooking_time']
