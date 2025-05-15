from django.db import models

# Create your models here.
class websites(models.Model):
    url=models.CharField(max_length=100);

class comments(models.Model):
    url=models.CharField(max_length=100);
    user=models.CharField(max_length=100);
    comment=models.CharField(max_length=1000);
    rating=models.FloatField(max_length=1000);
    sentiment=models.CharField(max_length=100);
    

class webres(models.Model):
    url=models.CharField(max_length=1000);
    num=models.FloatField(max_length=100);
    pos=models.FloatField(max_length=100);
    neg=models.FloatField(max_length=100);
    neu=models.FloatField(max_length=100);


class user(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	zip=models.CharField(max_length=100);
	gender=models.CharField(max_length=100);


class feedback(models.Model):
	name=models.CharField(max_length=100);
	feedback=models.CharField(max_length=100);
	


class accuracy(models.Model):
	algo=models.CharField(max_length=100);
	accuracyv=models.FloatField(max_length=1000)	
	