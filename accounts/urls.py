from django.urls import path
from accounts import views
from accounts.forms import CustomAuthForm, CustomPasswordChangeForm


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_view, name='login', kwargs={'authentication_form': CustomAuthForm}),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('password_change/', views.password_change_view, name='password_change', kwargs={'password_change_form': CustomPasswordChangeForm}),
]
