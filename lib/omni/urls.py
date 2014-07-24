from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import permission_required, login_required

from django_baseline.decorators import group_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'devshop', include('omni_devshop.urls')),
)
