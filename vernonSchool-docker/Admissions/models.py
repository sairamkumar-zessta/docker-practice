from django.db import models
from django.db.models import signals
from django.dispatch import receiver 
from datetime import date 
# Create your models here.
class Student (models.Model):
    name = models.CharField(max_length=100) 
    father_name = models.CharField(max_length=100) 
    class_name = models.IntegerField()
    date_of_birth = models.DateField( null = True)
    age = models.IntegerField( blank = True , editable= False) 
    @property
    def age_add (self):
        today = date.today()
        self.age = today.year - self.date_of_birth.year - ((today.month, today.day) <(self.date_of_birth.month, self.date_of_birth.day))
    


@receiver(signals.pre_save, sender=Student) 
def add_age(sender , instance, **kwargs):
    instance.age_add 