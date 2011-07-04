
function get_text_id() {
  return document.URL.split('/').reverse()[1];
}

function generate_submodels() {
  $.ajax({
    url: '/admin/main/generate_submodels/',
    method: 'get',
    data: 'text_id='+get_text_id(),
    success: function (data) { alert('Victory! (details: '+data+')'); },
    error: function (data) { alert('Zomg! Error: '+data); },
  });
}

function generate_translations() {
  $.ajax({
    url: '/admin/main/generate_translations/',
    method: 'get',
    data: 'text_id='+get_text_id(),
    success: function (data) { alert('Victory! (details: '+data+')'); },
    error: function (data) { alert('Zomg! Error: '+data); },
  });
}

$(function () {
  
  $('#js_generate_submodels').bind('click', generate_submodels);
  $('#js_generate_translations').bind('click', generate_translations);
  
});
