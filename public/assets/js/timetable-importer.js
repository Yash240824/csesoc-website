var active = 'use-login';

$(document).ready(function() {
  var checkRadioButtons = function() {
    $("input[name='input-type']").each(
      function(index,radio) {
      if (radio.checked) {
        $("#"+radio.value).show("fast");
        active = radio.value;
      } else {
        $("#"+radio.value).hide("fast");
        $("#"+radio.value+" .error").hide();
      }
    }
    )
  };

  checkRadioButtons();
  $("input[name='input-type']").change(checkRadioButtons);

  $('.error').hide();

  $('#source-help').click(
    function() {
    $('#source-help-text').slideToggle();
  }
  );
});

function validate() {
  var good = true;
  if (active == 'use-login') {
    if (! $('#zUser').val() || ! $('#zUser').val()) {
      good = false;
      $("#" + active + ' .error').slideDown();
    }
  } else {
    if (! $('#source').val()) {
      good = false;
      $("#" + active + ' .error').slideDown();
    }
  }
  if (good) {
    if (active == 'use-source') {
      $('#use-login :input').each(function(i, e) { e.value="" });
    }
    $('#importing-timetable-modal').modal({
      keyboard: false,
      backdrop: "static",
    });
    $('#importing-timetable-statusbar').animate({width:'100%'}, 60000, function() {});
  }
  return good;
}
