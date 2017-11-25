$(document).ready(function() {
    $('#duration-picker').duration_picker();

    $('#my-select').multiSelect()
    $('#candidate-select').multiSelect()

    var questionCounter = 2;

    $("#add-question").click(function() {
        var questionId = 'question-' + questionCounter;
        var $elem = $( ".question-multiple .col-5" ).data( "arr", [ 1 ] ),
        $clone = $elem.clone( true )
          // Deep copy to prevent data sharing
          .data( "arr", $.extend( [], $elem.data( "arr" ) ) ).addClass(questionId);
          
        $('.added-questions').append($clone);
        var $button = "<button type='button' class=' btn btn-danger " + questionId + "' id='"+ questionId +"' onclick=deleteQuestion('"+ questionId +"')>Remove Question</button>"
        $('.added-questions').append("<div class='col-2 d-flex align-items-center " + questionId + "'>" + $button + "</div>")
        questionCounter += 1;

    })

    $('.availability-field').hide()

    $('#id_availability').on('change', function() {
        if ($('#id_availability').val() == 'AvailableOnSpecificTime') {
            $('.availability-field').show()
        } else {
            $('.availability-field').hide()
        }

        console.log($('#id_availability').val())
    })

});

function deleteQuestion(question_id) {
    $('.' + question_id).remove()
}