from django.db import models

class Todo(models.Model):
    pet = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    appointments = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)