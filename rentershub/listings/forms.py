from django import forms
from .models import *

# Form for new property post
class PropertyPostForm(forms.ModelForm):
    class Meta:
        model = PropertyPost
        fields = ['property_type', 'city','location', 'price', 'bedrooms', 'bathrooms', 'toilets', 'electricity', 'water', 'description',]
