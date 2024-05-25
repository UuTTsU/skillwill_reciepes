from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
   class Meta:
       model = Recipe
       fields = ('id','name','ingredient','time','process', 'user')
       read_only_fields = ['user']