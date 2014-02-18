# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Application'
        db.create_table('campattendees_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('student_number', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('cse_username', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('cse_program', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('age', self.gf('django.db.models.fields.DateField')()),
            ('dietary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('medical', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('payment_status', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
            ('medical_form', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medical_pdf', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('shirt_size', self.gf('django.db.models.fields.CharField')(default='N', max_length=3)),
        ))
        db.send_create_signal('campattendees', ['Application'])


    def backwards(self, orm):
        # Deleting model 'Application'
        db.delete_table('campattendees_application')


    models = {
        'campattendees.application': {
            'Meta': {'object_name': 'Application'},
            'age': ('django.db.models.fields.DateField', [], {}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'cse_program': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'cse_username': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'dietary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medical': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'medical_form': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medical_pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3'}),
            'student_number': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['campattendees']