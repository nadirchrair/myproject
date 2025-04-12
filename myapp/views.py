from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def teams(request):
    return render(request, 'teams.html')
def groupebactirie(request):
    return render(request, 'groupebacterie.html')
def bactirie(request):
    return render(request, 'bactirie.html')
def bactirie_detail(request):
    return render(request, 'detials.html')