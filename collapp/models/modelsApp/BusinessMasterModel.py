from pyexpat import model
from turtle import back
from django.db import models
from collapp.models.modelsBase.BaseModel import MasterBaseModel
from collapp.models.modelsApp.GenericMasterModel import MetadataParameterModel, SourceHostMstModel
from django.contrib.auth.models import User
# from collapp.models.modelsApp.CustomerModel import *
# # abhishek import
# from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator
# this to be used for Business Masters in Collapp
class CaseMstModel(MasterBaseModel): 
    YES = 1
    NO =0
    STATUS_CHOISE =[(YES,'Yes'),(NO,'No') ]   
    customer_centricity=		models.IntegerField(default=0, choices=STATUS_CHOISE)  
    club_deliquent=				models.IntegerField(default=1, choices=STATUS_CHOISE)   
    club_unstamped=				models.IntegerField(default=1, choices=STATUS_CHOISE)  
    club_deal_account=			models.IntegerField(default=1, choices=STATUS_CHOISE)  
    club_group_account=			models.IntegerField(default=1, choices=STATUS_CHOISE)  
    class Meta:
        verbose_name = 'Case Master'
        verbose_name_plural = 'Case Masters'          
        db_table = "case_mst"
       

class SegmentMstModel(MasterBaseModel): 
    YES = 1
    NO =0
    STATUS_CHOISE =[(YES,'Yes'),(NO,'No') ]   
    queue_code=					models.CharField(max_length=20)
    queue_desc=					models.CharField(max_length=300)
    priority=					models.IntegerField(default=0)
    rule=						models.CharField(max_length=300)
    valid_form=					models.DateField()
    valid_till=					models.DateField()    
    exceptional=		        models.IntegerField(default=0, choices=STATUS_CHOISE)  

    class Meta:
        verbose_name = 'Segment Master'
        verbose_name_plural = 'Segment Masters'         
        db_table = "segment_mst"

    def __str__(self):
        return self.queue_desc+" ("+self.queue_code+")"          
 
class UnitLevelMstModel(MasterBaseModel): 
    level_no    =		        models.IntegerField(default=0,blank=False, null=False,unique=True,validators=[MinValueValidator(1)])  
    level_desc  =				models.CharField(max_length=300)   
    class Meta:
        verbose_name = 'Unit Level'
        verbose_name_plural = 'Unit Levels'          
        db_table = "unit_level_mst" 

    def __str__(self):
        return self.level_desc+" ( Level - "+str(self.level_no)+")"            

#Abhishek Pate Creating Role master model 11/07/2022
class RoleMstModel(MasterBaseModel): 
    role_code  = models.CharField(max_length=20)
    role_desc  = models.CharField(max_length=300)   
    class Meta:
        verbose_name = 'Role Master'
        verbose_name_plural = 'Role Masters'           
        db_table = "role_mst" 

    def __str__(self):
        return self.role_desc+" ("+self.role_code+")"

class UnitMstModel(MasterBaseModel): 
    unit_code  = models.CharField(max_length=20)
    unit_desc  = models.CharField(max_length=300)   
    unit_level = models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='unitmst_unit_level',verbose_name="Unit Level")
    reporting_unit = models.ForeignKey('self', on_delete=models.PROTECT,related_name='unitmst_rep_unit',verbose_name="Reporting Unit",null=True,blank=True)
    max_no_case  =  models.IntegerField(null=True)  
    total_amt_cap  = models.DecimalField(max_digits=19, decimal_places=2,null=True)

#Abhishek Patel added roles field 11/07/2022
    roles=models.ManyToManyField(RoleMstModel,related_name='Roles', blank=True)

    class Meta:
        verbose_name = 'Unit Master'
        verbose_name_plural = 'Unit Masters'           
        db_table = "unit_mst" 

    def __str__(self):
        return self.unit_desc+" ("+self.unit_code+")"              

class UnitUserMapMstModel(MasterBaseModel): 
    unit_level = models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,
                                   related_name='unitusrmap_unit_level', verbose_name="Unit Level")
    # abhishek kumar 6/16/2022 : chained foreignkey                                 
    # unit = ChainedForeignKey(UnitMstModel,
    #         chained_field="unit_level",
    #         chained_model_field="unit_level",
    #         show_all=False, auto_choose=True)
    unit = models.ForeignKey(UnitMstModel, on_delete=models.CASCADE,related_name='unitusrmap_unit_unit',verbose_name="Unit")
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='unitusrmap_manager_manager',verbose_name="User")
    class Meta:
        verbose_name = 'Unit User Map'
        verbose_name_plural = 'Unit User Map'         
        db_table = "unit_user_map_mst" 

    def __str__(self):
        return self.unit.unit_desc+" ("+self.user.first_name+" "+self.user.last_name+")"   

