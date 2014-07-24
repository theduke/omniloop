from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext as _

from taggit.managers import TaggableManager


class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    website = models.URLField(max_length=255, blank=True)

    tags = TaggableManager(blank=True)

    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return self.name
