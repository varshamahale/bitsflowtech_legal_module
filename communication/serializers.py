from rest_framework import serializers
from .models import *
from collapp.models.modelsApp.CustomerModel import CustomerModel,CustomerAccountModel
class ArticleSerializer(serializers.ModelSerializer):
             
    class Meta:
        model = Article
        fields ='__all__'

    
    def create(self,validated_data):
          return Article.objects.create(**validated_data)

class CustomerModelSerializer(serializers.ModelSerializer):
             
    class Meta:
        model = CustomerModel
        fields ='__all__'

    
    def create(self,validated_data):
          return CustomerModel.objects.create(**validated_data)


class CustomerAccountModelSerializer(serializers.ModelSerializer):
             
    class Meta:
        model = CustomerAccountModel
        fields ='__all__'

    
    def create(self,validated_data):
          return CustomerAccountModel.objects.create(**validated_data)
