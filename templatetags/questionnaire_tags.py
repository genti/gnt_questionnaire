from django import template
from django.http import HttpRequest, HttpResponse
from gnt_questionnaire.models import *
from localsite.models import *
from django.db.models import Max
from django.conf import settings
from django.contrib.sites.models import Site


register = template.Library()




def printRange(context,id_range,id_domanda,id_questionario,id_risposta):
    Q_range=Range.objects.get(pk__exact=id_range)
        
    new_range=range(int(Q_range.start),(int(Q_range.end)+1));

    context.update(locals())
    return context   
printRange = register.inclusion_tag('questionnaire/range.html', takes_context=True)(printRange)
