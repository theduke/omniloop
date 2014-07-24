# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectType'
        db.create_table('omni_projects_projecttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('omni_projects', ['ProjectType'])

        # Adding model 'Project'
        db.create_table('omni_projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('typ', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['omni_projects.ProjectType'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['omni_customers.Customer'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('omni_projects', ['Project'])


    def backwards(self, orm):
        # Deleting model 'ProjectType'
        db.delete_table('omni_projects_projecttype')

        # Deleting model 'Project'
        db.delete_table('omni_projects_project')


    models = {
        'omni_customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '255'})
        },
        'omni_projects.project': {
            'Meta': {'object_name': 'Project'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['omni_customers.Customer']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'typ': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['omni_projects.ProjectType']"})
        },
        'omni_projects.projecttype': {
            'Meta': {'object_name': 'ProjectType'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['omni_projects']