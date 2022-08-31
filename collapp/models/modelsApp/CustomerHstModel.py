from django.db import models
from django.contrib.auth.models import User
from .GenericMasterModel import Country, MetadataParameterModel,SourceHostMstModel, State
from .BusinessMasterModel import DispositionCodeMstModel,UnitMstModel,UnitLevelMstModel,ProductMstModel
from .CustomerModel import CommonCustomerModel
from collapp.models.modelsBase.BaseModel import AppBaseModel
from collapp.models.modelsBase.CustomerBaseModel import *

# customer details models

class CustomerTmpHstModel(CustomerTmpBaseModel):
    source_host     = models.ForeignKey(SourceHostMstModel, on_delete=models.PROTECT,related_name='customertmphst_source_host',null=True)
    class Meta:
        db_table = "customer_tmp_hst"

class CustomerHstModel(CustomerBaseModel):
    ccn = models.ForeignKey(CommonCustomerModel, on_delete=models.PROTECT,related_name='customerhst_ccno',null=True)
    class Meta:
        verbose_name = 'Customer Hst'
        verbose_name_plural = 'Customers Hst'   
        db_table = "customer_hst"

class CustomerAccountHstModel(CustomerAccountBaseModel):
    customer = models.ForeignKey(CustomerHstModel, on_delete=models.PROTECT,related_name='Customer_accounthst_customer_id')
    product  = models.ForeignKey(ProductMstModel, on_delete=models.PROTECT,related_name='Customer_accounthst_product_id',null=True)
    
    class Meta:
        db_table = "customer_account_hst"   

# class CustomerCreditCardHstModel(CustomerCreditCardBaseModel):
#     customer = models.ForeignKey(CustomerHstModel, on_delete=models.PROTECT,related_name='Customer_creditcardhst_customer_id')
#     class Meta:
#         db_table = "customer_card_hst"           

class CustomerAddressHstModel(CustomerAddressBaseModel):
    customer= models.ForeignKey(CustomerHstModel, on_delete=models.PROTECT,related_name='Customer_addressHstModel_customer')
    customer_account = models.ForeignKey(CustomerAccountHstModel, on_delete=models.PROTECT,related_name='Customer_Addresshst_customer_account')
    #mailing adress / alt adress / office address / coapp address / employer / othe reference
    address_type = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='Customer_Addresshst_metadata_address')
    country=models.ForeignKey(Country, on_delete=models.PROTECT,related_name='additional_country_hst',null=True)
    state=models.ForeignKey(State, on_delete=models.PROTECT,related_name='additional_state_hst',null=True)
    class Meta:
        db_table = "customer_address_hst"      

# Ganesh - Added the cust_phone_type field in the "CustomerOtherPhonesHstModel"  model - Date of Submit - 16/06/2022
class CustomerOtherPhonesHstModel(CustomerOtherPhonesBaseModel):

    cust_phone_type = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='Customer_Metadata_Phonehst_Type',null=True)
    cust_contact_category = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='Customer_Metadata_Contacthst_Category',verbose_name="Contact Category",null=True)
    customer_account = models.ForeignKey(CustomerAccountHstModel, on_delete=models.PROTECT,related_name='Customer_other_Phoneshst_customer_account',null =True,blank =True)
    customer= models.ForeignKey(CustomerHstModel, on_delete=models.PROTECT,related_name='Customer_Other_Phoneshst_customer_id',null=True)

   
    class Meta:
        db_table = "customer_other_phone_hst"   

######################################################  ENDS HERE ########################################################


class CustomerCollateralHstModel(CustomerCollateralBaseModel):
    customer = models.ForeignKey(CustomerHstModel, on_delete=models.PROTECT,related_name='Customer_collateralhst_customer_id')
    customer_account = models.ForeignKey(CustomerAccountHstModel, on_delete=models.PROTECT,related_name='Customer_collateralhst_customer_account')
    class Meta:
        db_table = "customer_collateral_hst"   
        

class FollowUpHstModel(FollowUpBaseModel):
    customer = models.ForeignKey(CustomerHstModel, on_delete=models.PROTECT,related_name='followup_customerhst_id')
    customer_account = models.ForeignKey(CustomerAccountHstModel, on_delete=models.PROTECT,related_name='followup_customerhst_account')
    contact_type = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='followup_contacthst_type')
    disposition_code = models.ForeignKey(DispositionCodeMstModel, on_delete=models.PROTECT,related_name='followuphst_dispositioncode')
    person_contacted = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='followuphst_person_contacted')
    contacted_at = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='followuphst_contacted_at')
    contact_mode = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='followuphst_contact_mode')
    reminder_mode = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='followuphst_reminder_mode')
    contacted_by_unit = models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='followuphst_unit')
    class Meta:
        verbose_name = 'Customer Followup'
        verbose_name_plural = 'Customer Followups'  
        db_table = "customer_followup_hst"  

# class CaseHstModel(AppBaseModel):
#     case_no = models.CharField(max_length=30,null=True)
#     class Meta:
#         db_table = "case_hst"  

# class CaseCustomerHstModel(AppBaseModel):
#     caseid = models.ForeignKey(CaseHstModel, on_delete=models.PROTECT,related_name='customer_casehst_caseid')
#     customer = models.ForeignKey(CustomerHstModel, on_delete=models.PROTECT,related_name='customer_casehst_customer')
#     customer_account = models.ForeignKey(CustomerAccountHstModel, on_delete=models.PROTECT,related_name='customer_casehst_customer_account')  
#     from_unit_level =  models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='customer_casehst_from_unitlevel')            
#     to_unit_level =  models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='customer_casehst_to_unitlevel')  
#     from_unit =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='customer_casehst_from_unit')  
#     to_unit =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='customer_casehst_to_unit')  
#     allocated_to = models.ForeignKey(User, on_delete=models.PROTECT,related_name='customer_casehst_allocatedto')  
#     last_allocation_date =  models.DateTimeField(blank=True, null=True)   
#     class Meta:
#         db_table = "case_linked_hst"      

class CustomerPaymentsHstModel(CustomerPaymentBaseModel):
    customer = models.ForeignKey(CustomerHstModel, on_delete=models.PROTECT,related_name='customer_payments_hst_customer_id')
    customer_account = models.ForeignKey(CustomerAccountHstModel, on_delete=models.PROTECT,related_name='customer_payments_hst_customer_account_id')
    class Meta:
        db_table = "customer_payments_hst" 