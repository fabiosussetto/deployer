from django.core.management.base import BaseCommand, CommandError
from gae_deployer.models import Project, Deployment
from django.db import transaction

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            project_name = args[0]
        except IndexError:
            self.stderr.write("Wrong usage: missing project name\n")
            return False
            
        try:
            project = Project.objects.get(name=project_name)
        except Project.DoesNotExist:
            self.stderr.write("Missing project: %s\n" % project_name)
            return False
        
        project.deploy()
            
        self.stdout.write("Deployed\n")
