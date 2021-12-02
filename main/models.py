from django.db import models

class Recompense(models.Model):
    Image = models.ImageField(upload_to='images/Recompenses')
    Nom = models.CharField(max_length=200)
    
class Article(models.Model):
    Date = models.DateField()
    Titre = models.CharField(max_length=200)
    Source = models.TextField()
    Texte = models.TextField()

class Sauvetage(Article):
    NbMort = models.PositiveIntegerField(default=0)
    
class Personne(models.Model):
    sauvetage = models.ManyToManyField(Sauvetage)
    Nom = models.CharField(max_length=200)
    Prenom = models.CharField(max_length=200)
    Recompenses = models.ManyToManyField(Recompense)
    class TypePersonne(models.TextChoices):
        Sauveteur = "Sauveteur"
        Mecanicien = "Mecanicien"
        Capitaine = "Capitaine"
    Type = models.CharField(choices=TypePersonne.choices, max_length=15)

class Images(models.Model):
    image = models.ImageField(upload_to='images/sauvetages/')



class TypeBateau(models.Model):
    typeDuBateau = models.CharField(max_length=120)

class Bateau(models.Model):
    Type = models.ForeignKey(TypeBateau, on_delete=models.CASCADE)
    Nom = models.CharField(max_length=200)
    Sauvetage = models.ManyToManyField(Sauvetage)

class Stations (Article):
    nbPersonneSauve = models.PositiveIntegerField(default=0)
    image = models.ForeignKey(Images,on_delete=models.CASCADE)