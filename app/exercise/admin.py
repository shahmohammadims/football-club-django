from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    search_fields = ('name','price')
    
    
@admin.register(models.Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('date','category')
    list_filter = ('date','category')