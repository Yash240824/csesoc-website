$(document).ready(function () {
	// Expand about section click handler
	$('#aboutExpand').click(function() {
		$(this).hide();
		$('#aboutLong').slideDown();
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
