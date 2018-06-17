from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Hey y'all! You're at the messages index!")

def module(request, serial_no):
    return HttpResponse("Module Test")

def string(request, string_id):
    return HttpResponse("String Test")

def api_modules(request):
    return JsonResponse(ModuleMsg.latest_messages())

def api_module(request, serial_no):
    return JsonResponse(ModuleMsg.last_24_hours(serial_no))

def api_string(request, string_id):
    return JsonResponse(StringMsg.last_24_hours(string_id))
