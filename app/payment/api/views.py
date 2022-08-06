from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from django.http import Http404
from ..models import Payment
from .serializers import PaymentSerializer
from rest_framework.response import Response
from rest_framework import status

class PaymentList(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except:
            raise Http404
        
    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = PaymentSerializer(instance,many=False)
        return Response(serializer.data)