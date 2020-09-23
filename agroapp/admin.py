from django.contrib import admin
from . import models
from .models import slider, service, testimonial, galery, contact

# Register your models here.

class sliderAdmin(admin.ModelAdmin):
    list_display = ("baslik","altbaslik")
    list_per_page = 20
    search_fields = ("baslik",)

class serviceAdmin(admin.ModelAdmin):
    list_display = ("ad","icerik")
    list_per_page = 20
    search_fields = ("baslik",)

class testimonialAdmin(admin.ModelAdmin):
    list_display = ("baslik","altbaslik","yazan")
    list_per_page = 20
    search_fields = ("baslik",)

class galeryAdmin(admin.ModelAdmin):
    list_display = ("baslik","altbaslik","resim")
    list_per_page = 20
    search_fields = ("baslik",)

class contactAdmin(admin.ModelAdmin):
    list_display = ("adsoyad","telefon","eposta","konu","mesaj")
    list_per_page = 20
    search_fields = ("adsoyad",)


admin.site.register(slider, sliderAdmin)
admin.site.register(service, serviceAdmin)
admin.site.register(testimonial, testimonialAdmin)
admin.site.register(galery, galeryAdmin)
admin.site.register(contact, contactAdmin)
