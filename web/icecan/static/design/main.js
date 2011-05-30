


$(function () {

function displayExtra(event) {
  var t = $(this);
  $('.old:visible').hide();
  var old = t.find('.old');
  old.css('top', -t.height());
  old.css('float', 'left');
  old.show();
}

function toggleUserPanel(event) {
  $('#user > div').slideToggle(100);
  event.stopPropagation();
  return false;
}
  
  $('#user #hide').bind('click', toggleUserPanel);
  
  $('.article').hover(displayExtra);
  
});
