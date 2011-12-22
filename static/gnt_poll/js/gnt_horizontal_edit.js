document.write("<style>.hidden{ display:none;}</style>")

$(function() {

	$('a.add-another').each(function(index,value){
		modello=$(this).attr('id').replace('add_id_','');
		
		
		if ($(this).parent().find('select').hasClass('selectfilter')){
		
					c_model=$(this).attr('href').split('/')[3];
					c_project=$(this).attr('href').split('/')[2];
					
					edit_link = '&nbsp;&nbsp;&nbsp;<a onclick="return showAddAnotherPopup(this);" id="edit_id_'+modello+'" class="edit-another" href="/admin/'+c_project+'/'+c_model+'/##/"> <img width="10" height="10" alt="Modifica" src="/static/admin/img/admin/icon_changelink.gif"></a>';
			
					
					$('#add_id_'+modello).after(edit_link);
					
					$('#edit_id_'+modello).mousedown(function() {
						
						c_model=$(this).attr('id').replace('edit_id_','');
						
						
						if ($('#id_'+c_model+'_to option:selected').length==1) {
							
							id = $('#id_'+c_model+'_to option:selected').attr('value');
							
							link = $(this).attr('href').replace('##', id);
							
							$('#edit_id_'+c_model+'').attr('href', link)
						} else {
							alert('Controlla la selezione.');
			
						}
					})
					
					
		}
	})
});