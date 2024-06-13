from django.shortcuts import render
from django.http import HttpResponse


def app_1(request):
    return HttpResponse('<h1>JEEPERS KRREEPERS INCORPORATED</h1>')
