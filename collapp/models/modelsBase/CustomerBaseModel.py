from django.db import models
from django.contrib.auth.models import User
from .BaseModel import AppBaseModel

# customer tmp tables to dump upload data

class CustomerTmpBaseModel(AppBaseModel):
    customer_srno = models.CharField(max_length=100,null=True)
    customer_name = models.CharField(max_length=100,null=True)
    dob = models.CharField(max_length=30,null=True)
    cust_type = models.CharField(max_length=100,null=True)
    pan_no = models.CharField(max_length=100,null=True)
    customer_segmentation = models.CharField(max_length=100,null=True) 
    service_segment = models.CharField(max_length=100,null=True) 
    common_customer_num = models.CharField(max_length=20,default="",null=True)
    duplicate_flag = models.IntegerField(null=True) # this field to handle file duplicate customer
    #customer loan data
    loan_no = models.CharField(max_length=50,null=True)
    loan_emi = models.DecimalField(max_digits=19, decimal_places=2,null=True)
    bounce_charges = models.DecimalField(max_digits=19, decimal_places=2,null=True)
    overdue_charges = models.DecimalField(max_digits=19, decimal_places=2,null=True)
    other_charges = models.DecimalField(max_digits=19, decimal_places=2,null=True)
    total_amount_due = models.DecimalField(max_digits=19, decimal_places=2,null=True)
    total_inst_os = models.DecimalField(max_digits=19, decimal_places=2,null=True)
    total_prin_os = models.DecimalField(max_digits=19, decimal_places=2,null=True)
    dpd = models.IntegerField(null=True)
    bucket = models.IntegerField(null=True)
    mode_repayment = models.CharField(max_length=100,null=True)
    branch_name = models.CharField(max_length=100,null=True)
    maturity_date = models.CharField(max_length=30,null=True)
    tenure = models.IntegerField(null=True)
    disbursal_date = models.CharField(max_length=30,null=True)
    last_due_date = models.CharField(max_length=30,null=True)
    promo_code = models.CharField(max_length=100,null=True)
    scheme = models.CharField(max_length=100,null=True) 
    product = models.CharField(max_length=100,null=True) # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< added the product falt field 
    bounce_reason = models.CharField(max_length=100,null=True) 
    bounce_date = models.CharField(max_length=30,null=True)
    last_contacted_on = models.CharField(max_length=100,null=True) 
    last_contacted_date = models.CharField(max_length=30,null=True)
    # customer card no details 
    card_no = models.CharField(max_length=100,null=True,verbose_name="Card No")
    cc_issue_by = models.CharField(max_length=100,null=True,verbose_name="issued By")        

    # customer collateral details
    collateral_no  = models.CharField(max_length=100,null=True,verbose_name="Collateral No")
    collateral_type = models.CharField(max_length=100,null=True,verbose_name="Collateral Type")
    collateral_sub_type = models.CharField(max_length=100,null=True,verbose_name="Collateral Sub Type")
    collateral_desc = models.CharField(max_length=100,null=True,verbose_name="Collateral Desc")
    reg_no = models.CharField(max_length=100,null=True,verbose_name="Registration No")
    make = models.CharField(max_length=100,null=True,verbose_name="Make")
    model = models.CharField(max_length=100,null=True,verbose_name="Model")
    engine_no = models.CharField(max_length=100,null=True,verbose_name="Engine No")
    chassis_no = models.CharField(max_length=100,null=True,verbose_name="Chasis No") 
    dealer_name = models.CharField(max_length=100,null=True,verbose_name="Dealer Name")
    dma_name = models.CharField(max_length=100,null=True,verbose_name="DMA Name")  
    # if collateral_type is property
    property_address =  models.CharField(max_length=100,null=True,verbose_name="Property Address")
    ownership =  models.CharField(max_length=100,null=True,verbose_name="Ownership")  
    builder  = models.CharField(max_length=100,null=True,verbose_name="Builder")  
    builder_project  = models.CharField(max_length=100,null=True,verbose_name="Builder Project")
    building  = models.CharField(max_length=100,null=True,verbose_name="Building")
    building_wing  = models.CharField(max_length=100,null=True,verbose_name="Building Wing")
    carpet_area = models.CharField(max_length=100,null=True,verbose_name="Carpet Area")
    full_area = models.CharField(max_length=100,null=True,verbose_name="Full Area")    

    # customer payment dtl 
    payment_mode = models.CharField(max_length=100,null=True,verbose_name="Payment Mode")
    payment_submode = models.CharField(max_length=100,null=True,verbose_name="Payment Sub Mode")
    payment_amount = models.DecimalField(max_digits=19, decimal_places=2,null=True,verbose_name="Payment Amount")
    payment_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Payment Date") 
    payment_refno = models.CharField(max_length=100,null=True,verbose_name="Payment Refno")
    payment_remarks = models.CharField(max_length=100,null=True,verbose_name="Payment Remarks")
    payment_deposit_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Payment Deposit Date") 
    payment_realization_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Payment Realize Date") 

    # customer employeer dtal
    employer_name = models.CharField(max_length=100,null=True)
    employer_type = models.CharField(max_length=100,null=True)
    emp_addr1 = models.CharField(max_length=100,null=True)
    emp_addr2 = models.CharField(max_length=100,null=True)
    emp_addr3 = models.CharField(max_length=100,null=True)
    emp_addr4 = models.CharField(max_length=100,null=True)
    emp_city = models.CharField(max_length=100,null=True) 
    emp_state = models.CharField(max_length=100,null=True)
    emp_country = models.CharField(max_length=100,null=True)       
    emp_pin = models.CharField(max_length=10,null=True)
    emp_phone1 = models.CharField(max_length=15,null=True)
    emp_phone2 = models.CharField(max_length=15,null=True)
    emp_mobile = models.CharField(max_length=15,null=True)

    # customer mailing / primary address
    cust_addr1_primary = models.CharField(max_length=100,null=True)
    cust_addr2_primary = models.CharField(max_length=100,null=True)
    cust_addr3_primary = models.CharField(max_length=100,null=True)
    cust_addr4_primary = models.CharField(max_length=100,null=True)
    cust_city_primary = models.CharField(max_length=100,null=True)
    cust_state_primary = models.CharField(max_length=100,null=True)
    cust_country_primary = models.CharField(max_length=100,null=True)
    cust_pincode_primary = models.CharField(max_length=15,null=True)
    cust_phone1_primary = models.CharField(max_length=15,null=True)
    cust_phone2_primary = models.CharField(max_length=15,null=True)
    cust_mobile_primary = models.CharField(max_length=15,null=True)

    #customer office address
    cust_addr1_office = models.CharField(max_length=100,null=True)
    cust_addr2_office = models.CharField(max_length=100,null=True)
    cust_addr3_office = models.CharField(max_length=100,null=True)
    cust_addr4_office = models.CharField(max_length=100,null=True)
    cust_city_office = models.CharField(max_length=100,null=True)
    cust_state_office = models.CharField(max_length=100,null=True)
    cust_country_office = models.CharField(max_length=100,null=True)    
    cust_pincode_office = models.CharField(max_length=15,null=True)
    cust_phone1_office = models.CharField(max_length=15,null=True)
    cust_phone2_office = models.CharField(max_length=15,null=True)
    cust_mobile_office = models.CharField(max_length=15,null=True)

    # customer coapplicant address
    cust_coapp_name = models.CharField(max_length=100,null=True)
    cust_addr1_coapp = models.CharField(max_length=100,null=True)
    cust_addr2_coapp = models.CharField(max_length=100,null=True)
    cust_addr3_coapp = models.CharField(max_length=100,null=True)
    cust_addr4_coapp = models.CharField(max_length=100,null=True)
    cust_city_coapp = models.CharField(max_length=100,null=True)
    cust_state_coapp = models.CharField(max_length=100,null=True)
    cust_country_coapp = models.CharField(max_length=100,null=True)        
    cust_pincode_coapp = models.CharField(max_length=15,null=True)
    cust_phone1_coapp = models.CharField(max_length=15,null=True)
    cust_phone2_coapp = models.CharField(max_length=15,null=True)
    cust_mobile_coapp = models.CharField(max_length=15,null=True)          

    # customer additional address
    cust_addr_alt1_ref = models.CharField(max_length=100,null=True)
    cust_addr1_alt1 = models.CharField(max_length=100,null=True)
    cust_addr2_alt1 = models.CharField(max_length=100,null=True)
    cust_addr3_alt1 = models.CharField(max_length=100,null=True)
    cust_addr4_alt1 = models.CharField(max_length=100,null=True)
    cust_city_alt1 = models.CharField(max_length=100,null=True)
    cust_state_alt1 = models.CharField(max_length=100,null=True)
    cust_country_alt1 = models.CharField(max_length=100,null=True)        
    cust_pincode_alt1 = models.CharField(max_length=15,null=True)
    cust_phone1_alt1 = models.CharField(max_length=15,null=True)
    cust_phone2_alt1 = models.CharField(max_length=15,null=True)
    cust_mobile_alt1 = models.CharField(max_length=15,null=True) 

    cust_addr_alt2_ref = models.CharField(max_length=100,null=True)
    cust_addr1_alt2 = models.CharField(max_length=100,null=True)
    cust_addr2_alt2 = models.CharField(max_length=100,null=True)
    cust_addr3_alt2 = models.CharField(max_length=100,null=True)
    cust_addr4_alt2 = models.CharField(max_length=100,null=True)
    cust_city_alt2 = models.CharField(max_length=100,null=True)
    cust_state_alt2 = models.CharField(max_length=100,null=True)
    cust_country_alt2 = models.CharField(max_length=100,null=True)        
    cust_pincode_alt2 = models.CharField(max_length=15,null=True)
    cust_phone1_alt2 = models.CharField(max_length=15,null=True)
    cust_phone2_alt2 = models.CharField(max_length=15,null=True)
    cust_mobile_alt2 = models.CharField(max_length=15,null=True)      

    cust_addr_alt3_ref = models.CharField(max_length=100,null=True)
    cust_addr1_alt3 = models.CharField(max_length=100,null=True)
    cust_addr2_alt3 = models.CharField(max_length=100,null=True)
    cust_addr3_alt3 = models.CharField(max_length=100,null=True)
    cust_addr4_alt3 = models.CharField(max_length=100,null=True)
    cust_city_alt3 = models.CharField(max_length=100,null=True)
    cust_state_alt3 = models.CharField(max_length=100,null=True)
    cust_country_alt3 = models.CharField(max_length=100,null=True)      
    cust_pincode_alt3 = models.CharField(max_length=15,null=True)
    cust_phone1_alt3 = models.CharField(max_length=15,null=True)
    cust_phone2_alt3 = models.CharField(max_length=15,null=True)
    cust_mobile_alt3 = models.CharField(max_length=15,null=True)   

    cust_addr_alt4_ref = models.CharField(max_length=100,null=True)
    cust_addr1_alt4 = models.CharField(max_length=100,null=True)
    cust_addr2_alt4 = models.CharField(max_length=100,null=True)
    cust_addr3_alt4 = models.CharField(max_length=100,null=True)
    cust_addr4_alt4 = models.CharField(max_length=100,null=True)
    cust_city_alt4 = models.CharField(max_length=100,null=True)
    cust_state_alt4 = models.CharField(max_length=100,null=True)
    cust_country_alt4 = models.CharField(max_length=100,null=True)      
    cust_pincode_alt4 = models.CharField(max_length=15,null=True)
    cust_phone1_alt4 = models.CharField(max_length=15,null=True)
    cust_phone2_alt4 = models.CharField(max_length=15,null=True)
    cust_mobile_alt4 = models.CharField(max_length=15,null=True)    

    cust_addr_alt5_ref = models.CharField(max_length=100,null=True)
    cust_addr1_alt5 = models.CharField(max_length=100,null=True)
    cust_addr2_alt5 = models.CharField(max_length=100,null=True)
    cust_addr3_alt5 = models.CharField(max_length=100,null=True)
    cust_addr4_alt5 = models.CharField(max_length=100,null=True)
    cust_city_alt5 = models.CharField(max_length=100,null=True)
    cust_state_alt5 = models.CharField(max_length=100,null=True)
    cust_country_alt5 = models.CharField(max_length=100,null=True)      
    cust_pincode_alt5 = models.CharField(max_length=15,null=True)
    cust_phone1_alt5 = models.CharField(max_length=15,null=True)
    cust_phone2_alt5 = models.CharField(max_length=15,null=True)
    cust_mobile_alt5 = models.CharField(max_length=15,null=True)          

    #customer additional phone reference 
    cust_phone_ref1 = models.CharField(max_length=100,null=True)
    cust_phone_1 = models.CharField(max_length=15,null=True)     
    cust_phone_ref2 = models.CharField(max_length=100,null=True)
    cust_phone_2 = models.CharField(max_length=15,null=True)   
    cust_phone_ref3 = models.CharField(max_length=100,null=True)
    cust_phone_3 = models.CharField(max_length=15,null=True)   
    cust_phone_ref4 = models.CharField(max_length=100,null=True)
    cust_phone_4 = models.CharField(max_length=15,null=True) 
    cust_phone_ref5 = models.CharField(max_length=100,null=True)
    cust_phone_5 = models.CharField(max_length=15,null=True)  
    
    class Meta:
        abstract = True


