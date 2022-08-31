from django.db import models
from django.contrib.auth.models import User

from collapp.models.modelsApp.CustomerHstModel import CustomerAccountHstModel,CustomerHstModel
from collapp.models.modelsApp.ApplicationModel import CaseModel
from collapp.models.modelsApp.CustomerModel import CustomerModel,CustomerAccountModel
from collapp.models.modelsBase.BaseModel import AppBaseModel
from collapp.models.modelsApp.BusinessMasterModel import UnitMstModel,UnitLevelMstModel,ReasonMstModel



# Ganesh ->added case - MOD: 21/06/2022
# class CaseHstModel(AppBaseModel):
#     case_no = models.CharField(max_length=30,null=True)
#     class Meta:
#         db_table = "case_dtl_hst"    



 # Not creating the CaseHstModel since told during the BOM refresh caseid is not to be moved to history

class CaseCustomerHstModel(AppBaseModel):

    TELECALLER=0
    SKIP=1
    ESCALATED=2
    NOTTRACEABLE=3

    STAGE_CHOISE =[(TELECALLER,'Telecaller'),(SKIP,'Skip'),(ESCALATED,'Escalated'),(NOTTRACEABLE,'NotTraceable') ] 
    case_stage=models.IntegerField(default=0, choices=STAGE_CHOISE) 
    
    skip_unit_level=models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='Skip_case_unitlevel_hst',null=True)
    skip_unit =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='Skip_case_unit_hst',null=True)

    caseid = models.ForeignKey(CaseModel, on_delete=models.PROTECT,related_name='customer_case_caseid_hst')
    customer = models.ForeignKey(CustomerHstModel, on_delete=models.PROTECT,related_name='customer_case_customer_hst')
    customer_account = models.ForeignKey(CustomerAccountHstModel, on_delete=models.PROTECT,related_name='customer_case_customer_account_hst')  
    from_unit_level =  models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='customer_case_from_unitlevel_hst',null=True)            
    to_unit_level =  models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='customer_case_to_unitlevel_hst',null=True)  
    from_unit =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='customer_case_from_unit_hst',null=True)  
    to_unit =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='customer_case_to_unit_hst',null=True)  
    allocated_to = models.ForeignKey(User, on_delete=models.PROTECT,related_name='customer_case_allocatedto_hst',null=True)  
    last_allocation_date =  models.DateTimeField(blank=True, null=True) 
    reason = models.ForeignKey(ReasonMstModel, on_delete=models.PROTECT,related_name='customer_case_reason_hst',null=True)  
    remarks = models.CharField(max_length=200,null=True)

    escalated_unit_level       =  models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='Escalated_case_to_unitlevel_hst',null=True)
    escalated_unit             =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='Escalated_case_to_unit_hst',null=True)
    escalated_code             =  models.CharField(max_length=100,null=True) 
    escalation_last_updtd_date =  models.DateTimeField(blank=True, null=True)
    # action_type                =  models.CharField(max_length=100,null=True)
    # action_date                =  models.DateTimeField(blank=True, null=True) 

    class Meta:
        db_table = "case_linked_dtl_hst"  
#Note: To see how to migrate the field in the order it is written

class EscalatedCasesHstModel(AppBaseModel):

    customer = models.ForeignKey(CustomerModel, on_delete=models.PROTECT,related_name='customer_escalcase_customer_hst',null=True)
    customer_account = models.ForeignKey(CustomerAccountModel, on_delete=models.PROTECT,related_name='customer_escalcase_customer_account_hst',null =True)  
  
    escalated_unit_level       =  models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='Escalated_case_hst_unitlevel',null=True)
    escalated_unit             =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='Escalated_case_hst_unit',null=True)
    escalated_code             =  models.CharField(max_length=100,null=True) 
    escalation_last_updtd_date =  models.DateTimeField(blank=True, null=True)
    action_type                =  models.CharField(max_length=100,null=True)
    action_date                =  models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = "escalated_cases_hst"

