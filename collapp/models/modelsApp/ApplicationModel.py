from django.db import models
from django.contrib.auth.models import User
from collapp.models.modelsApp.GenericMasterModel import MetadataParameterModel,SourceHostMstModel,ProcessGroupModel,ProcessModel
from collapp.models.modelsApp.CustomerModel import CustomerTmpModel,CustomerModel,CustomerAccountModel
from collapp.models.modelsBase.BaseModel import MasterBaseModel,AppBaseModel
from collapp.models.modelsApp.BusinessMasterModel import DispositionCodeMstModel,UnitMstModel,UnitLevelMstModel,ReasonMstModel


class FileUploadModel(MasterBaseModel):
    PROCESSED = 1
    INIT = 0
    UNPROCESSED =-1
    STATUS_CHOISE =[(PROCESSED,'Processed'),(INIT,'Init'),(UNPROCESSED,'UnProcessed') ]      
    file_name =models.CharField(max_length=100)
    source_host = models.ForeignKey(SourceHostMstModel, on_delete=models.PROTECT,related_name='fileupload_source_host',verbose_name="File Source Host",default="")
    process_status =models.IntegerField(default=-1, choices=STATUS_CHOISE)  
    class Meta:
        db_table = "file_upload_dtl"


class UploadSourceTargetMapModel(MasterBaseModel): 
    FIELD_CHOISE =[(o, o.upper())  for o in CustomerTmpModel.__dict__.keys()]
    source_host = models.ForeignKey(SourceHostMstModel, on_delete=models.PROTECT,related_name='up_stm_source_host',verbose_name="File Source Host")
    source_col = models.CharField(max_length=200,verbose_name="Source Field Name")
    target_col = models.CharField(max_length=200,verbose_name="Target Field Name",default='#',choices=FIELD_CHOISE)
    class Meta:
        verbose_name = 'Upload File Field Mapping'
        verbose_name_plural = 'Upload File Field Mappings' 
        db_table = "upload_source_target_map_dtl"   

    def __str__(self):
        return self.source_col+" ("+self.source_host.host_name+")"   

class CaseModel(AppBaseModel):
    case_no = models.CharField(max_length=30,null=True,verbose_name="Case No")
    class Meta:
        db_table = "case_dtl"  

# Ganesh ->adding escalated_unit_level,escalated_unit, escalated_code & escalated_last_update - MOD: 16/06/2022
class CaseCustomerModel(AppBaseModel):

    # Abhishek Patel case_stage 05/07/2022
    #case stage =0 (telecaller), 1 (skip), 2 (escalated)
    #skip unit level, skip unit id

    #disposition code- Add Assigned unit level

    # ACTIVE = 1
    # INACTIVE =0
    TELECALLER=0
    SKIP=1
    ESCALATED=2
    NOTTRACEABLE=3

    # STATUS_CHOISE =[(ACTIVE,'Active'),(INACTIVE,'Inactive'),(NOTTRACEABLE,'NotTraceable') ] 
    # skip_trace_status=models.IntegerField(default=0, choices=STATUS_CHOISE) 

    STAGE_CHOISE =[(TELECALLER,'Telecaller'),(SKIP,'Skip'),(ESCALATED,'Escalated'),(NOTTRACEABLE,'NotTraceable') ] 
    case_stage=models.IntegerField(default=0, choices=STAGE_CHOISE) 
    
    skip_unit_level=models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='Skip_case_unitlevel',null=True)
    skip_unit =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='Skip_case_unit',null=True)

    #---------------------------END----------------------------------------------------------

    caseid = models.ForeignKey(CaseModel, on_delete=models.PROTECT,related_name='customer_case_caseid',verbose_name="Case Details")
    customer = models.ForeignKey(CustomerModel, on_delete=models.PROTECT,related_name='customer_case_customer')
    customer_account = models.ForeignKey(CustomerAccountModel, on_delete=models.PROTECT,related_name='customer_case_customer_account')  
    # applicant_type = models.ForeignKey(MetadataParameterModel, default=1, on_delete=models.PROTECT,related_name='customer_case_applicanttype',null=False)
    from_unit_level =  models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='customer_case_from_unitlevel',null=True)            
    to_unit_level =  models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='customer_case_to_unitlevel',null=True)  
    from_unit =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='customer_case_from_unit',null=True)  
    to_unit =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='customer_case_to_unit',null=True)  
    allocated_to = models.ForeignKey(User, on_delete=models.PROTECT,related_name='customer_case_allocatedto',null=True)  
    last_allocation_date =  models.DateTimeField(blank=True, null=True)   
    reason = models.ForeignKey(ReasonMstModel, on_delete=models.PROTECT,related_name='customer_case_reason',null=True)  
    remarks = models.CharField(max_length=200,verbose_name="Remarks",null=True)

# Ganesh >>>
    escalated_unit_level       =  models.ForeignKey(UnitLevelMstModel, on_delete=models.PROTECT,related_name='Escalated_case_unitlevel',null=True)
    escalated_unit             =  models.ForeignKey(UnitMstModel, on_delete=models.PROTECT,related_name='Escalated_case_unit',null=True)
    escalated_code             =  models.CharField(max_length=100,verbose_name="Escalated_code",null=True) 
    escalation_last_updtd_date =  models.DateTimeField(blank=True, null=True) 

    class Meta:
        db_table = "case_linked_dtl"      

class TaskModel(AppBaseModel): 
    DONE = 1
    INIT =0
    FAIL =-1
    STATUS_CHOISE =[(DONE,'Done'),(INIT,'Init'),(FAIL,'Fail') ]  
    # process_type = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='task_metadata_parameter')
    # reference_id = models.IntegerField(default="") 
    process_group = models.ForeignKey(ProcessGroupModel, on_delete=models.PROTECT,related_name='task_processgroup',blank=True,null=True)
    process_status = models.IntegerField(default=0, choices=STATUS_CHOISE) 
    force_completion=	models.IntegerField(default=0) 

    class Meta:
        db_table = "task_dtl"        

class TaskProcessModel(AppBaseModel): 
    DONE = 1
    INIT =0
    FAIL =-1
    STATUS_CHOISE =[(DONE,'Done'),(INIT,'Init'),(FAIL,'Fail') ]  
    task = models.ForeignKey(TaskModel, on_delete=models.PROTECT,related_name='taskprocess_task')
    process = models.ForeignKey(ProcessModel, on_delete=models.PROTECT,related_name='taskprocess_process',blank=True,null=True)
    process_name = models.CharField(max_length=100)
    process_status = models.IntegerField(default=0, choices=STATUS_CHOISE) 
    remarks = models.CharField(max_length=1000)
    class Meta:
        db_table = "task_process_dtl"      


class SearchApiModel(AppBaseModel):
    key  = models.TextField(max_length=50,default="",null=True)
    query = models.TextField(max_length=2000,default="",null=True)
    class Meta:
        db_table = "searchapi_parameter"      
     



