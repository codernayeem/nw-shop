from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import get_user_model, hashers


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(request.GET.get('next') or '/')

    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if not (username and password):
            request.session['login_error'] = 'Invalid Information'
        else:
            try:
                user = get_user_model().objects.get(username=username)
                if user.check_password(password):
                    auth.login(request, user)
                    return HttpResponseRedirect(request.GET.get('next') or '/')
            except:
                pass

            request.session['login_error'] = 'Incorrect username or password.'
            request.session['login_user'] = username
        return HttpResponseRedirect('/account/login')
        
    else:
        login_error = request.session.get('login_error')
        login_user = request.session.get('login_user')

        if login_error:
            request.session.pop('login_error')
        if login_user:
            request.session.pop('login_user')

        context = {
            'login_error' : login_error,
            'login_user' : login_user,
        }
        
        return render(request, 'login.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect(request.GET.get('next') or '/')
