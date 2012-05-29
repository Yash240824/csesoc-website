$(document).ready(function() {
    $('.global-flash .alert').click(function() {
        $(this).slideUp('fast');
    });
    
    
      // Fix input element click problem
      $('.dropdown input, .dropdown label, .dropdown-menu').click(function(e) {
        e.stopPropagation();
      });
});