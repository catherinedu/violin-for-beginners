var answers = ['GA', 'DA', 'EB', 'AE']

var correct_num = 0
var id = 0
$(document).ready(function() {
   	$("#click").hide();


    var img = $('#planets'),
        martian = $('#martian');
    img.mapster({
        mapKey: 'alt',
        fillOpacity: 0.8,
        fillColor: 'ff0000',
        stroke: true,
        strokeWeight: 2,
        strokeColor: '00ff00',
        onConfigured: function() {
            img.siblings().css('z-index', 0);
            img.css('z-index', 10);

        }
    });

    martian.css('z-index', 5).draggable({
        drag: function() {
            $(this).css('z-index', 5)
        }
    
    });
    img.droppable({
        drop: function(e, ui) {
            var landing = img.mapster('highlight');
            console.log(landing)
            $(ui.draggable).css('z-index', 20);
            if (landing == answers[id]) {
                //alert("This is the correct position!!!");
                correct_num += 1
                id += 1
                //console.log(correct_num)
                martian.draggable('disable').hide('slow');
                $("#click").show();
                
            } 
            else if (landing) {
                // alert("This is incorrect");
                id +=1 
                martian.draggable('disable').hide('slow');
                $("#click").show();

            }

        }
    });
    console.log(id)

    $("#next").click(function(){
          pageRedirect_2()
      })

    var pageRedirect_2 = function(){
        window.location.href = "/quiz1"
        console.log("clicked")
    }






});