from rest_framework import serializers
from ..models import Account

class Accountserializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone_number', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'debt', 'exercises_not_payment']