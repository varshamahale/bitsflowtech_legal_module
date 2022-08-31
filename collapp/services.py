from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models.modelsApp.CustomerModel import CustomerAccountModel,CustomerAddressModel
from .serializers import *


def get_colapp_mst(id):
    print("Inside Colapp Services")
    obj=CustomerAccountModel.objects.get(id=id)
    serializer=CustomerAccountModelSerializer(obj)
    print('serializer',serializer)
         
    legal_data=JSONRenderer().render(serializer.data)
    print('legal_data',legal_data)

    return legal_data