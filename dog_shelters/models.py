from django.db import models


class Classe(models.Model):
 nom = models.CharField(max_length=200)
 specialite = models.CharField(max_length=200)
 def __str__(self):
    return self.nom

class Etudiant(models.Model):
 classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
 nom = models.CharField(max_length=200)
 prenom = models.TextField()
 dateNaiss = models.DateTimeField(auto_now_add=True)
 def __str__(self):
    return self.nom

