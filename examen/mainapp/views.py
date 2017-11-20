# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseForbidden

# Create your views here.
def index(req):
    return render(req,'index.html')



def authentificate_user(request):
    """
    Méthode d'authentification d'un utiulisateur à partir du formulaire
    :param request:
    :return:
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))

def logout_view(request):
    """
    Méthode de déconnexion de l'utilisateur
    :param request:
    :return:
    """
    logout(request)
    return HttpResponseRedirect(reverse('index'))



