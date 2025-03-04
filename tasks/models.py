from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del Proyecto")
    description = models.TextField(verbose_name="Descripción")
    start_date = models.DateField(verbose_name="Fecha de Inicio")
    end_date = models.DateField(verbose_name="Fecha de Finalización")
    dependency = models.CharField(max_length=200, verbose_name="Dependencia del Proyecto")
    status = models.CharField(max_length=50, choices=[
        ('analysis', 'Análisis de Factibilidad'),
        ('presentation', 'Presentación'),
        ('approval', 'Aprobación'),
        ('execution', 'Ejecución y Monitoreo')
    ], verbose_name="Estado del Proyecto")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Proyecto")
    name = models.CharField(max_length=200, verbose_name="Nombre de la Tarea")
    description = models.TextField(verbose_name="Descripción")
    completed = models.BooleanField(default=False, verbose_name="Completado")
    deadline = models.DateField(verbose_name="Fecha Límite")

    def __str__(self):
        return self.name

class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Nom")
    file = models.FileField(upload_to='documents/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name