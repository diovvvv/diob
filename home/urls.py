from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import AdminLoginForm

urlpatterns = [
    # Root Route
    path('', views.project_list, name='home'),

    # --- Quiz 1 & Quiz 2 Routes ---
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('about/', views.personal_info, name='personal_info'),

    # --- Quiz 3 Required Routes ---
    path('projects/add/', views.add_project, name='add_project'),
    path('contact/', views.contact_view, name='contact'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/add/', views.add_testimony, name='add_testimony'),
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony_detail'),

    # --- New Dashboard & Tech Stack Routes (Requirements 2 & 3) ---
    path('login/', auth_views.LoginView.as_view(
        template_name='home/login.html',
        authentication_form=AdminLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/projects/create/', views.create_project, name='create_project'),
    path('dashboard/tech-stacks/create/', views.create_tech_stack, name='create_tech_stack'),
]