class CustomerBaseModel(AppBaseModel):
    customer_srno = models.CharField(max_length=100,null=True,verbose_name="CIF#")
    customer_name = models.CharField(max_length=100,null=True,verbose_name="Customer Name")
    dob = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="DOB")
    cust_type = models.CharField(max_length=100,null=True,verbose_name="Customer Type")
    pan_no = models.CharField(max_length=100,null=True,verbose_name="PAN")
    customer_segmentation = models.CharField(max_length=100,null=True,verbose_name="Segmentation") 
    service_segment = models.CharField(max_length=100,null=True,verbose_name="Service Segment") 

    class Meta: 
        abstract = True

class CustomerAccountBaseModel(AppBaseModel):
    loan_no = models.CharField(max_length=50,null=True,verbose_name="Account No")
    loan_emi = models.DecimalField(max_digits=19, decimal_places=2,null=True,verbose_name="EMI Amount")
    
    bounce_charges = models.DecimalField(max_digits=19, decimal_places=2,null=True,verbose_name="Bounce Charges")
    overdue_charges = models.DecimalField(max_digits=19, decimal_places=2,null=True,verbose_name="Overdue Charges")
    other_charges = models.DecimalField(max_digits=19, decimal_places=2,null=True,verbose_name="Other Charges")
    total_amount_due = models.DecimalField(max_digits=19, decimal_places=2,null=True,verbose_name="Total Due Amount")
    total_inst_os = models.DecimalField(max_digits=19, decimal_places=2,null=True,verbose_name="Total Int OS")
    total_prin_os = models.DecimalField(max_digits=19, decimal_places=2,null=True,verbose_name="Total Prin OS")
    dpd = models.IntegerField(null=True,verbose_name="DPD")
    bucket = models.IntegerField(null=True,verbose_name="Bucket")
    mode_repayment = models.CharField(max_length=100,null=True,verbose_name="Repayment Mode")
    branch_name = models.CharField(max_length=100,null=True,verbose_name="Branch Name")
    maturity_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Maturity Date")
    tenure = models.IntegerField(null=True,verbose_name="Tenure")
    disbursal_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Disbursal Date")
    last_due_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Last Due Date") 
    promo_code = models.CharField(max_length=100,null=True,verbose_name="Promo Code")
    scheme = models.CharField(max_length=100,null=True,verbose_name="Scheme") 
    bounce_reason = models.CharField(max_length=100,null=True,verbose_name="Bounce Reason") 
    bounce_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Bounce Date")
    card_no = models.CharField(max_length=100,null=True,verbose_name="Card No")
    cc_issue_by = models.CharField(max_length=100,null=True,verbose_name="issued By")     

    loan_amt = models.DecimalField(max_digits=19, decimal_places=2,null=True,verbose_name="Loan Amount")
    # deli  
    class Meta:
        abstract = True

