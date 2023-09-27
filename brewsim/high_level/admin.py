from django.contrib import admin

# Register your models here.
from .models import Departement, Usine, Prix, Machine, Recette, Ingredient, Quantiteingredient, Action

class DepartementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')

class UsineAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'country')

class PrixAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')

class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'country')

class RecetteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'country')

class QuantiteingredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')

class ActionAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'country')
  
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Usine, UsineAdmin)
admin.site.register(Prix, PrixAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Recette, RecetteAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Quantiteingredient, QuantiteingredientAdmin)
admin.site.register(Action, ActionAdmin)
