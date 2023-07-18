from .models import Tweet
from django import forms


class TweetForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.Textarea(
                               attrs={
                                   'placeholder': 'Enter Your Tweet !',
                                   'class': 'form-control'
                               }
                           ),
                           label='',
                           )
    class Meta:
        model = Tweet
        exclude = ['user']
