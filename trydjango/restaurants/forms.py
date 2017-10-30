from django import forms
from .models import RestaurantLocation
from .validators import validate_category

# Old one
# class RestaurantCreateForm(forms.Form):
#     name            = forms.CharField(required=True)
#     location        = forms.CharField(required=False)
#     category        = forms.CharField(required=False)


class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
        ]

    # Custom validation of the "name" field
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if name == 'Hello':
    #         raise forms.ValidationError('Not a valid name.')
    #     return name

    # Custom validation of the "email" field
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if 'edu' in email:
    #         raise forms.ValidationError('We do not accept edu emails.')
    #     return email