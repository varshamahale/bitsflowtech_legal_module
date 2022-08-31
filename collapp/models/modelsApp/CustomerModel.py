from django.db import models
from django.contrib.auth.models import User
from collapp.models.modelsApp.GenericMasterModel import MetadataParameterModel,SourceHostMstModel,Country,State
from collapp.models.modelsApp.BusinessMasterModel import DispositionCodeMstModel,UnitMstModel,UnitLevelMstModel,DocumentCategoryMstModel,DocumentMstModel,ProductMstModel
from collapp.models.modelsBase.BaseModel import AppBaseModel
from collapp.models.modelsBase.CustomerBaseModel import *

# customer details models

class CommonCustomerModel(AppBaseModel):
    common_customer_num = models.CharField(max_length=20,verbose_name="Common Customer No")
    class Meta:
        db_table = "common_customer_dtl"

class CustomerTmpModel(CustomerTmpBaseModel):
    source_host     = models.ForeignKey(SourceHostMstModel, on_delete=models.PROTECT,related_name='customertmp_source_host',null=True)
    ccn = models.ForeignKey(CommonCustomerModel, on_delete=models.PROTECT,related_name='customertmp_ccn',blank=True,null=True,verbose_name="Common Customer Details")
    class Meta:
        db_table = "customer_tmp"

class CustomerModel(CustomerBaseModel):
    ccn = models.ForeignKey(CommonCustomerModel, on_delete=models.PROTECT,related_name='customer_ccn',null=True,verbose_name="Common Customer Details")
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'   
        db_table = "customer_dtl"

class CustomerAccountModel(CustomerAccountBaseModel):
    customer = models.ForeignKey(CustomerModel, on_delete=models.PROTECT,related_name='Customer_account_customer_id',verbose_name="Customer Details")
    product  = models.ForeignKey(ProductMstModel, on_delete=models.PROTECT,related_name='Customer_account_product_id',verbose_name="Customer Product Details")
    
    class Meta:
        db_table = "customer_account_dtl"   

# class CustomerCreditCardModel(CustomerCreditCardBaseModel):
#     customer = models.ForeignKey(CustomerModel, on_delete=models.PROTECT,related_name='Customer_creditcard_customer_id',verbose_name="Customer Details")
#     customer_account = models.ForeignKey(CustomerAccountModel, on_delete=models.PROTECT,related_name='Customer_Address_customer_account',verbose_name="Account Details")    
#     class Meta:
#         db_table = "customer_card_dtl"           

# Abhishek patel:- added new fields (country,state) 16/06/2022
class CustomerAddressModel(CustomerAddressBaseModel):
    ACCOUNT='account'
    CUSTOMER='customer'
    level_choice=[(ACCOUNT,'account'),(CUSTOMER,'customer')]
    level=models.CharField(choices=level_choice,max_length=20,verbose_name="Level",null=True)
    customer= models.ForeignKey(CustomerModel, on_delete=models.PROTECT,related_name='Customer_Address_customer_id',verbose_name="Customer Details")
    customer_account = models.ForeignKey(CustomerAccountModel, on_delete=models.PROTECT,related_name='Customer_Address_customer_account',verbose_name="Account Details")
    #mailing adress / alt adress / office address / coapp address / employer / othe reference
    address_type = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='Customer_Address_metadata_address',verbose_name="Address Type")
    country=models.ForeignKey(Country, on_delete=models.PROTECT,related_name='additional_country',verbose_name="Country",null=True)
    state=models.ForeignKey(State, on_delete=models.PROTECT,related_name='additional_state',verbose_name="State",null=True)
    class Meta:
        db_table = "customer_address_dtl"      


# Ganesh - Added the cust_phone_type field in the "CustomerOtherPhonesModel"  model - Date of Submit - 16/06/2022

class CustomerOtherPhonesModel(CustomerOtherPhonesBaseModel):
    ACCOUNT='account'
    CUSTOMER='customer'
    level_choice=[(ACCOUNT,'account'),(CUSTOMER,'customer')]
    level=models.CharField(choices=level_choice,max_length=20,verbose_name="Level",null=True)

    cust_phone_type = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='Customer_Metadata_Phone_Type',verbose_name="Phone Type ")
    cust_contact_category = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='Customer_Metadata_Contact_Category',verbose_name="Contact Category")
    customer_account = models.ForeignKey(CustomerAccountModel, on_delete=models.PROTECT,related_name='Customer_other_Phones_customer_account',verbose_name="Account Details",null =True,blank =True)
    customer= models.ForeignKey(CustomerModel, on_delete=models.PROTECT,related_name='Customer_Other_Phones_customer_id',verbose_name="Customer Details",null=True)

    class Meta:
        db_table = "customer_other_phone_dtl"   


# class CustomerPhoneAdditionModel(CustomerPhoneAdditionBaseModel):

#     cust_account_no = models.ForeignKey(CustomerAccountModel, on_delete=models.PROTECT,related_name='Customer_Phones_Addition_account_no',verbose_name="Customer Account Number")
#     # customer_type = models.ForeignKey(CustomerModel, on_delete=models.PROTECT,null=False,blank=False,related_name='Customer_Phone_Addition_customer_type',verbose_name="Customer Type Phone Addition")
#     # customer_name = models.ForeignKey(CustomerModel, on_delete=models.PROTECT,related_name='Customer_Phone_Addition_customer_name',verbose_name="Customer Name Phone Addition")
#     cust_phone_type = models.ForeignKey(MetadataParameterModel,null=False,blank=False, on_delete=models.PROTECT,related_name='Customer_Metadata_Phone_Type',verbose_name="Phone Type Addition")
    
        
#     class Meta:
#         db_table = "customer_phone_addition_dtl"


