
var extra_selectors = new Array('.old', '.annotations');

function displayExtra(event) {
  var t = $(this);
  $.each(extra_selectors, function (idx, extra_selector)
    {
      $(extra_selector+':visible').hide();
      var els = t.find(extra_selector);
      els.css('top', -t.height());
      els.show();
    });
}

function toggleUserPanel(event) {
  $('#user > div').slideToggle(100);
  event.stopPropagation();
  return false;
}
  

$(function () {
  $('#user #hide').bind('click', toggleUserPanel);
  $('.article').hover(displayExtra);
});
