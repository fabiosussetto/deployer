# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('gae_deployer_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('github_repo_uri', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('deployment_branch', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('gae_deployer', ['Project'])

        # Adding model 'Deployment'
        db.create_table('gae_deployer_deployment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gae_deployer.Project'])),
        ))
        db.send_create_signal('gae_deployer', ['Deployment'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('gae_deployer_project')

        # Deleting model 'Deployment'
        db.delete_table('gae_deployer_deployment')


    models = {
        'gae_deployer.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gae_deployer.Project']"})
        },
        'gae_deployer.project': {
            'Meta': {'object_name': 'Project'},
            'deployment_branch': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'github_repo_uri': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['gae_deployer']