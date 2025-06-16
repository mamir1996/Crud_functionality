from django import forms 
from CRUD.models import Registration

class Profile(forms.ModelForm):
    class Meta:
        model=Registration
        fields='__all__'
        
        widgets ={
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"Enter your Name"
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }),
            'roll_num':forms.NumberInput(attrs={
                'class':'form-control',
                'placeholder':"Enter roll num"
            }),
             'subject':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"your subject here"
            })
        }