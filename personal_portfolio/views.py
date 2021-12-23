from django.shortcuts import render

# Create your views here.
from personal_portfolio.models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'personal_portfolio/home.html', {'projects': projects})