from django.conf.urls.defaults import patterns, include, url
from gae_deployer.views import ProjectList, ProjectCreate, ProjectUpdate, DeploymentList, DeploymentDetail, TaskCreate, TaskList, TaskUpdate

urlpatterns = patterns('',
    url(r'^$', ProjectList.as_view(), name='home'),
    url(r'^projects/new$', ProjectCreate.as_view(), name='new-project'),
    url(r'^projects/edit/(?P<pk>\d+)$', ProjectUpdate.as_view(), name='edit-project'),
    
    url(r'^deployments$', DeploymentList.as_view(), name='deployment-list'),
    url(r'^deployments/view/(?P<pk>\d+)$', DeploymentDetail.as_view(), name='deployment-detail'),
    
    url(r'^tasks$', TaskList.as_view(), name='task-list'),
    url(r'^tasks/create$', TaskCreate.as_view(), name='task-create'),
    url(r'^tasks/update/(?P<pk>\d+)$', TaskUpdate.as_view(), name='task-update'),
)
