$(document).ready(function() {
    $('.global-flash .alert').click(function() {
        $(this).slideUp('fast');
    });
    
    
      // Fix input element click problem
      $('.dropdown input, .dropdown label').click(function(e) {
        e.stopPropagation();
      });
});