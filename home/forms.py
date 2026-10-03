from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Project, TechStack, Testimony


# Requirement 1: Dedicated Admin/Superuser Only Login Form
class AdminLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not (user.is_superuser or user.is_staff):
            raise ValidationError(
                "Access restricted. Regular users cannot authenticate on this page.",
                code="not_admin",
            )


# Requirement 3: Create Tech Stack Form
class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Tech Stack Name (e.g. Python, Django)'
            }),
        }


# Requirement 3: Create Project Form (Updated with RadioSelect for Tech Stack)
class ProjectForm(forms.ModelForm):
    tech_stack = forms.ModelMultipleChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.RadioSelect,
        required=True,
        help_text="Select a tech stack for this project."
    )

    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stack', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Project Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Project Description'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'https://github.com/...'
            }),
        }


# Previous TestimonyForm (Maintained intact)
class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'content']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Full Name'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Write your feedback/testimony here...'
            }),
        }