from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request, pk):
    context = {'pk': pk}
    if request.method == 'POST':
        nom = request.POST.get('a')
        prenom = request.POST.get('b')
        dateNaiss = request.POST.get('c')
        d = request.POST.get('d')
        classe = get_object_or_404(models.Classe, pk=d)
        user = models.Etudiant.objects.create(nom=nom, prenom=prenom, dateNaiss=dateNaiss, classe=classe)
    return render(request, 'templates/index.html', context=context)

def classe_list(request):
    classes = models.Classe.objects.all()
    context = { 'classes': classes }
    return render(request, 'templates/classe_list.html', context=context)


def et_list(request):
    etudiants = models.Etudiant.objects.all()
    context = { 'etudiants': etudiants }
    return render(request, 'templates/classe_list.html', context=context)


def classe_detail(request, pk):
    classe = get_object_or_404(models.Classe, pk=pk)
    etudiant = models.Etudiant.objects.all()
    context = {'classe': classe, 'etudiant': etudiant}
    return render(request, 'templates/classe_detail.html', context=context)

def register(request):
    if request.method == 'POST':
        nom = request.POST.get('a')
        prenom = request.POST.get('b')
        dateNaiss = request.POST.get('c')
        d = request.POST.get('d')
        classe = get_object_or_404(models.Classe, pk=d)
        user = models.Etudiant.objects.create_user(nom=nom, prenom=prenom, dateNaiss=dateNaiss, classe=classe)
        redirect('dog_shelters:index')
    return render(request, 'templates/classe_list.html')