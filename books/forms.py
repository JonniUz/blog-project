from django import forms
from django.forms import fields
from .models import Review

class ReviewForm(forms.ModelForm):

    # body = forms.CharField(widget=forms.Textarea(attrs={'class': 'border rounded p-2 w-full', 'placeholder': 'Write your review here'}))
    # image = forms.ImageField(required=False)

    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['user', 'book']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'border rounded p-2 w-full', 'placeholder': 'Write your review here'
            })
        }