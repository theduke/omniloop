from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

from omni_projects.models import Project


class Website(models.Model):
    project = models.ForeignKey(Project, related_name='websites')

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=255, help_text='The main URL for this website.')

    tags = TaggableManager(blank=True)

    slug = models.SlugField(max_length=100, unique=True)


    class Meta:
        verbose_name = _('Website')
        verbose_name_plural = _('Websites')

    def __str__(self):
        return '{} <{}>'.format(self.name, self.url)


class WebsiteEnvironment(models.Model):
    MODE_PRODUCTION = 'production'
    MODE_STAGING = 'staging'
    MODE_TESTING = 'testing'
    MODE_DEVELOPMENT = 'development'

    MODE_CHOICES = (
        (MODE_PRODUCTION, 'production'),
        (MODE_STAGING, 'staging'),
        (MODE_TESTING, 'testing'),
        (MODE_DEVELOPMENT, 'development'),
    )

    website = models.ForeignKey(Website, related_name='envs')
    mode = models.CharField(max_length=50, choices=MODE_CHOICES)
    url = models.URLField(max_length=255, help_text='URL where the env can be reached.')

    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('WebsiteEnvironment')
        verbose_name_plural = _('WebsiteEnvironments')

    def __str__(self):
        return self.mode
