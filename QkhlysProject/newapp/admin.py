from django.contrib import admin

# Register your models here.
from .models import City, Company

admin.site.register(City)
admin.site.register(Company)