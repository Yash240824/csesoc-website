$(document).ready(function () {
	// Expand about section click handler
	$('#aboutExpand').click(function() {
		$('#aboutLong').slideDown();
		$('#aboutShort').hide();
	});

	// Hide about section click handler
	$('#aboutHide').click(function() {
		$('#aboutLong').slideUp();
		$('#aboutShort').slideDown();
	});

	// Wizard validate
	$("#findClassBtn").click(function () {
		if ($('input[name=year]:checked').length == 0) {
			$('#wizardError').slideDown();
			return false;
		} else if ($('input[name=experience]:checked').length == 0) {
			$('#wizardError').slideDown();
			return false;
		}
	});
});
