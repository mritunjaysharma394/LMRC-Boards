from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Topic(models.Model):
	subject = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board,on_delete = models.CASCADE, related_name = 'topics')
	starter = models.ForeignKey(User,on_delete = models.CASCADE, related_name ='topics')

class Post(models.Model): 	
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic,on_delete = models.CASCADE, related_name = 'posts')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	created_by = models.ForeignKey(User,on_delete = models.CASCADE, related_name='posts')
	updated_by = models.ForeignKey(User,on_delete = models.CASCADE, null=True, related_name='+')

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.description

    def delete(self,*args,**kwargs):
        self.document.delete()
        super().delete(*args,**kwargs)	