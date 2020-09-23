# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class slider(models.Model):
    baslik = models.CharField(max_length=100)
    altbaslik = models.CharField(max_length=100)

    def __str__(self):
        return self.baslik

class service(models.Model):
    ad = models.CharField(max_length=50)
    icerik = models.CharField(max_length=200)

    def __str__(self):
        return self.ad

class testimonial(models.Model):
    baslik = models.CharField(max_length=50)
    altbaslik = models.CharField(max_length=200)
    yazan = models.CharField(max_length=200)

    def __str__(self):
        return self.baslik

class galery(models.Model):
    baslik = models.CharField(max_length=50)
    altbaslik = models.CharField(max_length=100)
    resim = models.FileField(upload_to='documents/', null=True, blank=False)

    def __str__(self):
        return self.baslik

class contact(models.Model):
    adsoyad = models.CharField(max_length=50, help_text="Ad :")
    telefon = models.CharField(max_length=50, help_text="Telefon :")
    eposta = models.CharField(max_length=50, help_text="Eposta :")
    konu = models.CharField(max_length=50, help_text="Konu :")
    mesaj = models.TextField(max_length=700,editable = True)
