from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class student(models.Model):
	Name=models.CharField(max_length=50)
	Roll_Number=models.IntegerField()
	Email=models.CharField(max_length=200)
	College=models.CharField(max_length=100)
	passedout_year=models.IntegerField()
	course_name=models.CharField(max_length=30)
	course_fee=models.IntegerField()
	Institute_area=models.CharField(max_length=100)
	Fieles=models.FileField(upload_to='profile/pdfs/',null=True)
	Image=models.ImageField(upload_to='profile/pic/',null=True,blank=True)
	

	def __str__(self):
		return f'{self.user.username} student'

class UserProfile(User):
	roles = [("s","studentsection"),("a","admin")]
	role = models.CharField(choices=roles, max_length=3)


class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	image=models.ImageField(default='default.jpg',upload_to='profile')

	def __str__(self):
		return f'{self.user.username} Profile'

def delete(self,*args, **kwargs):
	self.pdf.delete()
	self.cover.delete()
	super().delete(*args,**kwargs)



