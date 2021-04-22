from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from database.models import Product
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
                return render(request, 'users/signup.html', {'form': SignUpForm(), 'error': 'Cet email est déjà pris. Merci d\'en choisir un nouveau.'})
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
    myproducts = Product.objects.filter(myproduct=request.user)
    return render(request, 'users/myproducts.html', {'myproducts': myproducts})


@login_required
def myproducts_delete(request, product):
    ''' '''
    myproduct = Product.objects.get(prod_id=product)
    myproduct.myproduct.clear()
    return redirect('myproducts')
