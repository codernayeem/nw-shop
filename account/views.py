from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import get_user_model, hashers
import string


def check_pattern(text, *patterns):
    allowed_char = []
    for pattern in patterns:
        if pattern == "A-Z":
            for a in string.ascii_uppercase[:26]:
                allowed_char.append(a)
        elif pattern == "a-z":
            for a in string.ascii_lowercase[:26]:
                allowed_char.append(a)
        elif pattern == "0-9":
            for a in range(0, 10):
                allowed_char.append(str(a))
        else:
            for a in pattern:
                allowed_char.append(a)

    for a in text:
        if a not in allowed_char:
            return False
    return True


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
        signup_info = request.session.get('signup_info')

        if login_error:
            request.session.pop('login_error')
        if login_user:
            request.session.pop('login_user')
        if signup_info:
            request.session.pop('signup_info')

        context = {
            'login_error' : login_error,
            'login_user' : login_user,
            'signup_info' : signup_info,
        }
        
        return render(request, 'login.html', context)


def signup_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(request.GET.get('next') or '/')

    if request.method == "POST":
        context = {}
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip().lower()
        
        if not username:
            context['errorUsername'] = "Username can not be empty."
        elif len(username) < 3:
            context['errorUsername'] = "Username is too short."
        elif len(username) > 20:
            context['errorUsername'] = "Username is too long."
        elif not check_pattern(username, "A-Z", "a-z", "0-9"):
            context['errorUsername'] = "Allowed character is A-Z, a-z, 0-9 only. Please, correct it."
        else:
            try:
                get_user_model().objects.get(username=username)
                context['errorUsername'] = "This username is already used."
            except:
                pass

        if not password:
            context['errorPassword'] = "Password can not be empty."
        elif len(password) < 6:
            context['errorPassword'] = "Password is too short."
        elif len(password) > 32:
            context['errorPassword'] = "Password is too long."
        elif password.isnumeric():
            context['errorPassword'] = "Password can not be entirely numeric. Use some characters too."
        else:
            try:
                password = hashers.make_password(password)
            except:
                context['errorPassword'] = "Password is invalid."

        if not first_name:
            context['errorFirst_name'] = "First name can not be empty."
        elif len(first_name) < 2:
            context['errorFirst_name'] = "First name is too short."
        elif len(first_name) > 32:
            context['errorFirst_name'] = "First name is too long."
        elif not check_pattern(first_name, "A-Z", "a-z", ". "):
            context['errorFirst_name'] = "Invalid name. Please, change it."

        if not last_name:
            context['errorLast_name'] = "Last name can not be empty."
        elif len(last_name) < 2:
            context['errorLast_name'] = "Last name is too short."
        elif len(last_name) > 32:
            context['errorLast_name'] = "Last name is too long."
        elif not check_pattern(last_name, "A-Z", "a-z", ". "):
            context['errorLast_name'] = "Invalid name. Please, change it."

        if not email:
            context['errorEmail'] = "Email can not be empty."
        elif not check_pattern(email, "a-z", "0-9", ".@"):
            context['errorEmail'] = "Your email is not valid."

        if context.get('errorUsername') or context.get('errorPassword') or context.get('errorFirst_name') or context.get('errorLast_name') or context.get('errorEmail'):
            request.session['signup_errorUsername'] = context.get('errorUsername', None)
            request.session['signup_defaultUsername'] = username
            request.session['signup_errorPassword'] = context.get('errorPassword', None)
            request.session['signup_errorFirst_name'] = context.get('errorFirst_name', None)
            request.session['signup_defaultFirst_name'] = first_name
            request.session['signup_errorLast_name'] = context.get('errorLast_name', None)
            request.session['signup_defaultLast_name'] = last_name
            request.session['signup_errorEmail'] = context.get('errorEmail', None)
            request.session['signup_defaultEmail'] = email
            
            return HttpResponseRedirect("/account/signup/")
        else:
            get_user_model().objects.get_or_create(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_staff=False,
                is_active=True,
                is_superuser=False,
            )
            request.session['signup_info'] = 'Registration Succesfull'
            return HttpResponseRedirect("/account/login")

    else:
        signup_error = request.session.get('signup_error')
        errorUsername = request.session.get('signup_errorUsername')
        defaultUsername = request.session.get('signup_defaultUsername', '')
        errorPassword = request.session.get('signup_errorPassword')
        errorFirst_name = request.session.get('signup_errorFirst_name')
        defaultFirst_name = request.session.get('signup_defaultFirst_name', '')
        errorLast_name = request.session.get('signup_errorLast_name')
        defaultLast_name = request.session.get('signup_defaultLast_name', '')
        errorEmail = request.session.get('signup_errorEmail')
        defaultEmail = request.session.get('signup_defaultEmail', '')

        if signup_error:
            request.session.pop('signup_error')
        if errorUsername:
            request.session.pop('signup_errorUsername')
        if defaultUsername:
            request.session.pop('signup_defaultUsername')
        if errorPassword:
            request.session.pop('signup_errorPassword')
        if errorFirst_name:
            request.session.pop('signup_errorFirst_name')
        if defaultFirst_name:
            request.session.pop('signup_defaultFirst_name')
        if errorLast_name:
            request.session.pop('signup_errorLast_name')
        if defaultLast_name:
            request.session.pop('signup_defaultLast_name')
        if errorEmail:
            request.session.pop('signup_errorEmail')
        if defaultEmail:
            request.session.pop('signup_defaultEmail')

        context = {
            'signup_error' : signup_error,
            'errorUsername' : errorUsername,
            'defaultUsername' : defaultUsername,
            'errorPassword' : errorPassword,
            'errorFirst_name' : errorFirst_name,
            'defaultFirst_name' : defaultFirst_name,
            'errorLast_name' : errorLast_name,
            'defaultLast_name' : defaultLast_name,
            'errorEmail' : errorEmail,
            'defaultEmail' : defaultEmail,
        }
        return render(request, 'signup.html', context)


def logout_view(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return HttpResponseRedirect(request.GET.get('next') or '/')
