from beers.models import Beer
from django.contrib import admin

class BeerOptions(admin.ModelAdmin):
    """Basic admin option class.
    Defines the slug prepopulated source."""
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Beer, BeerOptions)
