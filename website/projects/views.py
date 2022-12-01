from django.shortcuts import render

def main(request):
    return render(request, 'projects/main.html')

def projects(request):
    pass 