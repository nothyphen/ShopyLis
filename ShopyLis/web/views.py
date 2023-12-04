from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def home(request):
    list, c = List.objects.get_or_create(user=request.user)
    return HttpResponse(list.get_items)