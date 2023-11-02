from .models import Staf
from django.forms import ModelForm, TextInput, EmailInput, Select


class StafForm(ModelForm):
    class Meta:
        model = Staf
        fields = ["name", "phone", "email", "ind", "program"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            "ind": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите индекс'
            }),
            "program": Select(attrs={
                'class': 'form-control',
            }, choices=[('Програмист', 'Програмист'),
                        ('WEB-дизайнер', 'WEB-дизайнер'),
                        ('Электрик', 'Электрик')]),
        }
