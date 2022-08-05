from rest_framework.generics import ListAPIView
from ..models import Payment
from .serializers import PaymentSerializer
class PaymentList(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer