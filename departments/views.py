from django.http import HttpResponse
from django.shortcuts import render
from .models import Department, BloodType
from django.template import loader


def index(request):
    departments = Department.objects.all()
    context = {
        'departments': departments,
    }
    return render(request, 'departments/index.html', context)

