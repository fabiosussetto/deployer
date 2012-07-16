from django.db import models
from django.conf import settings
import os
import subprocess
import datetime
from git import *

TASK_CHOICES = [('bundle_assets', 'Bundle assets'), ('send_email', 'Bundle assets')]


class Project(models.Model):
    name = models.CharField(max_length=200)
    git_repo_uri = models.CharField(max_length=200)
    deployment_branch = models.CharField(max_length=200)
    gae_username = models.CharField(max_length=200)
    gae_password = models.CharField(max_length=200)
    
    @models.permalink
    def get_absolute_url(self):
        return ('edit-project', (), {'pk': self.pk})
        
    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        
    def deploy(self):
        repo_dir = os.path.join(settings.GAE_DEPLOYER_BASE_PATH, self.name)
        if not os.path.exists(repo_dir):
            os.makedirs(repo_dir)
            
        try:
            repo = Repo(repo_dir)
        except InvalidGitRepositoryError:
            repo = Repo.clone_from(self.git_repo_uri, repo_dir)
            
        origin = repo.remotes.origin
        git = repo.git
        branch_to_deploy = getattr(repo.heads, self.deployment_branch, None)
        if not branch_to_deploy:
            git.checkout('origin/%s' % self.deployment_branch, b=self.deployment_branch)
        else:
            git.checkout(self.deployment_branch)
        
        origin.fetch()
        origin.pull()
        
        deployment = Deployment(project=self, started_on=datetime.datetime.now(), in_progress=True)
        deployment.save()
        
        cmd = ["appcfg.py", 'update', '--passin', '--no_cookies', '--email=%s' % self.gae_username, repo_dir]
        
        s1 = subprocess.Popen(['echo', self.gae_password], shell=False, stdout=subprocess.PIPE)
        s2 = subprocess.Popen(cmd, stdin=s1.stdout, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        stdout, stderr = s2.communicate()
        
        to_update = {
            'success': not bool(s2.returncode),
            'in_progress': False,
            'stdout_log': stdout,
            'stderr_log': stderr,
            'finished_on': datetime.datetime.now()
        }
        
        for key, value in to_update.items():
            setattr(deployment, key, value)
        
        deployment.save()        
    
class Deployment(models.Model):
    project = models.ForeignKey('Project')
    started_on = models.DateTimeField()
    finished_on = models.DateTimeField(null=True)
    in_progress = models.BooleanField(default=False)
    success = models.NullBooleanField(null=True)
    stdout_log = models.TextField(null=True)
    stderr_log = models.TextField(null=True)
    tasks = models.ManyToManyField('Task')
    
    
class Task(models.Model):
    type = models.CharField(choices=['bundle_assets', 'send_email'])
    