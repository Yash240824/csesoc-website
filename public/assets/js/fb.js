function dateFromUTC( dateAsString, ymdDelimiter ){
  var pattern = new RegExp( "(\\d{4})" + ymdDelimiter + "(\\d{2})" + ymdDelimiter + "(\\d{2})T(\\d{2}):(\\d{2}):(\\d{2})" );
  var parts = dateAsString.match( pattern );

  return new Date(
      parseInt( parts[1] )
    , parseInt( parts[2], 10 ) - 1
    , parseInt( parts[3], 10 )
    , parseInt( parts[4], 10 )
    , parseInt( parts[5], 10 )
    , parseInt( parts[6], 10 )
    , 0
  );
}

function getFbEvents(){
  access_token = "AAACEdEose0cBALfwVmUTqRd30phFXva5uoylcDRhoESDkgDvnShUYNGqr69dBBZBCZChWRVZBX5SQIZAIGhWBwQoRHdxkhKkI0qfW8mKtgZDZD";
  $.getJSON("https://graph.facebook.com/2509117190/events",
    {
      "access_token": access_token,
      "limit": "3"
    },
    function(group_events) {
       $.each(group_events.data, function(i,item){
         $('#carousel-inner').html('');
         $.getJSON("https://graph.facebook.com/" + item.id,
           {
             "access_token": access_token
           },
           function(event_details){
             var a = dateFromUTC(event_details.start_time,"-");
               
              $('#carousel-inner').append(
              '<div class="item">\n' +
               '<h3>'+ event_details.name +'</h3>' +
                '<img class="pull-left" src="https://graph.facebook.com/'+ item.id + '/picture?type=large" />' +
                 
                 '<h5>When</h5><span>'+ a.toLocaleDateString() + " " + a.toLocaleTimeString() +'</span>' +
                 '<h5>Where</h5><span>'+ event_details.location +'</span>' +
                 '<p>'+ event_details.description.substring(0,200) + '...' +'</p>' +
                 '<p class="pull-right"><a href="#" class="btn btn-primary">Attending</a> <a href="#" class="btn">See more</a></p>' +
              '</div>'
              );
           }
         );
       });
     }
   );
}

