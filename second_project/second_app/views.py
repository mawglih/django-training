from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import User
from second_app.forms import FormName

# Create your views here.
def index(request):
  return render(request,'second_app/index.html')

def users(request):
  user_list = User.objects.order_by('last_name')
  user_dict = {'user_records':user_list}
  return render(request,'second_app/users.html',context=user_dict)

def signup(request):
  form = FormName()
  if request.method == 'POST':
    form = FormName(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return index(request)
    else:
      print('Error form invalid')
  return render(request,'second_app/signup.html',{'form':form})