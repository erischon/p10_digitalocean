from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Password
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# from django.contrib import messages

from database.models import Substitute
from users.forms import SignUpForm


def signupuser(request):
    ''' '''
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect('moncompte')
            except IntegrityError:
                return render(request, 'users/signup.html', {'form': SignUpForm(), 'error': 'Ce nom est déjà pris. Merci d\'en choisir un nouveau.'})
        else:
            return render(request, 'users/signup.html', {'form': SignUpForm(), 'error': 'Les mots de passe ne sont pas identiques.'})
    else:
        return render(request, 'users/signup.html', {'form': SignUpForm()})


def loginuser(request):
    ''' '''
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users/login.html', {'form': AuthenticationForm(), 'error': "Username and password did not match."})
        else:
            login(request, user)
            return redirect('moncompte')
    else:
        return render(request, 'users/login.html', {'form': AuthenticationForm()})


@login_required
def logoutuser(request):
    ''' '''
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def moncompte(request):
    ''' '''
    return render(request, 'users/moncompte.html')


@login_required
def myproducts(request):
    ''' '''
    myproducts = Substitute.objects.filter(user=request.user)
    return render(request, 'users/myproducts.html', {'myproducts': myproducts})


@login_required
def myproducts_delete(request, product):
    ''' '''
    myproduct = Substitute.objects.get(id=product)
    myproduct.delete()
    return redirect('myproducts')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)

        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))

            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "users/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '46.101.141.242',
                        'site_name': 'The Substitute',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }

                    email = render_to_string(email_template_name, c)

                    try:
                        send_mail(subject, email, 'erischondev@gmail.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect('password_reset_done')

    password_reset_form = PasswordResetForm()

    return render(request=request, template_name="users/password/password_reset.html", context={"password_reset_form": password_reset_form})
