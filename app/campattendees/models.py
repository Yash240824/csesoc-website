from django.db import models
from app import campglobals


class Application(models.Model):
   full_name = models.CharField(max_length=100)
   student_number = models.CharField(max_length=8)
   contact_number = models.CharField(max_length=15)
   gender = models.CharField(max_length=1, choices=campglobals.GENDER_CHOICES)
   arc = models.BooleanField(default=False)
   cse_program = models.CharField(max_length=2, choices=campglobals.PROGRAM_CHOICES, verbose_name='CSE program')

   age = models.DateField(verbose_name='Date of Birth', help_text='Proof of age will be required if you wish to consume alcohol.')
   dietary = models.TextField(help_text='Please list any special dietary requirements above.', blank=True)
   medical = models.TextField(help_text='Please list any medical conditions that should be disclosed above.', blank=True)

   payment_status = models.CharField(max_length=1, choices=campglobals.PAYMENT_CHOICES, default='N')
   medical_pdf = models.FileField(upload_to="storage/uploads", blank=True)
   year = models.IntegerField(verbose_name='Application Year', editable=True)
   shirt_size = models.CharField(max_length=3, choices=campglobals.SHIRT_CHOICES, default='N')

   def __unicode__(self):
      return self.full_name

