from django.db import models
from vegeta.models import VegetaMstModel

# Create your models here.
class XicorMstModel(models.Model):
  title = models.CharField( max_length=50)
  content = models.CharField( max_length=50)
  app_name = models.CharField(max_length=50)

  class Meta:
    db_table = "xicor_mst"

class GokuMstModel(models.Model):
  title = models.CharField( max_length=50)
  frnd_vegeta = models.ForeignKey(VegetaMstModel,on_delete=models.PROTECT,verbose_name='Vegeta mst model')

  class Meta:
    db_table = "goku_mst"
 