# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.gae_username'
        db.add_column('gae_deployer_project', 'gae_username',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)

        # Adding field 'Project.gae_password'
        db.add_column('gae_deployer_project', 'gae_password',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.gae_username'
        db.delete_column('gae_deployer_project', 'gae_username')

        # Deleting field 'Project.gae_password'
        db.delete_column('gae_deployer_project', 'gae_password')


    models = {
        'gae_deployer.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gae_deployer.Project']"})
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