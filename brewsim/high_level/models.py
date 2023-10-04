from django.db import models

# Create your models here.

class Departement(models.Model):
  numero = models.IntegerField()
  prix_departement = models.FloatField()
  def __str__(self):
      return str(self.numero)

class Machine(models.Model):
  nom = models.CharField(max_length=200)
  prix_machine = models.FloatField()
  def costs(self):
      return self.prix_machine
  def __str__(self):
      return self.nom

class Ingredient(models.Model):
  nom = models.CharField(max_length=200)

  def __str__(self):
      return self.nom

class Quantiteingredient(models.Model):
  ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
  quantite = models.IntegerField()
  def costs(self):
      return self.quantite*self.ingredient.prix_set.get(ingredient__nom=self.ingredient.nom).prix
  def __str__(self):
      return str(self.ingredient)

class Action(models.Model):
  machines = models.ForeignKey(Machine,on_delete=models.CASCADE)
  commande = models.CharField(max_length=200)
  duree = models.IntegerField()
  ingredient = models.ForeignKey(Quantiteingredient,on_delete=models.PROTECT)
  action = models.CharField(max_length=200)

  def __str__(self):
      return self.action
  
class Recette(models.Model):
  nom = models.CharField(max_length=200)
  action = models.ForeignKey(Action,on_delete=models.CASCADE)

  def __str__(self):
      return self.nom

class Usine(models.Model):
  departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
  taille = models.FloatField()
  machines = models.ManyToManyField('Machine')
  recettes = models.ForeignKey(Recette,on_delete=models.PROTECT)
  stocks = models.ManyToManyField('Quantiteingredient')
  def costs(self):
      value_costs=0
      for machine in self.machines.all():
          value_costs+=machine.costs()
      for stock in self.stocks.all():
          value_costs+=stock.costs()
      value_costs+=self.departement.prix_departement*self.taille
      return value_costs
  def __str__(self):
      return str(self.taille)

class Prix(models.Model):
  ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
  departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
  prix = models.FloatField()

  def __str__(self):
      return str(self.prix)





