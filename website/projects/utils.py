from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Project, Tag

def paginateProjects(request, projects, results):
    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    lefIndex = (int(page) - 4)
    if lefIndex < 1:
        lefIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(lefIndex, rightIndex)
    return custom_range, projects

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