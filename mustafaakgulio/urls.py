"""mustafaakgulio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('page_404', page_404, name='page_404'),
    path('about', about, name='about'),
    path('blog_details', blog_details, name='blog_details'),
    path('blog_list', blog_list_sidebar_right, name='blog_list_sidebar_right'),
    path('contact', contact, name='contact'),
    path('faq', faq, name='faq'),
    path('project_details', project_details, name='project_details'),
    path('project_list', project_list, name='project_list'),
    path('service_details', service_details, name='service_details'),
    path('service_list', service_list, name='service_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()