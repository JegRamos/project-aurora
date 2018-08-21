from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request, authentication_form=AuthenticationForm):  # authentication_form is for overriding the style of the built in form
    if request.method == 'POST':
        form = authentication_form(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('index')
    else:
        form = authentication_form()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


@login_required(login_url='/accounts/login/')
def password_change_view(request, password_change_form=PasswordChangeForm):
    if request.method == 'POST':
        form = password_change_form(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
    else:
        form = password_change_form(request.user)

    context = {'form': form}
    return render(request, 'accounts/password_change.html', context)


@login_required(login_url='/accounts/login/')
def profile_view(request):
    return render(request, 'accounts/profile.html')
