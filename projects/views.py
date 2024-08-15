from django.shortcuts import render
from .models import Projectshort,Projectlong
def projectIndex(request):
    projects = Projectshort.objects.all()
    context = {
        "projects":projects
    }
    return render(request,'projects/projectIndex.html',context)
def projectDetail(request,pk):
    project = Projectlong.objects.get(pk=pk)
    context = {
        "project":project
    }#man i love json
    return render(request,'projects/project.html',context)

# Create your views here.
