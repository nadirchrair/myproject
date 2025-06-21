from django.shortcuts import render , get_object_or_404
from .models import Service, GroupBacterie, Bacterie
import joblib
import numpy as np
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os

# Base path of your Django project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths to model and encoder
model_path = os.path.join(BASE_DIR, 'myapp', 'files', 'rf_model.pkl')
encoder_path = os.path.join(BASE_DIR, 'myapp', 'files', 'label_encoder.pkl')

# Load them
rf_model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)
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
def predectionEntérobactéries(request):
    return render(request, 'identification/Entérobactéries.html')
@csrf_exempt
def predict_bacteria(request):
    result = None

    if request.method == 'POST':
        features = [
            'ONPG', 'ADH', 'LDC', 'ODC', 'CIT', 'H2S', 'URE', 'TDA', 'IND',
            'VP', 'GEL', 'GLU', 'MAN', 'INO', 'SOR', 'RHA', 'SAC', 'MEL',
            'AMY', 'ARA', 'Oxydase', 'NO2', 'N2', 'Mobilité'
        ]
        input_data = []
        for feature in features:
            value = request.POST.get(feature)
            binary = 1 if value == 'positive' else 0
            input_data.append(binary)

        input_array = np.array(input_data).reshape(1, -1)
        pred = rf_model.predict(input_array)
        label = label_encoder.inverse_transform(pred)[0]
        result = f" {label}"
    return render(request, 'formulaire.html', {'result': result})
def predectionstash(request):
    return render(request, 'identification/stash.html')
def predectionPseudo_Aeromonas(request):
    return render(request, 'identification/Pseudo-Aeromonas.html')
def predectionEnterococcus(request):
    return render(request, 'identification/Enterococcus.html')
def predectionStreptococcus(request):
    return render(request, 'identification/Streptococcus.html')
def predectionBacillus(request):
    return render(request, 'identification/Bacillus.html')
def contact(request):
    return render(request, 'contact.html')