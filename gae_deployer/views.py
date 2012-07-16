# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from gae_deployer.models import Project, Deployment, Task

class ProjectList(ListView):
    model = Project

    
class ProjectCreate(CreateView):
    model = Project


class ProjectUpdate(UpdateView):
    model = Project    

    
class DeploymentList(ListView):
    model = Deployment
    queryset = Deployment.objects.select_related('project').order_by('-started_on')

    
class DeploymentDetail(DetailView):
    model = Deployment
    
    
class TaskList(ListView):
    model = Task
    
    
class TaskCreate(CreateView):
    model = Task


class TaskUpdate(UpdateView):
    model = Task