def get_rule_entity_fields():
    col_list = [ ("customer_dtl.customer_name" , "CUSTOMER_NAME"),("customer_dtl.dob" , "DOB"),("customer_dtl.cust_type","CUST_TYPE"),("customer_dtl.customer_segmentation","CUSTOMER_SEGMENTATION"),("customer_dtl.service_segment","SERVICE_SEGMENT"),
("customer_account_dtl.loan_emi","LOAN_EMI"),("ccustomer_account_dtl.bounce_charges","BOUNCE_CHARGES"),("customer_account_dtl.overdue_charges","OVERDUE_CHARGES"),("customer_account_dtl.other_charges","OTHER_CHARGES"),("customer_account_dtl.total_amount_due","TOTAL_AMOUNT_DUE"),("customer_account_dtl.total_inst_os","TOTAL_INST_OS"),("customer_account_dtl.total_prin_os","TOTAL_PRIN_OS"),("customer_account_dtl.dpd","DPD"),("customer_account_dtl.bucket","BUCKET"),("customer_account_dtl.mode_repayment","MODE_REPAYMENT"),("customer_account_dtl.branch_name","BRANCH_NAME"),("customer_account_dtl.maturity_date","MATURITY_DATE"),("customer_account_dtl.tenure","TENURE"),("customer_account_dtl.scheme","SCHEME"),
("customer_address_dtl.cust_pincode","CUST_MAILING_PINCODE")]
    return col_list

class RuleEntityModel(MasterBaseModel): 
    FIELD_CHOISE = get_rule_entity_fields()
    variable_name = models.CharField(max_length=50,verbose_name="Variable Name")   
    target_col = models.CharField(max_length=200,verbose_name="Target Field Name",default='#',choices=FIELD_CHOISE)
    class Meta:
        verbose_name = 'Rule Entity'
        verbose_name_plural = 'Rule Entities' 
        db_table = "rule_entity"    

class RuleMstModel(MasterBaseModel):
    rule_name = models.CharField(max_length=50,verbose_name="Rule Name")   
    rule_desc = models.CharField(max_length=300,verbose_name="Rule Desc")   
    rule = models.CharField(max_length=300,verbose_name="Rule")   
    class Meta:
        verbose_name = 'Rule Master'
        verbose_name_plural = 'Rule Masters' 
        db_table = "rule_mst"       
        
    def __str__(self):
        return self.rule_desc                  

class AllocationMstModel(MasterBaseModel): 
    segment = models.ForeignKey(SegmentMstModel, on_delete=models.PROTECT,related_name='allocmst_segment',verbose_name="Queue Code")
    valid_from = models.DateField()
    valid_till = models.DateField(null=True,blank=True)
    from_unit_level = models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='allocmst_from_unit_level',verbose_name="From Unit Level")
    to_unit_level = models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='allocmst_to_unit_level',verbose_name="To Unit Level")
    from_unit = models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='allocmst_from_unit',verbose_name="From Unit")
    to_unit = models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='allocmst_to_unit',verbose_name="To Unit")
    rule = models.ForeignKey(RuleMstModel, on_delete=models.PROTECT,related_name='allocmst_rulemst',verbose_name="Rule",null=True,blank=True)
    alloc_per = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    priority = models.IntegerField()  
    class Meta:
        verbose_name = 'Allocation Master'
        verbose_name_plural = 'Allocation Masters'              
        db_table = "allocation_mst"        
          
# Ganesh - mapped the rule field with the RuleMstModel - MOD: 16/06/2022 
class EscalationMstModel(MasterBaseModel): 
    code        = models.CharField(max_length=20)
    desc        = models.CharField(max_length=300)
    unit_level  = models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='escalmst_unit_level',verbose_name="Unit Level")
    unit        = models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='escalmst_from_unit',verbose_name="Unit")
    valid_from	= models.DateField()
    valid_till	= models.DateField()
    rule		= models.ForeignKey(RuleMstModel, on_delete=models.PROTECT,related_name='escalmst_rulemst',verbose_name="Rule",null=True,blank=True)   

    class Meta:
        verbose_name = 'Escalation Master'
        verbose_name_plural = 'Escalation Masters'                  
        db_table = "escalation_mst"  

#############################################################################      

class ProductMstModel(MasterBaseModel): 
    BOM = 'B'
    CYCLE ='C'
    REFRESH_CHOISE =[(BOM,'BOM'),(CYCLE,'CYCLE') ]      

    code        = models.CharField(max_length=20,verbose_name="Product Code")
    desc        = models.CharField(max_length=300,verbose_name="Product Desc")
    refresh_type = models.CharField(default='B', choices=REFRESH_CHOISE,max_length=1,verbose_name="Refresh Type")  
    class Meta:
        verbose_name = 'Product Master'
        verbose_name_plural = 'Product Masters'          
        db_table = "product_mst"  

    def __str__(self):
        return self.desc+' ( '+self.code+' ) '    

class ProductMapMstModel(MasterBaseModel):       
    product =  models.ForeignKey(ProductMstModel, on_delete=models.PROTECT,related_name='productmap_product',verbose_name="Product",default="",null=True)
    source_host = models.ForeignKey(SourceHostMstModel, on_delete=models.PROTECT,related_name='productmap_source_host',verbose_name="File Source Host",default="")
    source_product =models.CharField(max_length=50,verbose_name="Source Product")

    class Meta:
        verbose_name = 'Product Map Master'
        verbose_name_plural = 'Product Map Masters'          
        db_table = "product_map_mst"          

