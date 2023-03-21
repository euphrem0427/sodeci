$(function() {
    "use strict";
    $('#check').change(function () {
        $('#fname').prop("disabled", !this.checked);
    }).change()

    $("#formAdd select[name='departement']").on('change',function(){
        console.log('Bien changé');
        var $this = $(this);
  
        if ($this.val() != ''){
            $("#formAdd select[name='commune']").find('.after').nextAll().remove();
            $.ajax({
                url:'departement/list_communes/'+$this.val(),
                type:'GET',
                success: function(response){
                    let options = '';
                    response.data.forEach(commune => {
                        options+='<option value='+commune.id+'>'+commune.name+'</option>';
                    });
                    $("#formAdd select[name='commune']").find('.after').after(options);

                },
                error: function(response){
                    console.log('Aucune commune n\'existe pour ce département');
                }
            });
        }else{
            $("#formAdd select[name='commune']").find('.after').nextAll().remove();
        }
    });

});