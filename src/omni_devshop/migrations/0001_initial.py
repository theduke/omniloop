# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Website'
        db.create_table('omni_devshop_website', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='websites', to=orm['omni_projects.Project'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('omni_devshop', ['Website'])

        # Adding model 'WebsiteEnvironment'
        db.create_table('omni_devshop_websiteenvironment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('website', self.gf('django.db.models.fields.related.ForeignKey')(related_name='envs', to=orm['omni_devshop.Website'])),
            ('mode', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('omni_devshop', ['WebsiteEnvironment'])


    def backwards(self, orm):
        # Deleting model 'Website'
        db.delete_table('omni_devshop_website')

        # Deleting model 'WebsiteEnvironment'
        db.delete_table('omni_devshop_websiteenvironment')


    models = {
        'omni_customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'website': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '255'})
        },
        'omni_devshop.website': {
            'Meta': {'object_name': 'Website'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'websites'", 'to': "orm['omni_projects.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        'omni_devshop.websiteenvironment': {
            'Meta': {'object_name': 'WebsiteEnvironment'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'envs'", 'to': "orm['omni_devshop.Website']"})
        },
        'omni_projects.project': {
            'Meta': {'object_name': 'Project'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['omni_customers.Customer']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'typ': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['omni_projects.ProjectType']"})
        },
        'omni_projects.projecttype': {
            'Meta': {'object_name': 'ProjectType'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['omni_devshop']