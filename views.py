# -*- coding: utf-8 -*-
from urllib import *

from django.http import HttpResponseRedirect, Http404,HttpResponse
from django.shortcuts import render_to_response,redirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from gnt_questionnaire.models import *
from localsite.models import *
import settings
from django import forms
import csv
from  django.template.defaultfilters import slugify
from django.contrib.sites.models import RequestSite,Site
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMultiAlternatives
from datetime import datetime, date
from django.template import (Node, Variable, TemplateSyntaxError,TokenParser, Library, TOKEN_TEXT, TOKEN_VAR)
from django.views.decorators.csrf import csrf_exempt, csrf_protect

def salva(request):
    azienda = get_object_or_404(Azienda,pk__exact=request.POST.get('azienda',False))
    #assert False
    #return render_to_response('gnt_poll/questionario_results.html', {'post':request.POST}, context_instance=RequestContext(request))

    for item in request.POST:
        ids=item.split('#')
        
        if(len(ids)==2):
            id_questionario=ids[0]
            id_domanda=ids[1]
        
        if(len(ids)==3):
           
            id_questionario=ids[0]
            id_domanda=ids[1]
            id_risposta=ids[2]
                        
        if(len(ids)>=2):
        
            domanda=get_object_or_404(Domanda,pk__exact=id_domanda)
            '''
                risposta chiusa
            
            '''
            if domanda.tipo == "0": #domanda chiusa
                
                            
                if domanda.multiple == 1:
                    
                    risposte=request.POST.getlist(item)
                    for risposta in risposte:
                        try:
                            risposta_chiusa=Risposta_chiusa.objects.get(id__exact=risposta)
                        except:
                            assert False, risposta
                            
                        risultato, created = Risultati.objects.get_or_create(azienda=azienda,domanda=domanda,risposta_chiusa=risposta_chiusa)
                        risultato.testo=str(risposta)
                        risultato.save()

                
                
                
                else:
                
                    risposta=request.POST.get(item,False)
                    
                    try:
                        risposta_chiusa=Risposta_chiusa.objects.get(id__exact=risposta)
                    except: #boolean
                        try:
                            risposta_splitted=risposta.split('#')
                            risposta_chiusa=Risposta_chiusa.objects.get(id__exact=risposta_splitted[0])
                            risposta=risposta_splitted[1]
                        except:
                            raise TemplateSyntaxError("Errore nel salvataggio risposta chiusa. Name: %s Value: %s " % (item, risposta))

                    risultato, created = Risultati.objects.get_or_create(azienda=azienda,domanda=domanda,risposta_chiusa=risposta_chiusa)
                    risultato.testo=str(risposta)
                    risultato.save()
 
                    
        
            '''
            risposta di tipo range
            
            nome del campo =  questionario#domanda#risposta 
            valore = valore nel range
            '''
            if domanda.tipo == '2': #range
                
                risposta=request.POST.get(item,False)
                try:
                    risposta_chiusa=Risposta_chiusa.objects.get(id__exact=ids[2])
                except:
                    assert False, risposta
                    
                risultato, created = Risultati.objects.get_or_create(azienda=azienda,domanda=domanda,risposta_chiusa=risposta_chiusa)
                risultato.testo=str(risposta)
                risultato.save()
            '''
                risposta aperta
            
            '''
            if domanda.tipo == '1': 
        
                name_risposta='id_risposta#%s' % item
                id_risposta=request.POST[name_risposta]
                
                risposta_aperta=get_object_or_404(Risposta_aperta,id__exact=int(id_risposta))
                
                risultato, created = Risultati.objects.get_or_create(azienda=azienda,domanda=domanda,risposta_aperta=risposta_aperta)
                risultato.testo=str(request.POST.get(item,''))
                risultato.save()
                    
                
    return render_to_response('questionnaire/questionario_results.html', {'post':request.POST}, context_instance=RequestContext(request))
