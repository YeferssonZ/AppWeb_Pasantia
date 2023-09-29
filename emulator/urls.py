from django.urls import path
from . import views

app_name = 'emulator'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.CustomSignupView.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('mis_proyectos/', views.mis_proyectos, name='mis_proyectos'),
    path('crear_proyecto/', views.crear_proyecto, name='crear_proyecto'),
    path('cargar_archivo/', views.cargar_archivo, name='cargar_archivo'),
    path('exportar_xml/', views.exportar_xml, name='exportar_xml'),
    path('ejemplos/', views.ejemplos, name='ejemplos'),
    path('ejemplos/<int:ejemplo_id>/', views.detalle_ejemplo, name='detalle_ejemplo'),

]