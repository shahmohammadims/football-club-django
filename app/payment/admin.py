from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('account' , 'price' , 'count_of_items')
    
    @admin.display()
    def count_of_items(self , obj):
        obj.items.all().count()
        return