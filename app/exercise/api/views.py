from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import Category, Exercise
from .serializers import CategorySerializer, ExerciseSerializer
from django.http import Http404

class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = CategorySerializer(instance, many=False)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = CategorySerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)