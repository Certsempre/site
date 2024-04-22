from django.http import HttpResponse
from django.shortcuts import render

def notas(request):
    return render(request, 'notas/pages/notas.html')



