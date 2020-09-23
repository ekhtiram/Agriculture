# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import slider, service, testimonial, galery, contact
from .forms import contactForm


def home(request):
    sliders = slider.objects.all()
    services = service.objects.all()
    testimonials = testimonial.objects.all()
    context = {"sliders":sliders,"services":services,"testimonials":testimonials}
    return render(request, 'agroapp/home.html', context)

def gallery(request):
    galerys = galery.objects.all()
    context = {"galerys":galerys}
    return render(request, 'agroapp/gallery.html', context)

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/contact/')
        else:
            print (form.errors)
    else:
        form = contactForm()
    context = {"form":form}
    return render(request, 'agroapp/contact.html', context)
