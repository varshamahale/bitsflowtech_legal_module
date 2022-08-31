from django.db import models
from collapp.models.modelsBase.BaseModel import AppBaseModel
from collapp.models.modelsApp.ApplicationModel import FileUploadModel,TaskModel

# this to be used for day start process in Collapp
class DayStartProcessHdr(AppBaseModel): 
    YES = 1
    NO =0
    STATUS_CHOISE =[(YES,'Yes'),(NO,'No') ]   

    DONE = 1
    INIT =0
    FAIL =-1
    STATUS_CHOISE_2 =[(DONE,'Done'),(INIT,'Init'),(FAIL,'Fail') ]  

    start_business_date =       models.DateField()
    upload=		                models.IntegerField(default=0, choices=STATUS_CHOISE)  
    change_business_date=	    models.IntegerField(default=0, choices=STATUS_CHOISE) 
    bom_refresh=		            models.IntegerField(default=0, choices=STATUS_CHOISE) 
    force_completion=		            models.IntegerField(default=0, choices=STATUS_CHOISE) 
    cycle_refresh=		            models.IntegerField(default=0, choices=STATUS_CHOISE) 
    task = models.ForeignKey(TaskModel, on_delete=models.PROTECT,related_name='dayprocesshdr_task',null=True,default="")
    process_status = models.IntegerField(default=0, choices=STATUS_CHOISE_2) 
    
    class Meta:
        db_table = "daystart_process_hdr"

# class DayStartProcessDtl(AppBaseModel): 
#     DONE = 1
#     INIT =0
#     FAIL =-1
#     STATUS_CHOISE =[(DONE,'Done'),(INIT,'Init'),(FAIL,'Fail') ]       
#     daystart_hdr = models.ForeignKey(DayStartProcessHdr, on_delete=models.PROTECT,related_name='dayprocessdtl_hdr')
#     process     = models.CharField(max_length=100)
#     process_id  = models.IntegerField(default=0)
#     process_status = models.IntegerField(default=0, choices=STATUS_CHOISE) 
#     remarks		= models.CharField(max_length=1000)
#     class Meta:
#         db_table = "daystart_process_dtl"

class DayStartProcessFileDtl(AppBaseModel): 
    DONE = 1
    INIT =0
    FAIL =-1
    STATUS_CHOISE =[(DONE,'Done'),(INIT,'Init'),(FAIL,'Fail') ]       
    daystart_hdr = models.ForeignKey(DayStartProcessHdr, on_delete=models.PROTECT,related_name='dayprocessfiledtl_hdr')
    selected_files     = models.ForeignKey(FileUploadModel, on_delete=models.PROTECT,related_name='dayprocessfiledtl_file')
    file_status = models.IntegerField(default=0, choices=STATUS_CHOISE) 
    remarks		= models.CharField(max_length=1000)
    class Meta:
        db_table = "daystart_process_file_dtl"        

class DayStartProcessStatsDtl(AppBaseModel): 
    daystart_hdr = models.ForeignKey(DayStartProcessHdr, on_delete=models.PROTECT,related_name='dayprocessstatsdtl_hdr')
    process_type		=		models.CharField(max_length=30)
    stats_key			=	models.CharField(max_length=100)
    stats_value			=	models.CharField(max_length=20)
    class Meta:
        db_table = "daystart_process_stats_dtl"          