$(document).ready(function() {
    $('#title-2').animate({
        opacity: 1,
    }, 1100, function() {
        $('#title-1-heading-1').animate({
            left: 0
        }, 1000, function() {
            $('#title-1-heading-2').animate({
                bottom: 0
            }, 1000)
        })
    })
})