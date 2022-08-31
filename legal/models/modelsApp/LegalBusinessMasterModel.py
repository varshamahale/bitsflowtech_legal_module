# from time import clock_settime
from django.db import models
from legal.models.modelsBase.LegalMasterBase import LegalMstBaseModel
# from collapp.models.modelsApp.CustomerModel import CustomerModel,CustomerPaymentsModel,CustomerAccountModel
# from collapp.models.modelsApp.ApplicationModel import CaseCustomerModel
# from collapp.models.modelsApp.BusinessMasterModel import ReasonMstModel
# Create your models here.


class LegalCustomerModel(LegalMstBaseModel):
      # customer = models.ForeignKey( CustomerModel, on_delete=models.CASCADE,null=True)
      # cust_payment = models.ForeignKey(CustomerPaymentsModel, on_delete=models.CASCADE,null=True)
      # cust_acc = models.ForeignKey(CustomerAccountModel, on_delete=models.CASCADE,null=True)
      # cust_case = models.ForeignKey(CaseCustomerModel, on_delete=models.CASCADE,null=True)
      # reason = models.ForeignKey(ReasonMstModel, on_delete=models.CASCADE,null=True)
      
      class Meta:
            db_table='legal_tbl'
# class abc():
    #   name=models.CharField(max_length=50)
