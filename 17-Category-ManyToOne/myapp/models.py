from django.db import models

# Create your models here.
class Category(models.Model): # < here
  title = models.CharField(max_length=255, default='')
  def __str__(self):
    return self.title

class Flower(models.Model):
  title = models.CharField(max_length=255, default='')
  description = models.TextField(default='') 
  category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)

  def __str__(self):
    return self.title