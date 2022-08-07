from rest_framework import serializers
from ..models import Payment
from account.models import Account

class AccountForPayment(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['full_name']
class PaymentSerializer(serializers.ModelSerializer):
    account = AccountForPayment()
    class Meta:
        model = Payment
        fields = ['account','price','items']
        