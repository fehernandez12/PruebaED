from django.db import models
# Modelos de GeoDjango, necesarios para poder crear objetos de clase Point
from django.contrib.gis.db import models as geo_models

# Create your models here.
class Dataset(models.Model):
	name = models.CharField(max_length=95)
	date = models.DateTimeField(auto_now_add=True)

class Row(models.Model):
	dataset_id = models.ForeignKey(Dataset, on_delete=models.CASCADE)
	point = geo_models.PointField()
	client_id = models.IntegerField()
	client_name = models.CharField(max_length=45)