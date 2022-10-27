from django import forms
from images.models import Image, Album


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'albumId', 'image', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'albumId': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UpdateImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'albumId', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'albumId': forms.TextInput(attrs={'class': 'form-control'}),
        }