# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Deployment.started_on'
        db.add_column('gae_deployer_deployment', 'started_on',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 14, 0, 0)),
                      keep_default=False)


        # Changing field 'Deployment.success'
        db.alter_column('gae_deployer_deployment', 'success', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Deployment.stderr_log'
        db.alter_column('gae_deployer_deployment', 'stderr_log', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Deployment.finished_on'
        db.alter_column('gae_deployer_deployment', 'finished_on', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Deployment.stdout_log'
        db.alter_column('gae_deployer_deployment', 'stdout_log', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Deployment.started_on'
        db.delete_column('gae_deployer_deployment', 'started_on')


        # Changing field 'Deployment.success'
        db.alter_column('gae_deployer_deployment', 'success', self.gf('django.db.models.fields.BooleanField')())

        # User chose to not deal with backwards NULL issues for 'Deployment.stderr_log'
        raise RuntimeError("Cannot reverse this migration. 'Deployment.stderr_log' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Deployment.finished_on'
        raise RuntimeError("Cannot reverse this migration. 'Deployment.finished_on' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Deployment.stdout_log'
        raise RuntimeError("Cannot reverse this migration. 'Deployment.stdout_log' and its values cannot be restored.")

    models = {
        'gae_deployer.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'finished_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_progress': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gae_deployer.Project']"}),
            'started_on': ('django.db.models.fields.DateTimeField', [], {}),
            'stderr_log': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'stdout_log': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'success': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
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