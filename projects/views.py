from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from projects.forms import ProjectForm
from projects.models import Project


def projects(request):
    querysets = Project.objects.all()
    context = {'projects': querysets}

    return render(request, "templates/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()

    context = {'project': projectObj, 'tags': tags}
    return render(request, "templates/single-projects.html", context)


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST,  request.FILES,)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {'form': form}
    return render(request, "templates/project-form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")

    context = {'form': form}
    return render(request, "templates/project-form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect("projects")
    context = {'projects': project}
    return render(request, "templates/delete-obj.html", context)













