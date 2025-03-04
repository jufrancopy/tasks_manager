from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task, Document
from .forms import ProjectForm, TaskForm, DocumentForm

# Lista todos los proyectos
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/project_list.html', {'projects': projects})

# Muestra los detalles de un proyecto, sus tareas y documentos
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project=project)
    documents = Document.objects.filter(project=project)
    return render(request, 'tasks/project_detail.html', {
        'project': project,
        'tasks': tasks,
        'documents': documents
    })

# Agrega un nuevo proyecto
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()  # Guarda el proyecto

            # Verifica si el usuario subió un archivo y créalo en el modelo Document
            document_file = request.FILES.get("document")
            if document_file:
                Document.objects.create(project=project, file=document_file)

            return redirect("project_list")  # Redirige a la lista de proyectos
    else:
        form = ProjectForm()

    return render(request, "tasks/add_project.html", {"form": form})

# Agrega una tarea a un proyecto específico
def add_task(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})

# Sube un documento a un proyecto específico
def upload_document(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.project = project
            document.uploaded_by = request.user
            document.save()
            return redirect('project_detail', pk=project.id)
    else:
        form = DocumentForm()
    return render(request, 'tasks/upload_document.html', {'form': form, 'project': project})

def dashboard(request):
    # Obtener el número de tareas pendientes y aprobadas
    pending_tasks = Task.objects.filter(completed=False).count()
    completed_tasks = Task.objects.filter(completed=True).count()

    context = {
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'tasks/dashboard.html', context)