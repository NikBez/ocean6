from django.db import models

class Students(models.Model):
    name = models.CharField(max_length =50)
    surname = models.CharField(max_length =50)
    age = models.IntegerField()
    dateOfBirth = models.DateField()

    def __str__(self):
        return (f"{self.name} {self.surname} ({self.age} years)")
    
