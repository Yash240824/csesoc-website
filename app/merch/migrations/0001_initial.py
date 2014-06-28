# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.create_table('merch_hoodie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('student_number', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('contact_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('shirt_size', self.gf('django.db.models.fields.CharField')(default='N', max_length=3)),
            ('payment_status', self.gf('django.db.models.fields.CharField')(default='N', max_length=1)),
        ))
        db.send_create_signal('merch', ['Hoodie'])

    def backwards(self, orm):
        db.delete_table('merch_hoodie')

    models = {
        'merch.hoodie': {
            'Meta': {'object_name': 'Application'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'shirt_size': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '3'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '1'}),
        }
    }

    complete_apps = ['merch']