from beers.models import Beer
from django.contrib import admin
#from django.utils.translation import ugettext_lazy as _

class BeerOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Beer, BeerOptions)