# class CustomerCreditCardBaseModel(AppBaseModel):
#     card_no = models.CharField(max_length=100,null=True,verbose_name="Card No")
#     cc_issue_by = models.CharField(max_length=100,null=True,verbose_name="issued By")   
    # class Meta:
    #     abstract = True   
 
# Abhishek patel:- added new field (cust_landmark) 16/06/2022
class CustomerAddressBaseModel(AppBaseModel):
    #mailing adress / alt adress / office address / coapp address / employer / othe reference 
    # cust_address_reftype = models.CharField(max_length=30,null=True)
    cust_ref_name = models.CharField(max_length=100,null=True,verbose_name="Reference Name")
    cust_addr1 = models.CharField(max_length=100,null=True,verbose_name="Address Line 1")
    cust_addr2 = models.CharField(max_length=100,null=True,verbose_name="Address Line 2")
    cust_addr3 = models.CharField(max_length=100,null=True,verbose_name="Address Line 3")
    cust_addr4 = models.CharField(max_length=100,null=True,verbose_name="Address Line 4")
    cust_city = models.CharField(max_length=100,null=True,verbose_name="City")
    cust_pincode = models.CharField(max_length=15,null=True,verbose_name="Pincode")
    #TODO phone1, phone2, should be in phone model SUMIT SIR
    cust_phone1 = models.CharField(max_length=15,null=True,verbose_name="Phone No 1")
    cust_phone2 = models.CharField(max_length=15,null=True,verbose_name="Phone No 2")
    cust_mobile = models.CharField(max_length=15,null=True,verbose_name="Mobile No")
    cust_landmark = models.CharField(max_length=100,null=True,verbose_name="Landmark")
    class Meta:
        abstract = True       

