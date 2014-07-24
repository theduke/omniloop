from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import permission_required, login_required

from django_baseline.decorators import group_required

from .views import websites as view_website

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'websites', login_required(view_website), name='omni_devshop_websites'),
)
