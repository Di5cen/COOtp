from django.db import models

# Create your models here.

class Departement(models.Model):
  numero = models.IntegerField()
  prix = models.FloatField()

class Usine(models.Model):
  departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
  taille = models.FloatField()
  machines = models.ForeignKey(Machine,on_delete=models.PROTECT)
  recettes = models.ForeignKey(Recette,on_delete=models.PROTECT)
  stocks = models.ForeignKey(Quantiteingredient,on_delete=models.PROTECT)

class Prix(models.Model):
  ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
  departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
  prix = models.FloatField()

class Machine(models.Model):
  nom = models.CharField(max_length=200)
  prix = models.FloatField()

class Recette(models.Model):
  nom = models.CharField(max_length=200)
  action = models.FloatField(Action,on_delete=models.CASCADE)

class Ingredient(models.Model):
  nom = models.CharField(max_length=200)

class Quantiteingredient(models.Model):
  ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
  quantite = models.IntegerField()

class Action(models.Model):
  machines = models.ForeignKey(Machine,on_delete=models.CASCADE)
  commande = models.CharField(max_length=200)
  duree = models.IntegerField()
  ingredient = models.ForeignKey(Quantiteingredient,on_delete=models.PROTECT)
  def __str__(self):
        return 
