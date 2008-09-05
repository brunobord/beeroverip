from django.db import models
from django.utils.translation import ugettext as _
import os.path

class Beer(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100)
    picture = models.ImageField(_('picture'), upload_to='beers/', blank=True)
    credits = models.TextField(_('credits'), blank=True)

    class Admin:
        pass

    class Meta:
        verbose_name = _('beer')
        verbose_name_plural = _('beers')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/' % self.slug

    def get_picture_url(self):
        from django.conf import settings
        return os.path.join(settings.MEDIA_URL, self.picture.url)
