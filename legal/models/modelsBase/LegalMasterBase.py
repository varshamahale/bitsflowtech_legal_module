from django.db import models
class LegalMstBaseModel(models.Model):
    
     LEGAL=0
     REPOSSESSION=1
     SETTLEMENT=2
     SKIP=3
     MARK_CHOICE =[(LEGAL,'Legal Procedings'),(REPOSSESSION,'Repossesion'),(SETTLEMENT,'Settlement'),(SKIP,'Skip (Later on)') ] 
     
     
     ACCOUNT_LEVEL=0
     CUSTOMER_LEVEL=1
     CASE_LEVEL=2
     LEVEL_CHOICE=[(ACCOUNT_LEVEL,'Account Level'),(CUSTOMER_LEVEL,'Customer level'),(CASE_LEVEL,'Case Lavel')]
     
     account_marking_code=       models.CharField(max_length=100,null=False,blank=False)
     account_marking_description=models.CharField(max_length=100,null=False,blank=False)
     mark_for=                   models.IntegerField(default=0, choices=MARK_CHOICE)
     marking_level=              models.IntegerField(default=0, choices=LEVEL_CHOICE)
     # effective_from=             models.DateField(null=False,blank=False)
     # effective_to=               models.DateField()
     # reason_code=                models.CharField(max_length=100,null=False,blank=False)
     # rule_code=                  models.CharField(max_length=100,null=False,blank=False)
     # rule_description=           models.CharField(max_length=500,null=False,blank=False)
     class Meta:
            abstract = True