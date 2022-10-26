from django import forms
from images.models import Image, Album


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'album', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'album': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
