from django.urls import path
from basicapp import views

urlpatterns = [
  path('index',views.index,name='index'),
  path('forms',views.forms,name='form_view'),
]