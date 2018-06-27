from django.db import models

# Create your models here.

class UserInfo (models.Model):

	#用户名称唯一
	userName  = models.CharField(max_length=50, unique=True)
	sex = models.CharField(max_length=20)
	cardId = models.CharField(max_length=50)
	def __str__(self):

		return self.username

class CommentInfo(models.Model):

	comment = models.CharField(max_length=255)


