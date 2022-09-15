from django.contrib import admin
from .models.modelsApp.CustomerModel import CustomerAccountModel,CustomerAddressModel,CustomerModel,CommonCustomerModel
from .models.modelsBase.BaseModel import Tenant
from .models.modelsApp.ApplicationModel import CaseCustomerModel
# Register your models here.
admin.site.register(CustomerAccountModel)
admin.site.register(CustomerModel)
admin.site.register(Tenant)
admin.site.register(CommonCustomerModel)
admin.site.register(CaseCustomerModel)