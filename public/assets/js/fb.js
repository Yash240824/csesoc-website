function getFbEvents(){
  access_token = "AAACEdEose0cBAO7y2610rb3OeU6WgVgXcs3LpHrmSvoLGEZCyj8hWrEXQQW7ISySePKCQ4gByXsKjrA9GOqbzqBZBDVeJpB5w4BWZBuOQZDZD";
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
               '<div class="well">' +
               '<h3>'+ event_details.name +'</h3>' +
               '<center>' +
                '<img src="https://graph.facebook.com/'+ item.id + '/picture?type=large" />' +
                '</center>' +
                '<div class="caption">' +
                 
                 '<h5>When</h5><span>'+ event_details.start_time +'</span>' +
                 '<h5>Where</h5><span>'+ event_details.location +'</span>' +
                 '<p>'+ event_details.description.substring(0,100) + '...' +'</p>' +
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

// 
// 
// 
// <div class="span4">
// <div class="well">
//     <h3>CSESoc Poker Night</h3>
//     <center>
//     <img src="https://graph.facebook.com/351244491594507/picture?type=large" />
// </center>
//     
//     <div class="caption">
//         <h5>When</h5><span>2012-04-04T18:30:00</span>
//         <h5>Where</h5><span>CSE Seminar Room, K17</span>
//         <p>Poker night is back! Come join us in a night filled with cards, chips (poker and edible), boardgames...</p>
//         <p><a href="#" class="btn btn-primary">Attending</a>
//              <a href="#" class="btn">See more</a></p>
//     </div>
// </div>
