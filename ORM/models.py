from django.db import models
import uuid

class Salesforce(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name =  models.CharField(max_length=30,blank=True)
        Salesforce = models.CharField(max_length=30,blank=True)

        def __str__(self):
            return self.name

class Company(models.Model):
    Salesforce = models.ForeignKey(Salesforce,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,blank=True)
    role = models.CharField(max_length=40)
    is_developer = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} role -{self.role}'

        
