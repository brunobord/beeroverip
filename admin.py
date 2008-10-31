from beers.models import Beer
from django.contrib import admin

class BeerOptions(admin.ModelAdmin):
    """Basic admin option class.
    Defines the slug prepopulated source."""
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'upload_date']

admin.site.register(Beer, BeerOptions)
