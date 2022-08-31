from django.contrib import admin
from .models.modelsApp.CustomerModel import CustomerAccountModel,CustomerAddressModel
# Register your models here.
admin.site.register(CustomerAccountModel)