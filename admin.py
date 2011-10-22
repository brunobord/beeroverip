from beers.models import Beer, BeerImage
from django.contrib import admin


class BeerImageInline(admin.StackedInline):
    model = BeerImage


class BeerOptions(admin.ModelAdmin):
    """Basic admin option class.
    Defines the slug prepopulated source."""
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']
    inlines = [BeerImageInline]


admin.site.register(Beer, BeerOptions)
