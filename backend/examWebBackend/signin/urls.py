from django.urls import path
from . import views

app_name = 'signip'

urlpatterns = [
    path('', views.sign_in, name='signin'),
    # Other signup-related URLs can be defined here
]