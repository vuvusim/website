from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Profile, Skill

def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    lefIndex = (int(page) - 4)
    if lefIndex < 1:
        lefIndex = 1

    rightIndex = (int(page) + 5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(lefIndex, rightIndex)
    return custom_range, profiles

def searchProfiles(request):
    search_text = ''

    if request.GET.get('search_text'):
        search_text = request.GET.get('search_text')
    
    skills = Skill.objects.filter(name__icontains=search_text)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_text) | 
        Q(short_intro__icontains=search_text) |
        Q(skill__in=skills)
        )

    return profiles, search_text