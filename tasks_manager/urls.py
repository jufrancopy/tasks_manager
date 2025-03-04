from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tasks.views import dashboard  # Importar la vista dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  # Ahora accesible desde la raíz
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Incluye las URLs de la aplicación "tasks"
]

# Configuración para servir archivos multimedia durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)