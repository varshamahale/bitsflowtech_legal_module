from django.db import models
from django.contrib.auth.models import User
from .GenericMasterModel import MetadataParameterModel
from collapp.models.modelsBase.BaseModel import MasterBaseModel,AppBaseModel


class FileDownloadModel(MasterBaseModel):     
    download_datetime = models.DateTimeField(auto_now_add=True)
    download_type = models.ForeignKey(MetadataParameterModel, on_delete=models.PROTECT,related_name='download_download_type')
    path = models.CharField(max_length=1000)
