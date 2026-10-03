from django import forms
from .models import Project, Testimony, TechStack


class ProjectForm(forms.ModelForm):
    # Requirement 3: Radio buttons fetching all TechStack objects
    tech_stack = forms.ModelMultipleChoiceField(
        queryset=TechStack.objects.all(),
        widget=forms.RadioSelect,
        required=True
    )

    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stack', 'link']
        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Project Description'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/...'}),
        }


# Requirement 3: Create Tech Stack Form
class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tech Stack Name'}),
        }


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'content']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your feedback/testimony here...'}),
        }