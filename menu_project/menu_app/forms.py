from django import forms
from .models import Menu

class EditMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menu_name', 'cooking_time', 'menu_category_code']

    # カテゴリーフィールドの表示名を取得
    def __init__(self, *args, **kwargs):
        super(EditMenuForm, self).__init__(*args, **kwargs)
        self.fields['menu_category_code'].label_from_instance = lambda obj: f'{obj.category_name} ({obj.category_code})'
