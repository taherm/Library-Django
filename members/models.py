from django.db import models

class Members(models.Model):
	mem_id = models.IntegerField(max_length=7,primary_key=True)
	mem_name = models.CharField(max_length=50)
	mem_addr = models.CharField(max_length=70)
	mem_reg = models.DateField()
	mem_exp = models.DateField()

	def __str__(self):
		return self.mem_name



# Create your models here.
