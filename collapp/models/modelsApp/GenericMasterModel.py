from django.db import models
from collapp.models.modelsBase.BaseModel import MasterBaseModel,AppBaseModel

# this to be used for Generic Masters in Collapp
class SourceHostMstModel(MasterBaseModel): 
    host_code = models.CharField(max_length=20)
    host_name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Source Host'
        verbose_name_plural = 'Source Hosts'          
        db_table = "source_host"
    def __str__(self):
        return self.host_name+" ("+self.host_code+")"         

class MetadataParameterModel(MasterBaseModel):
    metadata_name =models.CharField(max_length=100)
    metadata_type =models.CharField(max_length=20)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Metadata Parameter'
        verbose_name_plural = 'Metadata Parameters'   
        db_table = "metadata_parameter"

    def __str__(self):
        return self.metadata_name+" ("+self.metadata_type+")"        

class ProcessGroupModel(MasterBaseModel):
    process_group_code =models.CharField(max_length=50)
    process_group_type = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='process_processtype',verbose_name="Process Type")
    process_group_name =models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Process Group'
        verbose_name_plural = 'Process Groups'   
        db_table = "process_group_mst"

    def __str__(self):
        return self.process_group_name+" ("+self.process_group_type.metadata_name+")"  

class ProcessModel(MasterBaseModel):
    process_name =models.CharField(max_length=100)
    process_class =models.CharField(max_length=50)
    process_method =models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Process'
        verbose_name_plural = 'Processes'   
        db_table = "process_mst"

    def __str__(self):
        return self.process_name    


class ProcessGroupMapModel(MasterBaseModel):
    process_group = models.ForeignKey(ProcessGroupModel, on_delete=models.PROTECT,related_name='processgroupmap_processgroup',verbose_name="Process Group")
    process = models.ForeignKey(ProcessModel, on_delete=models.PROTECT,related_name='processgroupmap_process',verbose_name="Process")
    order_by = models.IntegerField(default=1, verbose_name="Order By")    

    class Meta:
        verbose_name = 'Process Group Process Map'
        verbose_name_plural = 'Process Group Process Map'   
        db_table = "process_group_process_map_mst"
 

# Abhishek patel:- Added new models (country,state)  16/06/2022
class Country(MasterBaseModel):
    country=models.CharField(max_length=50,null=True)
    
    class Meta:
        verbose_name = 'Country Master'   
        db_table = "country_mst"
        
    def __str__(self):
        return self.country

class State(MasterBaseModel):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)  
    state=models.CharField(max_length=50,null=True)

    class Meta:
        verbose_name = 'State Master'   
        db_table = "state_mst"
        
    def __str__(self):
        return self.state


# class TelecallerSrvMstModel(MasterBaseModel):
#     srv_query_name = models.CharField(max_length=50,verbose_name="Telecaller Srv Query Name")   
#     srv_query_desc = models.CharField(max_length=300,verbose_name="Telecaller Srv Query Desc")   
#     srv_query      = models.CharField(max_length=700,verbose_name="Telecaller Srv Query")   
#     class Meta:
#         verbose_name = 'Telecaller Srv Master'
#         verbose_name_plural = 'Telecaller Srv Masters' 
#         db_table = "telecaller_srv_mst"       
        
#     def __str__(self):
#         return self.srv_query_desc