from django.urls import path
from . import views


app_name = 'ntcadventures'
urlpatterns = [
    path('', views.home, name='home'),
    path('media/<entry_id>/', views.media, name='media'),
    path('add_entry/', views.add_entry, name='add_entry'),
    path('close_entry/<entry_id>/', views.close_entry, name='close_entry')
]
