from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

from omni_customers.models import Customer


class ProjectType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=100)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProjectType, self).save(*args, **kwargs)


class Project(models.Model):
    typ = models.ForeignKey(ProjectType, verbose_name='Type', related_name='projects')
    customer = models.ForeignKey(Customer, related_name='projects')
    
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    tags = TaggableManager(blank=True)

    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)
