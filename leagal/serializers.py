from rest_framework import serializers
from .models import *


# class XicorMstModelSerializer(serializers.ModelSerializer):
             
#     class Meta:
#         model = XicorMstModel
#         fields ='__all__'
from .models.modelsApp.LegalBusinessMasterModel import LegalCustomerModel

class LegalCustomerModelSerializer(serializers.ModelSerializer):
             
    class Meta:
        model = LegalCustomerModel
        fields ='__all__'
    
    
    def create(self,validated_data):
          return LegalCustomerModel.objects.create(**validated_data)
