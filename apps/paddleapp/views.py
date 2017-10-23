from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib.messages import error

def index(request):

    return render(request, "paddleapp/index.html")

def buy(request):
    try:
        request.session['counter']
    except KeyError:
        request.session['counter'] = 0



    request.session['counter'] += int(request.POST['quantity'])

    price = {
        "1" : 1429.00,
        "2" : 1890.00,
        "3" : 1543.00,
        "4" : 1429.00,
        "5" : 1890.00,
        "6" : 1543.00,
    }

    quantity = request.POST['quantity']
    product = request.POST['product']
    request.session['total'] = int(quantity) * price[product]


    if 'total_purchase' not in request.session:
        request.session['total_purchase'] = request.session["total"]

    else:
        request.session['total_purchase'] += request.session['total']


    request.session.modified = True
    return redirect('/result')

def result(request):
    return render(request, "paddleapp/checkout.html")






################################LOGIN REGISTRATION#####################


def display(request):
    context= {
        'users': User.objects.all()
    }
    return render(request, 'paddleapp/display.html', context)


def registration(request):
    return render(request, 'paddleapp/registration.html')

def new(request):
    return render(request, 'restful_users/new.html')

def create(request):
    errors= User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/users/new')

    User.objects.create(
        first_name= request.POST['first_name'],
        last_name= request.POST['last_name'],
        email= request.POST['email'],
    )
    return redirect('/users')

def edit(request,user_id):
    context= {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'restful_users/edit.html', context)

def show(request,user_id):
    context= {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'restful_users/show.html', context)

def destroy(request,user_id):
    User.objects.get(id=user_id).delete()
    return HttpResponseRedirect('/users')

def update(request,user_id):
    errors= User.objects.validate(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            error(request, message, extra_tags=field)
        return redirect('/users/{}/edit'.format(user_id))
    user_update = User.objects.get(id=user_id)
    user_update.first_name= request.POST['first_name']
    user_update.last_name= request.POST['last_name']
    user_update.email= request.POST['email']
    user_update.save()
    return redirect('/users')
