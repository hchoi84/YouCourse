$(document).ready(function(){
    console.log("load")
    $('.add-subject').hide()
    $('#subject_id').on("change", function(){
        console.log("change");
        if ($(this).val() == "add") {
            console.log("new subject");
            $('.add-subject').show()
        }
    })

});