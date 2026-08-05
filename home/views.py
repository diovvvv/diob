from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Project, PersonalInformation, Testimony, Inquiry
from .forms import ProjectForm, TestimonyForm

# --- Existing Quiz 1 & 2 Views ---

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def personal_info(request):
    info = PersonalInformation.objects.first()
    return render(request, 'portfolio/about.html', {'info': info})

# --- Quiz 3 Required Views ---

# 1. Add Project (Function-Based View + Django Form)
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'portfolio/add_project.html', {'form': form})

# 2. Contact Page (Function-Based View + HTML Form)
def contact_view(request):
    if request.method == 'POST':
        Inquiry.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            contact_number=request.POST.get('contact_number'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            message=request.POST.get('message')
        )
        return redirect('contact')
    return render(request, 'portfolio/contact.html')

# 3. Add Testimony (Function-Based View + Django Form)
def add_testimony(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony_list')
    else:
        form = TestimonyForm()
    return render(request, 'portfolio/add_testimony.html', {'form': form})

# 4. List Testimonies (Class-Based ListView)
class TestimonyListView(ListView):
    model = Testimony
    template_name = 'portfolio/testimony_list.html'
    context_object_name = 'testimonies'
    ordering = ['-created_at']

# 5. Testimony Detail (Function-Based Detail View)
def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'portfolio/testimony_detail.html', {'testimony': testimony})