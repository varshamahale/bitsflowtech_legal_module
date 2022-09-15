from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import *
from .serializers import *


def get_collapp_mst(id):
    print("Inside Collapp Services")
    obj=CollappMstModel.objects.get(id=id)
    serializer=CollappMstModelSerializer(obj)
    print('serializer',serializer)
         
    vegeta_data=JSONRenderer().render(serializer.data)
    print('legal_data',legal_data)

    return legal_data