from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('module/<str:serial_no>', views.module, name='module_details'),
    path('string/<int:string_id>', views.string, name='string_details'),
    path('api/modules', views.api_modules, name='api_modules'),
    path('api/module/<str:serial_no>', views.api_module, name='api_module'),
    path('api/string/<int:string_id>', views.api_string, name='api_string'),
]
