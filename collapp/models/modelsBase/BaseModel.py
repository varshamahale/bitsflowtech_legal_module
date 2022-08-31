from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Base(models.Model):
    ACTIVE = 1
    INACTIVE =0
    STATUS_CHOISE =[(ACTIVE,'Active'),(INACTIVE,'Inactive') ]   
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default=1, choices=STATUS_CHOISE)  
    class Meta:
        abstract = True

class MasterBase(Base):
    created_by=  models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_createdBy',blank=True, null=True)
    created_date= models.DateTimeField(default=timezone.now)
    updated_by=  models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='%(class)s_updatedBy')
    updated_date= models.DateTimeField(blank=True, null=True)
    class Meta:
        abstract = True

class AppBase(Base):
    created_by=  models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_createdBy')
    created_date= models.DateTimeField(default=timezone.now)
    updated_by=  models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='%(class)s_updatedBy')
    updated_date= models.DateTimeField(blank=True, null=True)    
    class Meta:
        abstract = True

class Tenant(MasterBase):
    DONE = 1
    INIT =0
    FAIL =-1
    STATUS_CHOISE =[(DONE,'Done'),(INIT,'Init'),(FAIL,'Fail') ]       
    name = models.CharField(max_length=100)
    subdomain = models.CharField(max_length=100, unique=True)
    business_date = models.DateField(blank=False, null=False,default=datetime.date.today)
    daystart_status = models.IntegerField(default=1, choices=STATUS_CHOISE)  
    last_bom_refresh_date = models.DateField(blank=True, null=True)
    last_cycle_refresh_date = models.DateField(blank=True, null=True)
    class Meta:
        db_table = "tenant"

# this to be used for Masters in Collapp
class MasterBaseModel(MasterBase): 
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    class Meta:
        abstract = True

# Use this model where allocation happen like for application or customer classes
class AppBaseModel(AppBase): 
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    class Meta:
        abstract = True

class UserTenantModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    class Meta:
        db_table = "auth_user_tenant"