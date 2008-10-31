import os.path
import datetime
from django.db import models
from django.utils.translation import ugettext as _


class Beer(models.Model):
    """Beer model.

    * `name`: name of the beer, to be displayed.
    * `slug`: prepopulated from `name`.
    * `picture`: image field (requires PIL module).
    * `credits`: text field where you can add meta information, credits, etc.
    * `upload_date`: the date/time the beer has been uploaded."""
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100)
    picture = models.ImageField(_('picture'), upload_to='beers/', blank=True)
    credits = models.TextField(_('credits'), blank=True)
    upload_date = models.DateTimeField(_('upload date'),
        default=datetime.datetime.now)

    class Meta:
        verbose_name = _('beer')
        verbose_name_plural = _('beers')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/' % self.slug
