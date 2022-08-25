from django.forms import ModelForm
from django.forms import TextInput
from .models import Contact
from django import forms


class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'subject']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Ваше имя',
                                     'autocomplete': 'off'}),
            'phone': TextInput(attrs={'placeholder': 'Ваш телефон', 
                                      'type': 'tel', 
                                      'pattern': '^[\\d() +-]+$',
                                      'minlength': '6',
                                      'title': 'Пример: 79501234567',
                                      'autocomplete': 'off'}),
            'subject': TextInput(attrs={'placeholder': 'Укажите предмет (необязательно)',
                                        'autocomplete': 'off'})
        }
        