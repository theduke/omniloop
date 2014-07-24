# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WebsiteEnvironment.url'
        db.add_column('omni_devshop_websiteenvironment', 'url',
                      self.gf('django.db.models.fields.URLField')(max_length=255, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WebsiteEnvironment.url'
        db.delete_column('omni_devshop_websiteenvironment', 'url')


    models = {
        'omni_customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        'omni_devshop.website': {
            'Meta': {'object_name': 'Website'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'websites'", 'to': "orm['omni_projects.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'})
        },
        'omni_devshop.websiteenvironment': {
            'Meta': {'object_name': 'WebsiteEnvironment'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255'}),
            'website': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'envs'", 'to': "orm['omni_devshop.Website']"})
        },
        'omni_projects.project': {
            'Meta': {'object_name': 'Project'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['omni_customers.Customer']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'}),
            'typ': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['omni_projects.ProjectType']"})
        },
        'omni_projects.projecttype': {
            'Meta': {'object_name': 'ProjectType'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'unique': 'True'})
        }
    }

    complete_apps = ['omni_devshop']