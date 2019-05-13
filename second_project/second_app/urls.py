from django.urls import path
from second_app import views

urlpatterns = [
  path('index',views.index,name='index'),
  path('users',views.users,name='users'),
  path('signup',views.signup,name='signup'),
]