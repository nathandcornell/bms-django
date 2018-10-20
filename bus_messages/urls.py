from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('module/<str:serial_no>', views.module, name='module_details'),
    path('string/<int:string_id>', views.string, name='string_details'),
    path('api/modules', views.api_modules, name='api_modules'),
    path('api/module/<str:serial_no>', views.api_module, name='api_module'),
    path('api/string/<int:string_id>', views.api_string, name='api_string'),
]
