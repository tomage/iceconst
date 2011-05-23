

$(function () {
function toggleUserPanel(event) {
  $('#user > div').slideToggle(100);
  event.stopPropagation();
  return false;
}
  
  $('#user #hide').bind('click', toggleUserPanel);
  
});
