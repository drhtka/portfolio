from django.shortcuts import render

# Create your views here.
from personal_portfolio.models import Project


def home(request):
    projects = Project.objects.all()
    #
    # for project in projects:
    #     print('projects')
    #     print(project.adaptiv)
    return render(request, 'personal_portfolio/home.html', {'projects': projects})

# def drf_post(request):
#     drf_post = Project.objects.all()
#     print('drf_post')
#     print(drf_post)
#     return render(request, 'personal_portfolio/home.html', {'drf_post': drf_post})