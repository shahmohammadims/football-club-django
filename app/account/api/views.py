from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .serializers import AccountSerializer
from ..models import Account
class AccountList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Account.objects.get(phone_number=pk)
        except:
            raise Http404
    
    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = AccountSerializer(instance,many=False)
        return Response(serializer.data)
