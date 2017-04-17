"""miniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from parking import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from registration.backends.hmac.views import RegistrationView
from parking.forms import MyCustomUserForm


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/', views.search),
    url(r'^security/$', views.security_list),
    url(r'^security/(?P<place_name>([a-z]+))/$', views.security),
    url(r'^security/(?P<place_name>([a-z]+))/update/$', views.security_update),
    url(r'^carowner/(?P<carowner_id>[0-9]+)/search/$', views.search, name='search'),
    url(r'^carowner/(?P<carowner_id>[0-9]+)/$', views.carowner, name='search'),
    url(r'^carowner/(?P<carowner_id>[0-9]+)/search/loc$', views.loc, name='loc'),
    url(r'^carowner/(?P<carowner_id>[0-9]+)/search/name/$', views.namelist, name='name'),
    url(r'^carowner/(?P<carowner_id>[0-9]+)/search/name/(?P<place_name>([a-z]+))/$',views.name, name='name'),
    url(r'^carowner/(?P<carowner_id>[0-9]+)/search/name/(?P<place_name>([a-z]+))/book/$',views.book, name='name'),
    url(r'^landowner/(?P<landowner_id>[0-9]+)/rent/$', views.landowner),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=MyCustomUserForm
        ),
        name='registration_register',
    ),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^accounts/', include('registration.backends.hmac.urls')),    
    # url(r'^admin/', admin.site.urls),
    ]