# Ganesh - Added the cust_contact_category, cust_email_address field in the "CustomerOtherPhonesBaseModel"  model - Date of Submit - 16/06/2022

class CustomerOtherPhonesBaseModel(AppBaseModel):

    customer_name =  models.CharField(max_length=100,null=True,verbose_name="Customer Name")
    cust_phone_ref = models.CharField(max_length=100,null=True,verbose_name="Reference Name")
    cust_phone = models.CharField(max_length=15,null=True,verbose_name="Contact No")    
    cust_email_address  = models.CharField(max_length=100,null=True,verbose_name="Email Id")
  
    class Meta:
        abstract = True

# class CustomerPhoneAdditionBaseModel(AppBaseModel):
    
#     # marking_level = models.CharField(max_length=100,null=False,blank=False,verbose_name="Marking Level")
#     cust_mobile_no = models.CharField(max_length=15,null=False,blank=False,verbose_name="Mobile")
#     cust_contact_category = models.CharField(max_length=100,null=False,blank=False,verbose_name="Contact Category")
#     cust_email_address  = models.CharField(max_length=100,null=False,blank=False,verbose_name="")
  
#     class Meta:
#         abstract = True



########################################## ENDS HERE ########################################


class CustomerCollateralBaseModel(AppBaseModel):
    collateral_no  = models.CharField(max_length=100,null=True,verbose_name="Collateral No")
    collateral_type = models.CharField(max_length=100,null=True,verbose_name="Collateral Type")
    collateral_sub_type = models.CharField(max_length=100,null=True,verbose_name="Collateral Sub Type")
    collateral_desc = models.CharField(max_length=100,null=True,verbose_name="Collateral Desc")
    reg_no = models.CharField(max_length=100,null=True,verbose_name="Registration No")
    make = models.CharField(max_length=100,null=True,verbose_name="Make")
    model = models.CharField(max_length=100,null=True,verbose_name="Model")
    engine_no = models.CharField(max_length=100,null=True,verbose_name="Engine No")
    chassis_no = models.CharField(max_length=100,null=True,verbose_name="Chasis No") 
    dealer_name = models.CharField(max_length=100,null=True,verbose_name="Dealer Name")
    dma_name = models.CharField(max_length=100,null=True,verbose_name="DMA Name")  
    # if collateral_type is property
    property_address =  models.CharField(max_length=100,null=True,verbose_name="Property Address")
    ownership =  models.CharField(max_length=100,null=True,verbose_name="Ownership")  
    builder  = models.CharField(max_length=100,null=True,verbose_name="Builder")  
    builder_project  = models.CharField(max_length=100,null=True,verbose_name="Builder Project")
    building  = models.CharField(max_length=100,null=True,verbose_name="Building")
    building_wing  = models.CharField(max_length=100,null=True,verbose_name="Building Wing")
    carpet_area = models.CharField(max_length=100,null=True,verbose_name="Carpet Area")
    full_area = models.CharField(max_length=100,null=True,verbose_name="Full Area")
    class Meta:
        abstract = True   

class CustomerPaymentBaseModel(AppBaseModel):   
    payment_mode = models.CharField(max_length=100,null=True,verbose_name="Payment Mode")
    payment_submode = models.CharField(max_length=100,null=True,verbose_name="Payment Sub Mode")
    payment_amount = models.DecimalField(max_digits=19, decimal_places=2,null=True,verbose_name="Payment Amount")
    payment_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Payment Date") 
    payment_refno = models.CharField(max_length=100,null=True,verbose_name="Payment Refno")
    payment_remarks = models.CharField(max_length=100,null=True,verbose_name="Payment Remarks")
    payment_deposit_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Payment Deposit Date") 
    payment_realization_date = models.DateField(auto_now=False, auto_now_add=False,null=True,verbose_name="Payment Realize Date") 
    class Meta:
        abstract = True

class FollowUpBaseModel(AppBaseModel):
    account_no = models.CharField(max_length=50,null=True,verbose_name="Account No")
    class Meta:
        abstract = True




