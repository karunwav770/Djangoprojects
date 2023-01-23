from django import forms
from django.forms import ModelForm
from testapp.models import Mymodel

class Myform(ModelForm):
    class Meta:
        model=Mymodel
        fields='__all__'
