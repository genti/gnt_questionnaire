from django import template
from django.http import HttpRequest, HttpResponse
from gnt_questionnaire.models import *
from localsite.models import *
from django.db.models import Max
from django.conf import settings
from django.contrib.sites.models import Site


register = template.Library()




def printRange(context,id_range,id_domanda,id_questionario,id_risposta,id_azienda):
    Q_range=Range.objects.get(pk__exact=id_range)
        
    new_range=range(int(Q_range.start),(int(Q_range.end)+1));
    
    azienda=Azienda.objects.get(pk__exact=id_azienda)
    questionario=Questionario.objects.get(pk__exact=id_questionario);
    domanda=Domanda.objects.get(pk__exact=id_domanda,questionario=questionario);
    risposta=Risposta_chiusa.objects.get(pk__exact=id_risposta,domanda=domanda);
    try:
        risultato=Risultati.objects.get(azienda=azienda,questionario=questionario,domanda=domanda,risposta_chiusa=risposta)
        result=int(risultato.testo)
    except:
        risultato=False
        result=False        
    

    context.update(locals())
    return context   
printRange = register.inclusion_tag('questionnaire/range.html', takes_context=True)(printRange)






def getAnswer(id_questionario,id_domanda,id_risposta,id_azienda,bool_val=False):
    questionario=Questionario.objects.get(pk__exact=id_questionario);
    domanda=Domanda.objects.get(pk__exact=id_domanda,questionario=questionario);
    azienda=Azienda.objects.get(pk__exact=id_azienda)
    
    
    '''
        ('0', 'Chiusa'),
        ('1', 'Aperta'),
         ('2', 'Range'),
         ('3', 'Modulare'),
    '''
    
    
    if domanda.tipo == '0':
        risposta=Risposta_chiusa.objects.get(pk__exact=id_risposta,domanda=domanda);
                    
        
        try:
            risultato=Risultati.objects.get(azienda=azienda,questionario=questionario,domanda=domanda,risposta_chiusa=risposta)
            
            
                        
            if int(risultato.testo) == 1 and bool_val == 1 and risposta.boolean:
                return ' checked="checked"'
            if int(risultato.testo) == 1 and bool_val == 0 and risposta.boolean:
                return ''
                
            if int(risultato.testo) == 0 and bool_val == 1 and risposta.boolean:
                return ''
            if int(risultato.testo) == 0 and bool_val == 0 and risposta.boolean:
                return ' checked="checked"'
                     
            #endbooleano
            
            
            
            if id_risposta == int(risultato.testo):
                return ' checked="checked"'
            else:
                return ''
        except:
            return ''
        
    
    if domanda.tipo == '1':
        risposta=Risposta_aperta.objects.get(pk__exact=id_risposta,domanda=domanda);
        try:
            risultato=Risultati.objects.get(azienda=azienda,questionario=questionario,domanda=domanda,risposta_aperta=risposta)
            return risultato.testo
        except:
            return ''
    
    if domanda.tipo == '3':
        risposta=Risposta_aperta.objects.get(pk__exact=id_risposta,domanda=domanda);


        risultato=Risultati.objects.filter(azienda=azienda,questionario=questionario,domanda=domanda,risposta_aperta=risposta,risposta_aperta_cluster=risposta)
        str=''
        default='<tr class="module_%s"> <td > <textarea name="%s#%s#%s" id="" class="textArea"></textarea> </td> </tr>' %(id_domanda,id_questionario,id_domanda,id_risposta)
        for item in risultato:
            str+=' <tr class="module_%s"> <td > <textarea name="%s#%s#%s" id="" class="textArea">%s</textarea> </td> </tr>' %(id_domanda,id_questionario,id_domanda,id_risposta,item.testo)
            
        if str:    
            return str
        else:
            return default            



register.simple_tag(getAnswer)