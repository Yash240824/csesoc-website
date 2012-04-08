function getFbEvents(){
  access_token = "AAAECJC0TVB4BAD1SU1Hx1UDMMeUr7yZA9CwUMLntC9O0mpT6dKQ7UjpZCDl2Eanatnmelpkgime9ZBBYAkLlUwHhK7MvX1sWtbZATNxIxQZDZD";
  $.getJSON("https://graph.facebook.com/2509117190/events",
    {
      "access_token": access_token,
      "limit": "3"
    },
    function(group_events) {
       $.each(group_events.data, function(i,item){
         $('#upcoming-container').html('');
         $.getJSON("https://graph.facebook.com/" + item.id,
           {
             "access_token": access_token
           },
           function(event_details){
              $('#upcoming-container').append(
              '<div class="span4">' +
               '<div class="thumbnail">' +
                '<img src="https://graph.facebook.com/'+ item.id + '/picture?type=large" alt="">' +
                '<div class="caption">' +
                 '<h3>'+ event_details.name +'</h3>' +
                 '<h5>When</h5><span>'+ event_details.start_time +'</span>' +
                 '<h5>Where</h5><span>'+ event_details.location +'</span>' +
                 '<p><br/><br/>'+ event_details.description.substring(0,100) + '...' +'</p>' +
                 '<p><a href="#" class="btn btn-primary">Attending</a> <a href="#" class="btn">See more</a></p>' +
                '</div>' +
               '</div>' +
              '</div>'
              );
           }
         );
       });
     }
   );
}
