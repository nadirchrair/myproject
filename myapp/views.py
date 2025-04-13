from django.shortcuts import render , get_object_or_404
from .models import Service, GroupBacterie, Bacterie

def index(request):
    services = Service.objects.all()
    return render(request, 'index.html',{'services': services})

def teams(request):
    return render(request, 'teams.html')
def groupebactirie(request,id):
    service = get_object_or_404(Service, id=id)
    groups = service.groups.all()
    return render(request, 'groupebacterie.html', {'service': service, 'groups': groups})
def bactirie(request,group_id):
    group = get_object_or_404(GroupBacterie, id=group_id)
    bacteries = group.bacteries.all()
    return render(request, 'bactirie.html',{'group': group, 'bacteries': bacteries})
def predection(request):
    return render(request, 'Predection.html')