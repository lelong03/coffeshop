from django.contrib import admin
from .models import Category, Drink, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Drink)
admin.site.register(Order)