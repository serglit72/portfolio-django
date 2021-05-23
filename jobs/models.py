from django.db import models

class Job(models.Model):
    immage = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)