from django import forms
from .models import RestaurantLocation
from .validators import validate_category
from .utils import unique_slug_generator


class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
            'slug',
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

    def clean_slug(self):
        # Get this form's slug
        slug = self.cleaned_data.get('slug')
        # Get all slugs in the database
        slugs_in_db = self.instance.__class__.objects.filter(slug=slug)
        # Check if the form's slug is equal to the instance's slug - i.e. nothing has changed
        if slug == self.instance.slug:
            return slug
        # Check if the slug already exists in the database
        if slugs_in_db.exists():
            slug = unique_slug_generator(self.instance)
        return slug
