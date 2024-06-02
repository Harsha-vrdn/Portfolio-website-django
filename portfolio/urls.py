from django.contrib import admin
from django.urls import path
from home.views import *
from contact.views import *
from about.views import *
from projects.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('contact', contact_us, name='contact'),
    path('about', about, name='about'),
    path('projects', projects, name='projects'),
]
