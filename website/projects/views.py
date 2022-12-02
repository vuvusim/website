from django.shortcuts import render
from .models import Project

projectsList = [
    {
        'id':'1',
        'title':'Gym Website',
        'description':'Fully functional Gym website',
    },
    {
        'id':'2',
        'title':'Recepie Website',
        'description':'Fully functional Recepie website',
    },
    {
        'id':'3',
        'title':'Bike repair',
        'description':'Fully functional Bike repair website'
    },
]

def projects(request):
    page = 'Projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i ['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})