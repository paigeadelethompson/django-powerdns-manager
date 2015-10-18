from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

# URLs for django.contrib.admin
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

# URLs for powerdns_manager
urlpatterns.append(
    url('^powerdns/', include('powerdns_manager.urls')),
)
