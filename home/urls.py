from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # --- Quiz 1 & Quiz 2 Routes ---
    path('', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('about/', views.personal_info, name='personal_info'),

    # --- Quiz 3 Required Routes ---
    path('projects/add/', views.add_project, name='add_project'),
    path('contact/', views.contact_view, name='contact'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimonies/add/', views.add_testimony, name='add_testimony'),
    path('testimonies/<int:pk>/', views.testimony_detail, name='testimony_detail'),

    # --- New Admin Auth Routes ---
    path('login/', views.AdminLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # --- New Admin Dashboard & List Routes ---
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/projects/', views.admin_project_list, name='admin_project_list'),
    path('dashboard/projects/create/', views.create_project, name='create_project'),
    path('dashboard/tech-stacks/', views.admin_tech_stack_list, name='admin_tech_stack_list'),
    path('dashboard/tech-stacks/create/', views.create_tech_stack, name='create_tech_stack'),
]