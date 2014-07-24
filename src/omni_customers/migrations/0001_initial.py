# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table('omni_customers_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(blank=True, max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
        ))
        db.send_create_signal('omni_customers', ['Customer'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table('omni_customers_customer')


    models = {
        'omni_customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['omni_customers']