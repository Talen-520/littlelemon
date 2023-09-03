from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   time = models.DateTimeField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name
   def date_now(self):
      return self.time.strftime('%d/%m/%Y %H:%M:%S')


# Add code to create Menu model

class Menu(models.Model):
   name = models.CharField(max_length=200)
   price = models.IntegerField()
   def __str__(self):
       return self.name