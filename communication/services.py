from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from collapp.models.modelsApp.CustomerModel import CustomerModel,CustomerAccountModel
from .models import *
from .serializers import *



    
def get_colapp_mst(request):
    cust=get_cust_dtl(request.data['customer_id'])
    # cust_acc=get_acc_dtl(request.data['account_id'])
    # temp=get_temp(request.data['template_id'])
    return request

def get_cust_dtl(cust_id):
    print("Inside cust dtl services Services")
    obj=CustomerModel.objects.filter(id=cust_id)
    print(obj)
    serializer=CustomerModelSerializer(obj)
    print('serializer',serializer.data)
         
    cust_data=JSONRenderer().render(serializer.data)
    print('customer data',cust_data)

    return cust_data

def get_acc_dtl(acc_id):
    print("Inside cust acount dtl  Services")
    obj=CustomerAccountModel.objects.get(id=acc_id)
    serializer=CustomerAccountModelSerializer(obj)
    print(obj)
    print('serializer',serializer)
    cust_acc_data=JSONRenderer().render(serializer.data)
    print('customer  account data',cust_acc_data)
    return cust_acc_data


def get_temp(temp_id):
    print("Inside Article dtl  Services")
    obj=Article.objects.get(id=temp_id)
    print(obj)
    serializer=ArticleSerializer(obj)
    print('serializer',serializer)
    cust_temp_data=JSONRenderer().render(serializer.data)
    print('customer  template data',cust_temp_data)
    return cust_temp_data