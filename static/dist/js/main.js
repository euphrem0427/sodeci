$(function() {
    "use strict";
    /** disable input until checkbox not checked */
    $('#checksolaire').change(function () {
        $('#solaire').prop("disabled", !this.checked);
    }).change()

    $('#checkgroupe').change(function () {
        $('#groupe').prop("disabled", !this.checked);
    }).change()

    $('#checknouveau').change(function () {
        $('#nouveau').prop("disabled", !this.checked);
    }).change()

    $('#checkproduction').change(function () {
        $('#Production').prop("disabled", !this.checked);
    }).change()

    $('#checksbee').change(function () {
        $('#Sbee').prop("disabled", !this.checked);
    }).change()

    $('#checkwaterwQT').change(function () {
        $('#water').prop("disabled", !this.checked);
    }).change()

    $('#checkobservation').change(function () {
        $('#Observation').prop("disabled", !this.checked);
    }).change()

    $('#checknbrpanne').change(function () {
        $('#nbrepanne').prop("disabled", !this.checked);
    }).change()

    $('#checknbrpanne').change(function () {
        $('#pannedesc').prop("disabled", !this.checked);
    }).change()
    
    $('#checkprod').change(function () {
        $('#prod').prop("disabled", !this.checked);
    }).change()

    //script to calculate production
    $(document).ready(function() {
        //this calculates values automatically 
        Subtract();
        $("#ancien, #nouveau").on("keydown keyup", function() {
            Subtract();
        });
    });
    
    function Subtract() {
                var ancien = document.getElementById('ancien').value;
                var nouveau = document.getElementById('nouveau').value;
                var result = parseInt(nouveau) - parseInt(ancien);
                if (!isNaN(result)) {
                    document.getElementById('subt').value = result;
                }
            }

    //script to get commune filter by departement
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