class DispositionCodeMstModel(MasterBaseModel): 
    YES = 1
    NO =0
    STATUS_CHOISE =[(YES,'Yes'),(NO,'No') ]

#Abhishek patel creating level field 21/07/2022
    ACCOUNT='account'
    CUSTOMER='customer'
    level_choice=[(ACCOUNT,'account'),(CUSTOMER,'customer')]
    level=models.CharField(choices=level_choice,max_length=20,verbose_name="Level",null=True)
#--------------end---------------------------------------------------------------

    product     =       models.ForeignKey(ProductMstModel, on_delete=models.PROTECT,related_name='disposition_product',verbose_name="Product Category",null=True)
    code        = models.CharField(max_length=20,verbose_name="Disposition Code")
    desc        = models.CharField(max_length=300,verbose_name="Description")
    # customer_level=		            models.IntegerField(default=0, choices=STATUS_CHOISE,verbose_name="Customer Level")  
    # account_level=		            models.IntegerField(default=0, choices=STATUS_CHOISE,verbose_name="Account Level")  
    consider_contact=		        models.IntegerField(default=0, choices=STATUS_CHOISE,verbose_name="Consider Contact")  
    next_action_date=		        models.IntegerField(default=0, choices=STATUS_CHOISE,verbose_name="Make Next Action Date Mandatory")  
    restrict_next_action_date=		models.IntegerField(default=0, choices=STATUS_CHOISE,verbose_name="Restrict Next Action Date Till Default Date")  
    document_upload=		        models.IntegerField(default=0, choices=STATUS_CHOISE,verbose_name="Is Document Upload Mandatory")  
    next_action_time=		        models.IntegerField(default=0, choices=STATUS_CHOISE,verbose_name="Make Next Action Time Mandatory")  
    action_amount=		            models.IntegerField(default=0, choices=STATUS_CHOISE,verbose_name="Make Action Amount Mandatory")  
    remarks=		                models.IntegerField(default=0, choices=STATUS_CHOISE,verbose_name="Make Remarks Mandatory")  
    roles=                          models.CharField(max_length=300,verbose_name="Roles",null=True,blank=True)    

    #Abhishek patel added new field assigned_unit to get default unit for skip trace 07/07/2022
    assigned_unit_level=models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='assigned_unit_level',null=True)
#----------------------------------------------End--------------------------------------------------------
    class Meta:
        verbose_name = 'Disposition Code Master'
        verbose_name_plural = 'Disposition Code Masters'           
        db_table = "disposition_code_mst"   

    def __str__(self):
        return self.desc+' ( '+self.code+' ) '                    

class DocumentCategoryMstModel(MasterBaseModel): 
    code        = models.CharField(max_length=20)
    desc        = models.CharField(max_length=300)
    class Meta:
        verbose_name = 'Document Category'
        verbose_name_plural = 'Document Categories'            
        db_table = "document_category_mst"     

class DocumentMstModel(MasterBaseModel): 
    code        = models.CharField(max_length=20)
    desc        = models.CharField(max_length=300)
    document_category = models.ForeignKey(DocumentCategoryMstModel, on_delete=models.PROTECT,related_name='doc_doc_category',verbose_name="Document Category")
    class Meta:
        verbose_name = 'Document Master'
        verbose_name_plural = 'Document Masters'          
        db_table = "document_mst"             

    

class ReasonMstModel(MasterBaseModel):       
    reasonType =  models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='reasonmst_reasontype',verbose_name="Reason Type")
    reason_code = models.CharField(max_length=50,verbose_name="Reason Code")
    reason_desc =models.CharField(max_length=200,verbose_name="Reason Desc")

    class Meta:
        verbose_name = 'Reason Master'
        verbose_name_plural = 'Reason Masters'          
        db_table = "reason_mst"             

class DedupeMstModel(MasterBaseModel): 
    valid_from = models.DateField()
    valid_till = models.DateField(null=True,blank=True)
    rule_name = models.CharField(max_length=50,verbose_name="Rule Name",default="")
    min_match_percentage= models.DecimalField(max_digits=5, decimal_places=2,verbose_name="Minimum match percentage",null=True)
    class Meta:
        verbose_name = 'Dedupe Master'
        verbose_name_plural = 'Dedupe Masters'              
        db_table = "dedupe_mst"        

class DedupeParameterMstModel(MasterBaseModel): 
    dedupe = models.ForeignKey(DedupeMstModel, on_delete=models.PROTECT,related_name='dedupeparametermst_dedupe',verbose_name="Dedupe Master")
    parameter_rule = models.CharField(max_length=100,verbose_name="Rule Name",default="")
    priority = models.IntegerField()  
    class Meta:
        verbose_name = 'Dedupe Parameter Master'
        verbose_name_plural = 'Dedupe Parameter Masters'        
        db_table = "dedupe_parameter_mst"         

    def __str__(self):
        return str(self.id)