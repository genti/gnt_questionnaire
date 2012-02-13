from django.db import models
from django.template.defaultfilters import slugify
import datetime
from django.utils.translation import ugettext_lazy as _
from localsite.models import *
from django.db.models import signals
from tinymce import models as tinymce_models
from tinymce.widgets import TinyMCE

ANSWER_TYPE = (
        ('0', 'Chiusa'),
        ('1', 'Aperta'),
        ('2', 'Range'),
        ('3', 'Modulare'),
    )

class Questionario(models.Model):
    titolo = models.CharField(_('Titolo'),max_length=200)
    intro=models.TextField(_('Introduzione'))
    #custom field to tisplay scrollable textarea
    long_intro=models.TextField(_('Introduzione lunga'))
    published = models.BooleanField(_('Pubblicato'),default=True)
    published_on = models.DateTimeField(_('Data'),auto_now=True, auto_now_add=True,blank=True)
    
    slug = models.SlugField();
    def __unicode__(self):
        return self.titolo
    class Meta:
        verbose_name_plural = _('Questionari')



class Range(models.Model):
    start=models.CharField(_('Start'),blank=True, null=True,max_length=3) 
    end=models.CharField(_('End'),blank=True, null=True,max_length=3) 
    def __unicode__(self):
        return "%s - %s" % (self.start,self.end)
    class Meta:
        verbose_name_plural = _('Range risposte chiuse')



#opzioni per risposte chiuse
class Risposta_chiusa(models.Model): 
    domanda = models.ForeignKey('Domanda')
    range = models.ForeignKey('Range',blank=True, null=True)
    
    testo=models.TextField(_('Testo'),blank=True, null=True)
    risposta = models.BooleanField(_('Risposta'),default=False)
 
    boolean = models.BooleanField(_('Booleano (Si/No)'),default=False)
    published_on = models.DateTimeField(auto_now=True, auto_now_add=True,blank=True,verbose_name=_('Data'))
    def __unicode__(self):
        if self.boolean:
            return "%s %s" % (self.domanda.domanda,"Si - No")
        else:
            return self.testo
        
    class Meta:
        verbose_name="Risposta chiusa"
        verbose_name_plural = _('Risposte chiuse')




class Risposta_aperta(models.Model):
   
   
    domanda = models.ForeignKey('Domanda')
    
    maxlength=models.CharField(_('Lunghezza massima'),blank=True,null=True,max_length=500)
    
    published = models.BooleanField(_('Pubblicato'),default=True)
    published_on = models.DateTimeField(auto_now=True, auto_now_add=True,blank=True,verbose_name=_('Data'))

    def __unicode__(self):
        return '%s, domanda n. %s' % (self.domanda.questionario.titolo,self.domanda.numero)
    class Meta:
        verbose_name_plural = _('Risposte aperte')


class Domanda(models.Model):
    numero = models.PositiveSmallIntegerField(blank=True, null=True)
    questionario = models.ForeignKey('Questionario')
        
    tipo = models.CharField(_('Tipo di risposta'),max_length=1, choices=ANSWER_TYPE)  
    
    domanda = models.TextField(_('Domanda'),blank=True, null=True)
    
    multiple = models.BooleanField(_('Risposta multipla'),default=False)
    
    published = models.BooleanField(_('Pubblicato'),default=True)
    published_on = models.DateTimeField(auto_now=True, auto_now_add=True,blank=True,verbose_name=_('Data'))
        
    def __unicode__(self):
        return "%s - domanda n. %s" % (self.questionario.titolo,self.numero)
    class Meta:
        verbose_name_plural = _('Domande')



class Risultati(models.Model):
    azienda = models.ForeignKey('localsite.Azienda')
    
    questionario=models.ForeignKey('Questionario',blank=True, null=True)
    domanda = models.ForeignKey('Domanda',blank=True, null=True)
    risposta_aperta = models.ForeignKey('Risposta_aperta',blank=True, null=True,related_name="Risposta aperta")
    risposta_aperta_cluster = models.ForeignKey('Risposta_aperta',blank=True, null=True,related_name="Risposta aperta mod")
    risposta_chiusa = models.ForeignKey('Risposta_chiusa',blank=True, null=True,related_name="Risposta chiusa")
    testo = models.TextField(_('Testo risposta aperta'),blank=True, null=True)
    
    def __unicode__(self):
        return "%s - %s" % (self.questionario.titolo,self.azienda.anagrafica.nome)
    class Meta:
        verbose_name_plural = _('Risultati')







