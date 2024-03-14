"""
URL configuration for gardeningproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from gardeningproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('project/',views.project,name='project'),
    path('feature/',views.feature,name='feature'),
    path('quote/',views.quote,name='quote'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('404/',views.error,name='404'),
    path('contact/',views.contact,name='contact'),
]
