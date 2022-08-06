from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import AccountSerializer
from ..models import Account
class AccountList(ListAPIView, CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

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
    
    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = AccountSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)