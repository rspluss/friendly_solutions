from django import forms
from images.models import Image, Album


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'