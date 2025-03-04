from django import forms
from .models import Project, Task, Document

from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    document = forms.FileField(required=False)  # Campo para subir documentos

    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'dependency', 'status']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']