from django.urls import path
from gsheets import views


app_name = 'gsheets'
urlpatterns = [
    path('', views.home_view, name='home')
]
