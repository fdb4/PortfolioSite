from django.shortcuts import render
from .models import Aboutme,Education,Coreskills, Certifications,Workexperience
from projects.models import Projectshort
from django.http import FileResponse
import os
# Create your views here.
def home(request):
    aboutme = Aboutme.objects.first()
    education = Education.objects.all()
    coreskills = Coreskills.objects.all()
    certifications = Certifications.objects.all()
    projects = Projectshort.objects.all()
    work = Workexperience.objects.all()
    context = {
        "aboutme": aboutme,
        "education": education,
        "coreskills": coreskills,
        "certifications": certifications,
        "projects": projects,
        "work": work
    }
    return render(request,"home.html",context)
def aboutMe(request):
    aboutme = Aboutme.objects.first()
    education = Education.objects.all()
    coreskills = Coreskills.objects.all()
    certifications = Certifications.objects.all()
    projects= Projectshort.objects.all()
    work=Workexperience.objects.all()
    context = {
        "aboutme": aboutme,
        "education": education,
        "coreskills": coreskills,
        "certifications": certifications,
        "projects": projects,
        "work":work
    }
    return render(request, "aboutme.html",context)
def resume(request):
    cwd=os.getcwd()
    direct=os.path.join(cwd,"pages","templates","resumeFrancescoBettinardi.pdf")
    return FileResponse(open(direct,'rb'), content_type='application/pdf')