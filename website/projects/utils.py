from django.db.models import Q
from .models import Project, Tag

def searchProjects(request):
    search_text = ''

    if request.GET.get('search_text'):
        search_text = request.GET.get('search_text')

    tags = Tag.objects.filter(name__icontains=search_text)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_text) |
        Q(description__icontains=search_text) |
        Q(owner__name__icontains=search_text) |
        Q(tags__in=tags)
    )
    return projects, search_text