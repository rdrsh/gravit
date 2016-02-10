// referer: {{ ref }}
// url: {{ url }}
// alert('{{ url }}')

var mceFull = ''
var mceLight = ''

{% ifequal url 'banner' %}
var mceFull = 'id_content'
{% endifequal %}

{% ifequal url 'page' %}
var mceFull = 'id_content'
{% endifequal %}

{% ifequal url 'news' %}
var mceFull = 'id_content'
{% endifequal %}

{% ifequal url 'payment' %}
var mceFull = 'id_content,id_annotation'
{% endifequal %}

{% ifequal url 'help' %}
var mceFull = 'id_question,id_answer'
{% endifequal %}

{% ifequal url 'product' %}
var mceFull = 'id_annotation,id_description'
{% endifequal %}

{% ifequal url 'service' %}
var mceFull = 'id_content,id_settings'
{% endifequal %}

var mceSettings = {
    mode : "exact",
    elements : "id_content",
    theme : "advanced",
    plugins : "advimage,advlink,media,contextmenu",
    theme_advanced_buttons1_add_before : "newdocument,separator",
    theme_advanced_buttons1_add : "fontselect,fontsizeselect",
    theme_advanced_buttons2_add : "separator,forecolor,backcolor,liststyle",
    theme_advanced_buttons2_add_before: "cut,copy,separator,",
    theme_advanced_buttons3_add_before : "",
    theme_advanced_buttons3_add : "media",
    theme_advanced_toolbar_location : "top",
    theme_advanced_toolbar_align : "left",
    extended_valid_elements : "hr[class|width|size|noshade]",
    paste_use_dialog : false,
    theme_advanced_resizing : true,
    theme_advanced_resize_horizontal : true,
    apply_source_formatting : true,
    force_br_newlines : true,
    force_p_newlines : false,
    relative_urls : true,
    width:700,
    height:700,

    // file_browser_callback : "AjexFileManager.open",
}

if (mceFull) {
    var elements = mceFull.split(',')
    // alert(elements)
    for (var i = 0; i < elements.length; i++) {
        mceSettings.elements = elements[i]
        tinyMCE.init(mceSettings);
        
    }
}

AjexFileManager.init({
    returnTo: 'tinymce',
    skin: 'light'
});
