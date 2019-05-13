from django import forms
from second_app.models import User

class FormName(forms.ModelForm):
  class Meta:
    model = User
    fields = '__all__'