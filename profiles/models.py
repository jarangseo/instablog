from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	_genders = (
		('M', 'Male',),
		('F', 'Female',),
	)
	# kind = models.CharField( max_length=40 )
	# value = models.CharField( max_length=200 )
	gender = models.CharField(max_length=1, choices=_genders)
