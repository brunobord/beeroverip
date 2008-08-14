from django.db import models

class Beer(models.Model):
    name = models.CharField(_('name'), maxlength=100)
    slug = models.SlugField(_('slug'), maxlength=100, prepopulate_from=('name',))
    picture = models.ImageField(_('picture'), upload_to='beers/')

    class Admin:
        pass

    class Meta:
        verbose_name = _('beer')
        verbose_name_plural = _('beers')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/' % self.slug
