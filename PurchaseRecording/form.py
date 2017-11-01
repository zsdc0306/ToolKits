from django import forms
from models import *


class GiftCardForm(forms.ModelForm):
    class Meta:
        model = GiftCard
        fields = ['brand', 'value', 'card_num', 'pin_num', 'remain_value', 'expire_date']
        widgets = {
            'brand': forms.Select(attrs={
                'class': 'form-control'
            }),
            'value': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'step': 'any',
            }),
            'card_num': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'pin_num': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'step': 'any',
            }),
            'remain_value': forms.NumberInput(attrs={
                'type': 'number',
                'step': 'any',
                'class': 'form-control'
            }),
            'expire_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }
