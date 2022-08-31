from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

from .models.modelsApp.LegalBusinessMasterModel import LegalCustomerModel

from .serializers import LegalCustomerModelSerializer


def get_legal_mst(id):
    print("Inside Legal Services")
    obj=LegalCustomerModel.objects.get(id=id)
    serializer=LegalCustomerModelSerializer(obj)
    print('serializer',serializer)
         
    legal_data=JSONRenderer().render(serializer.data)
    print('legal_data',legal_data)

    return legal_data

def post_legal_mst(request):
    
        data = JSONParser().parse(request)
        legal_post = LegalCustomerModelSerializer(data=data)
        if legal_post.is_valid():
            legal_post.save()
            return JsonResponse(legal_post.data, status=201)
        return JsonResponse(legal_post.errors, status=400)
