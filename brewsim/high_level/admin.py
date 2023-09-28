from django.contrib import admin

# Register your models here.
from .models import Departement, Usine, Prix, Machine, Recette, Ingredient, Quantiteingredient, Action

class DepartementAdmin(admin.ModelAdmin):
    list_display = ('numero', 'prix_departement')

class UsineAdmin(admin.ModelAdmin):
    list_display = ('departement', 'taille', 'machines','recettes','stocks')

class PrixAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'departement', 'prix')

class MachineAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix_machine')

class RecetteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'action')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('nom',)

class QuantiteingredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'quantite')

class ActionAdmin(admin.ModelAdmin):
    list_display = ('machines', 'commande', 'duree','ingredient')
  
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Usine, UsineAdmin)
admin.site.register(Prix, PrixAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Recette, RecetteAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Quantiteingredient, QuantiteingredientAdmin)
admin.site.register(Action, ActionAdmin)
