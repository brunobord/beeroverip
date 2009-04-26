import os.path
import datetime
import random
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Drink(models.Model):
    """Drink meta-model. Abstract class

    * `name`: name of the beer, to be displayed.
    * `slug`: prepopulated from `name`.
	"""

    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/' % self.slug



class Beer(Drink):
    """Beer model."""

    class Meta:
        verbose_name = _('beer')
        verbose_name_plural = _('beers')
        ordering = ('slug',)

    def _picture(self):
        pic = self.beerimage_set.order_by('?')[0]
        print pic
        return self.beerimage_set.order_by('?')[0]
    picture = property(_picture)


class NotABeer(Drink):
    """Not-a-Beer model."""

    class Meta:
        verbose_name = _('drink')
        verbose_name_plural = _('drinks')
        ordering = ('slug',)

    def get_absolute_url(self):
        return '/%s/%s/' % ('notabeer', self.slug)


class DrinkImage(models.Model):
    """Drink image Meta-model.

    * `credits`: text field where you can add meta information, credits, etc.
    * `upload_date`: the date/time the beer has been uploaded.
    """
    credits = models.TextField(_('credits'), blank=True)
    upload_date = models.DateTimeField(_('upload date'),
        default=datetime.datetime.now)

    class Meta:
        abstract = True

    def _url(self):
        return self.picture.url
    url = property(_url)


class BeerImage(DrinkImage):
    """Beer image-related information

    * `beer`: The linked beer.
    * `picture`: image field (requires PIL module).
    """
    beer = models.ForeignKey(Beer)
    picture = models.ImageField(_('picture'), upload_to='beers/', blank=True)


class NotABeerImage(Drink):
    """Image-related information for normal drinks

    * `notabeer`: The linked drink.
    * `picture`: image field (requires PIL module).
    """
    notabeer = models.ForeignKey(NotABeer)
    picture = models.ImageField(_('picture'), upload_to='notabeers/', blank=True)

# EOF
