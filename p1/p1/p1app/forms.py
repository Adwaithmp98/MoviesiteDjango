from django import forms
from . models import movies


class Movieform(forms.ModelForm):
    class Meta:
        model=movies
        fields=['name','desc','year','img']