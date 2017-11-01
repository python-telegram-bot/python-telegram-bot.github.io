from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'website/index.html', {})

def page(request, page):
    return render(request, 'website/%s.html' % page, {})
