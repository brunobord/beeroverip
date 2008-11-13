import os.path
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Drink(models.Model):
    """Drink meta-model. Abstract class

    * `name`: name of the beer, to be displayed.
    * `slug`: prepopulated from `name`.
    * `picture`: image field (requires PIL module).
    * `credits`: text field where you can add meta information, credits, etc.
    * `upload_date`: the date/time the beer has been uploaded."""

    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100)
    credits = models.TextField(_('credits'), blank=True)
    upload_date = models.DateTimeField(_('upload date'),
        default=datetime.datetime.now)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/' % self.slug


class Beer(Drink):
    """Beer model."""
    picture = models.ImageField(_('picture'), upload_to='beers/', blank=True)
    class Meta:
        verbose_name = _('beer')
        verbose_name_plural = _('beers')
        ordering = ('-upload_date',)



class NotABeer(Drink):
    """Not-a-Beer model."""

    picture = models.ImageField(_('picture'), upload_to='notabeers/', blank=True)

    class Meta:
        verbose_name = _('drink')
        verbose_name_plural = _('drinks')
        ordering = ('-upload_date',)

    def get_absolute_url(self):
        return '/%s/%s/' % ('notabeer', self.slug)

# EOF
