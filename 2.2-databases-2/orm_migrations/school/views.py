from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students_query = Student.objects.order_by('group').prefetch_related('teachers')

    context = {
        'object_list': students_query
    }

    return render(request, template, context)
