from django.db import models , json

# Create your models here.

class Departement(models.Model):
  numero = models.IntegerField()
  prix_departement = models.FloatField()

  def __str__(self):
      return str(self.numero)

  def json(self):
        return {
            'id': self.id,
            'numero': str(self.numero),
            'prix_departement': str(self.prix_departement),
        }

class Machine(models.Model):
  nom = models.CharField(max_length=200)
  prix_machine = models.FloatField()

  def __str__(self):
      return self.nom

def json(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'prix_machine': str(self.prix_machine),
        }
  
class Ingredient(models.Model):
  nom = models.CharField(max_length=200)

  def __str__(self):
      return self.nom

  def json(self):
        return {
            'id': self.id,
            'nom': self.nom,
        }
    
class Quantiteingredient(models.Model):
  ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
  quantite = models.IntegerField()

  def __str__(self):
      return str(self.ingredient)

  def json(self):
        return {
            'id': self.id,
            'ingredient': self.ingredient.nom,
            'quantite': str(self.quantite),
        }
    
class Action(models.Model):
  machines = models.ForeignKey(Machine,on_delete=models.CASCADE)
  commande = models.CharField(max_length=200)
  duree = models.IntegerField()
  ingredient = models.ForeignKey(Quantiteingredient,on_delete=models.PROTECT)
  action = models.CharField(max_length=200)

  def __str__(self):
      return self.action

  def json(self):
        return {
            'id': self.id,
            'machines': self.machines.nom,
            'commande': self.quantite,
            'duree': str(self.duree),
            'ingredient': self.ingredient.nom,
            'action': self.action,
        }
  
class Recette(models.Model):
  nom = models.CharField(max_length=200)
  action = models.ForeignKey(Action,on_delete=models.CASCADE)

  def __str__(self):
      return self.nom

  def json(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'action': self.action.action,
        }
   
class Usine(models.Model):
  departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
  taille = models.FloatField()
  machines = models.ManyToManyField('Machine')
  recettes = models.ForeignKey(Recette,on_delete=models.PROTECT)
  stocks = models.ManyToManyField('Quantiteingredient')

  def __str__(self):
      return str(self.taille)

  def json(self):
        return {
            'id': self.id,
            'departement': str(self.departement.numero),
            'taille': str(self.taille),
            'machines': str(self.machines.nom),
            'recettes': self.recettes.nom,
            'stocks': self.stocks.ingredient,
        }
 
class Prix(models.Model):
  ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
  departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
  prix = models.FloatField()

  def __str__(self):
      return str(self.prix)

  def json(self):
        return {
            'id': self.id,
            'ingredient': self.ingredient.nom,
            'departement': self.departement.nom,
            'prix': str(self.prix),
        }
 




