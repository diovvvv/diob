from django.shortcuts import render, get_object_or_404
from .models import Project, PersonalInformation

def project_list(request):
    # Fetch all projects from the database
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, pk):
    # Fetch a single project using its primary key (ID)
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def personal_info(request):
    # Fetch the personal info record (assuming there's only one entry)
    info = PersonalInformation.objects.first()
    return render(request, 'portfolio/about.html', {'info': info})
