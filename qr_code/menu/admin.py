from django.contrib import admin
from .models import FoodItems

# Register your models here.
@admin.register(FoodItems)
class Fooditemadmin(admin.ModelAdmin):
    list_display =('name','price','category')
    search_fields = ('name','category')