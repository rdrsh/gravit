function preloadImages() {
    for (var i = 0; i < arguments.length; i++) {
        $("<img/>").attr("src", arguments[i])
    }
}
function preloadImagesList(list) {
    for (var i = 0; i < list.length; i++) {
        $("<img/>").attr("src", list[i])
    }
}

function setCur(obj) {
    var path = ''+window.location
    path = path.split('/')
    if (path.length > 3 && path[3]) {
        path = path[3]
        var sel = 'a[href^=/'+path+'/]'
        // alert(sel)
        $(sel, obj).addClass('current')
    }
}

function printVersion() {
    $('.print-hide').hide()
    $('#col-l').text('')
    $('#col-r').text('')
}