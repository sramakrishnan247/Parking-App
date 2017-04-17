from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Place(models.Model):
    Name = models.CharField(max_length=30)	
    Vacant = models.IntegerField()
    # pid = models.ForeignKey('LandOwner',on_delete=models.CASCADE,)
    def __str__(self):
    	return str(self.Name)

class CarOwner(models.Model):
	Username = models.CharField(max_length=40)
	# Name = models.CharField(max_length=40)
	# Address = models.CharField(max_length=100)
	# cno = models.IntegerField(primary_key=True)
	Mobile = models.IntegerField()
	def __str__(self):
		return str(self.Username)

class Security(models.Model):
	sid = models.OneToOneField('Place',on_delete=models.CASCADE,)
	# Username = models.CharField(max_length=40)
	def __str__(self):
		return str(self.sid)			

class LandOwner(models.Model):
	Name = models.CharField(max_length=30)
	Slots = models.IntegerField()

	def __str__(self):
		return str(self.Name)		