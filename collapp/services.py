from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models.modelsApp.CustomerModel import CustomerAccountModel,CustomerAddressModel
from .serializers import *

def get_colapp_mst(id):
    print("Inside Customer Services")
    obj=CustomerModel.objects.get(id=id)
    serializer=CustomerModelSerializer(obj)
    print('serializer',serializer)
         
    data=JSONRenderer().render(serializer.data)
    print('customer_data',data)

    return data
