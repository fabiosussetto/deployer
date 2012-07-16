# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.github_repo_uri'
        db.delete_column('gae_deployer_project', 'github_repo_uri')

        # Adding field 'Project.git_repo_uri'
        db.add_column('gae_deployer_project', 'git_repo_uri',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=200),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Project.github_repo_uri'
        raise RuntimeError("Cannot reverse this migration. 'Project.github_repo_uri' and its values cannot be restored.")
        # Deleting field 'Project.git_repo_uri'
        db.delete_column('gae_deployer_project', 'git_repo_uri')


    models = {
        'gae_deployer.deployment': {
            'Meta': {'object_name': 'Deployment'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gae_deployer.Project']"})
        },
        'gae_deployer.project': {
            'Meta': {'object_name': 'Project'},
            'deployment_branch': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'git_repo_uri': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['gae_deployer']