from rest_framework import serializers
from ..models import Exercise, Category
from account.api.serializers import AccountSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
class ExerciseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    accounts = AccountSerializer()
    class Meta:
        model = Exercise
        fields = '__all__'