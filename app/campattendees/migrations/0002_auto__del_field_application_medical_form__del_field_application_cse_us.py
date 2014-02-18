# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Application.medical_form'
        db.delete_column('campattendees_application', 'medical_form')

        # Deleting field 'Application.cse_username'
        db.delete_column('campattendees_application', 'cse_username')


    def backwards(self, orm):
        # Adding field 'Application.medical_form'
        db.add_column('campattendees_application', 'medical_form',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Application.cse_username'
        db.add_column('campattendees_application', 'cse_username',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 2, 19, 0, 0), max_length=15),
                      keep_default=False)


    models = {
        'campattendees.application': {
            'Meta': {'object_name': 'Application'},
            'age': ('django.db.models.fields.DateField', [], {}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'cse_program': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'dietary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medical': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'medical_pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3'}),
            'student_number': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['campattendees']