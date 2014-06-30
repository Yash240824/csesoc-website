from django.db import models

GENDER_CHOICES = (
      ('M', 'Male'),
      ('F', 'Female'),
      )
    

PAYMENT_CHOICES = (
      ('N', 'Not Paid'),
      ('P', 'Paid')
      )

SHIRT_CHOICES = (
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    )

class Hoodie(models.Model):
   full_name = models.CharField(max_length=100)
   student_number = models.CharField(max_length=8)
   contact_number = models.CharField(max_length=15)
   email_address = models.EmailField(max_length=75)
   gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
   size = models.CharField(max_length=3, choices=SHIRT_CHOICES)
   payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default='N')
   

   def __unicode__(self):
      return self.full_name

