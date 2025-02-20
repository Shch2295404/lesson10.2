from django.shortcuts import render


def index(request):
    return render(request, 'project_app/index.html')

def about(request):
    return render(request, 'project_app/about.html')

def section_one(request):
    return render(request, 'project_app/section_one.html')

def section_two(request):
    return render(request, 'project_app/section_two.html')
