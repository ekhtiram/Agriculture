# -*- coding: utf-8 -*-
from django import forms
from .models import contact


class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ("adsoyad","telefon","eposta","konu","mesaj")
