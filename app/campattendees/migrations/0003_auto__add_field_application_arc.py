# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Application.arc'
        db.add_column('campattendees_application', 'arc',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Application.arc'
        db.delete_column('campattendees_application', 'arc')


    models = {
        'campattendees.application': {
            'Meta': {'object_name': 'Application'},
            'age': ('django.db.models.fields.DateField', [], {}),
            'arc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'cse_program': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'dietary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medical': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'medical_pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3'}),
            'student_number': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['campattendees']