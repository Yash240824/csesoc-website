$(document).ready(function () {
	// Expand about section click handler
	$('#aboutExpand').click(function() {
		$(this).hide();
		$('#aboutLong').slideDown();
	});
});
