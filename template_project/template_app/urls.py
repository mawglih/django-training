from django.urls import path
from template_app import views

app_name = 'app'
urlpatterns = [
  path('relative/',views.relative,name='relative'),
  path('other/',views.other,name='other'),
]