######################################################  ENDS HERE ########################################################


class CustomerCollateralModel(CustomerCollateralBaseModel):
    customer = models.ForeignKey(CustomerModel, on_delete=models.PROTECT,related_name='customer_collateral_customer_id',verbose_name="Customer Details")
    customer_account = models.ForeignKey(CustomerAccountModel, on_delete=models.PROTECT,related_name='customer_collateral_customer_account',verbose_name="Account Details")
    class Meta:
        db_table = "customer_collateral_dtl"   

class CustomerPaymentsModel(CustomerPaymentBaseModel):
    customer = models.ForeignKey(CustomerModel, on_delete=models.PROTECT,related_name='customer_payments_customer_id',verbose_name="Customer Details")
    customer_account = models.ForeignKey(CustomerAccountModel, on_delete=models.PROTECT,related_name='customer_payments_customer_account',verbose_name="Account Details")
    class Meta:
        db_table = "customer_payments_dtl"          

# abhishek kumar 5/7/2022
class DocumentUpModel(AppBaseModel):
    customer_account = models.ForeignKey(CustomerAccountModel, on_delete=models.PROTECT,related_name='Document_customer_account',verbose_name="Account Details")
    document_name = models.ForeignKey(DocumentMstModel, on_delete=models.PROTECT,related_name='Document_document',verbose_name="Document",null=True)
    document_category = models.ForeignKey(DocumentCategoryMstModel, on_delete=models.PROTECT,related_name='Document_document_category',verbose_name="Document Category",null=True)
    doc_remarks = models.CharField(max_length=200,null=True,verbose_name="Document Remarks")
    file_path = models.CharField(max_length=200,null=True,verbose_name="file path")

    class Meta:
        verbose_name = 'Document Upload'
        verbose_name_plural = 'Document Upload'  
        db_table = "document_upload_dtl"
             

class FollowUpModel(FollowUpBaseModel):
    customer = models.ForeignKey(CustomerModel, on_delete=models.PROTECT,related_name='followup_customer_id',verbose_name="Customer Details")
    customer_account = models.ForeignKey(CustomerAccountModel, on_delete=models.PROTECT,related_name='followup_customer_account',verbose_name="Account Details")
    level  = models.CharField(max_length=20,null=True,verbose_name="Level")
    action_date = models.DateField(verbose_name="Action Date",null=True)
    disposition_code = models.ForeignKey(DispositionCodeMstModel, on_delete=models.PROTECT,related_name='followup_dispositioncode',verbose_name="Disposition Code")
    action_amount = models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True,verbose_name="Action Amount")
    person_contacted = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,null=True,related_name='followup_person_contacted',verbose_name="Person Contacted")
    contacted_at = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,null=True,related_name='followup_contacted_at',verbose_name="Contacte At")
    contact_mode = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,null=True,related_name='followup_contact_mode',verbose_name="Contact Mode")
    reminder_mode = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,null=True,related_name='followup_reminder_mode',verbose_name="Reminder Mode")
    contacted_by_unit = models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,null=True,related_name='followup_unit',verbose_name="Conteacted By Unit")
    contacted_by_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='%(class)s_contacted_by',verbose_name="Contacted By")
    next_action_date = models.DateField(verbose_name="Next Action Date",null=True,blank=True)
    next_action_time = models.CharField(max_length=100,null=True,verbose_name="Next Action Time")
    call_remarks = models.CharField(max_length=200,null=True,verbose_name="Call Remarks")

    #abhishek patel adding field for document 08/07/2022
    document = models.ForeignKey(DocumentUpModel, on_delete=models.PROTECT,related_name='followup_document',verbose_name="Document",null=True)

    # document = models.ForeignKey(DocumentMstModel, on_delete=models.PROTECT,related_name='followup_document',verbose_name="Document",null=True)
    # document_category = models.ForeignKey(DocumentCategoryMstModel, on_delete=models.PROTECT,related_name='followup_document_category',verbose_name="Document Category",null=True)
    # doc_remarks = models.CharField(max_length=200,null=True,verbose_name="Document Remarks")
    # file_path = models.CharField(max_length=200,null=True,verbose_name="file path")
    
    class Meta:
        verbose_name = 'Customer Followup'
        verbose_name_plural = 'Customer Followups'  
        db_table = "customer_followup_dtl"  


class CustomerDedupeIndexModel(AppBaseModel):
    ccn = models.ForeignKey(CommonCustomerModel, on_delete=models.PROTECT,related_name='customededupeindex_ccn',blank=True,null=True,verbose_name="Common Customer Details")
    common_customer_num = models.CharField(max_length=20,verbose_name="Common Customer No")
    customer_srno = models.CharField(max_length=100,null=True)
    customer_name = models.CharField(max_length=100,null=True)
    dob = models.CharField(max_length=30,null=True)
    pan_no = models.CharField(max_length=100,null=True)     
    loan_no = models.CharField(max_length=50,null=True)
    cust_pincode_primary = models.CharField(max_length=15,null=True)   

    class Meta:
        db_table = "customer_dedupe_index_dtl"
        indexes = [
                    models.Index(fields=['customer_srno',]),
                    models.Index(fields=['customer_name',]),
                    models.Index(fields=['dob',]),
                    models.Index(fields=['pan_no',]),
                    models.Index(fields=['loan_no',]),
                    models.Index(fields=['cust_pincode_primary',])
        ]         