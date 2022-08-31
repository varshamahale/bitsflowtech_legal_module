from rest_framework import serializers
# from .models import Customer
from rest_framework import generics
# from collapp.models.modelsBase import CustomerBaseModel
from .models.modelsApp.CustomerModel import CustomerAccountModel,CustomerAddressModel

class CustomerAccountModelSerializer(serializers.ModelSerializer):
                
        class Meta:
            model = CustomerAccountModel
            fields ='__all__'
        
        
        def create(self,validated_data):
            return CustomerAccountModel.objects.create(**validated_data)

class CustomerAddressModelSerializer(serializers.ModelSerializer):
             
    class Meta:
        model = CustomerAddressModel
        fields ='__all__'
    
    
    def create(self,validated_data):
          return CustomerAddressModel.objects.create(**validated_data)          


