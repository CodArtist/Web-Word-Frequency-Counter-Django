from django.db import connections,models

class Urls(models.Model):
    link=models.CharField(max_length=500)
  
