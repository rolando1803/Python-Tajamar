from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100) 
    age = models.IntegerField()
   

    def __str__(self): 
        return str(self.first_name) 

