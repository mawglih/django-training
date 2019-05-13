from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
  return render(request,'basicapp/index.html')

def form_view(request):
  form = forms.FormName()
  if request.method == 'POST':
    form = forms.FormName(request.POST)
    if form.is_valid():
      print("Validation success")
      print("NAME: "+form.cleaned_data['name'])
      print("Email: "+form.cleaned_data['email'])
      print("TEXT: "+form.cleaned_data['text'])
  return render(request,'basicapp/form_page.html',{'form':form})