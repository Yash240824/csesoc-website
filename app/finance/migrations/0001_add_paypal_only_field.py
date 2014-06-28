# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.add_column('finance_invoice', 'paypal_only',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

    def backwards(self, orm):
        db.delete_column('finance_invoice', 'paypal_only')

    models = {
        'finance.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'max_quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'paypal_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'primary_key': 'True'}),
            'students_login': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['finance']