from django.urls import path

from projects import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('projects/<str:pk>/', views.project, name='project'),
    path('create-project/', views.createProject, name="create_projects"),
    path('update-project/<str:pk>/', views.updateProject, name="update_projects"),
    path('del-project/<str:pk>/', views.deleteProject, name="delete_projects"),
]