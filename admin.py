from beers.models import Beer
from django.contrib import admin

class BeerOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Beer, BeerOptions)
