document.write("<style>.hidden{ display:none;}</style>");
$(function() {
    $('div.risposta').addClass('hidden');
    $('div.opzioni').addClass('hidden');
    $('#id_tipo').change(function(){
            if($(this).attr('value') == '0') {   
                    if($('textarea#id_risposta').attr('value').length>0)
                    {
                            if(confirm('Cambiando tipo di risposta eliminerai il testo inserito.')) {
                                    $('textarea#id_risposta').attr('value')='';
                                    $('div.risposta').addClass('hidden');
                                    $('div.opzioni').removeClass('hidden');
                                    
                                    
                            }
                    } else {
                        $('div.risposta').addClass('hidden');
                        $('div.opzioni').removeClass('hidden');
                    }
            } 
            else 
            {
                    if($('#id_opzioni_to option').length > 0) {
                            if(confirm('Cambiando tipo di risposta eliminerai le opzioini associate.')) {
                                $('#id_opzioni_to').empty();
                                $('div.risposta').removeClass('hidden');
                                $('div.opzioni').addClass('hidden');                            
                            }
                    } else {
                        $('div.risposta').removeClass('hidden');
                        $('div.opzioni').addClass('hidden');                        
                    }
            }
    });
    
});