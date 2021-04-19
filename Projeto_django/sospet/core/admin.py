from django.contrib import admin
#o .model, é porque a pasta já está no mesmo diretorio no casoa pasta core poderia ser core.models.
#from core.models import Pet
from .models import Pet


# Register your models here.
# criando a classe de registro no admin
@admin.register(Pet)# decorador
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'description', 'phone', 'email', 'begin_date']