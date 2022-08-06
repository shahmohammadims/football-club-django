from rest_framework.generics import ListAPIView
from .serializers import AccountSerializer
from ..models import Account
class AccountList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer