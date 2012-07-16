# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Deployment.in_progress'
        db.add_column('gae_deployer_deployment', 'in_progress',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Deployment.in_progress'
        db.delete_column('gae_deployer_deployment', 'in_progress')


    models = {
        'gae_deployer.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'finished_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_progress': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gae_deployer.Project']"}),
            'stderr_log': ('django.db.models.fields.TextField', [], {}),
            'stdout_log': ('django.db.models.fields.TextField', [], {}),
            'success': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'gae_deployer.project': {
            'Meta': {'object_name': 'Project'},
            'deployment_branch': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gae_password': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gae_username': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'git_repo_uri': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['gae_deployer']