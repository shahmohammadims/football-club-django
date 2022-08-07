from rest_framework import serializers
from ..models import Payment
from account.api.serializers import AccountSerializer
class PaymentSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = Payment
        fields = ['account','price','items']
        