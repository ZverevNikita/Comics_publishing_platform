from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group

admin.site.unregister(Group)

= 'Комиксы'
AdminSite.site_header = 'Комиксы'
