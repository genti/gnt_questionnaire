from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
        url(r'^salva/', 'gnt_questionnaire.views.salva'),
)