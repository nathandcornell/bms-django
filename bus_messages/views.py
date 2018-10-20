from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from .models.module_msg import ModuleMsg
from .models.string_msg import StringMsg

# Create your views here.
def index(request):
    return ""

def module(request, serial_no):
    return HttpResponse("Module Test")

def string(request, string_id):
    return HttpResponse("String Test")

def api_modules(request):
    return JsonResponse(ModuleMsg.latest_messages(), safe=False)

def api_module(request, serial_no):
    return JsonResponse(serializers.serialize('json', ModuleMsg.last_24_hours(serial_no)), safe=False)

def api_string(request, string_id):
    return JsonResponse(serializers.serialize('json', StringMsg.last_24_hours(string_id)), safe=False)
