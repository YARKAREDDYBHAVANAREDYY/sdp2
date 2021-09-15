from django.db import models

class userreg(models.Model):
	Aadhar=models.IntegerField()
	Name=models.CharField(max_length=100,blank=False)
	password=models.CharField(max_length=100,blank=False)
	class Meta:
		db_table = "user_table"

# declare a new model with a name "GeeksModel"
