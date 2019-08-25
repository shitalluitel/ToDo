from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import views

AdminSite.login_template = 'rest_framework/login.html'
views.LogoutView.template_name = 'rest_framework/login.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/v1/', include('apps.api.v1.urls')),
]

if settings.DEBUG:
    from apps.commons.api.v1.swagger_views import SwaggerSchemaView
    urlpatterns += [
        path('api/root/', SwaggerSchemaView.as_view(), name='swagger_view'),
        path('', RedirectView.as_view(url='/api/root/', permanent=False))
    ]