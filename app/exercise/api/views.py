from rest_framework.generics import ListCreateAPIView
from ..models import Category, Exercise
from .serializers import CategorySerializer, ExerciseSerializer

class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer