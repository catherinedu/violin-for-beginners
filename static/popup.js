var display_item  = function(item){
	$(".hover_bkgr_fricc").empty()
	var span = $("<span class='helper'></span>")
	$(".hover_bkgr_fricc").append(span)


	var div = $("<div>")
	var content_div = $("<div class='popupCloseButton'>X</div>")
	$(div).append(content_div)

	
	var img_url = item["image"]
	var img = $("<img src = '"+img_url+"'>")
	$(div).append(img)

	var audio_controls = $("<audio controls>")
	var audio_url = item["audio"]
	var audio_src = $("<source src = '"+audio_url+"' type='audio/mp3'>")
	$(audio_controls).append(audio_src)

	$(div).append(audio_controls)
	$(".hover_bkgr_fricc").append(div)

}

var get_item = function(title){
	for (i = 0; i < data.length; i++){
		var tt  = data[i]["Title"]
		//console.log(tt)
		if(tt == title){
			display_item(data[i])
			break
		}
		
	}

}




$(document).ready(function () {
	$('map').imageMapResize();
	$('img[usemap]').rwdImageMaps();
    $(".trigger_popup_fricc").click(function(){
    	var title = $(this).attr("title")
    	//console.log(title)
 		get_item(title)
       $('.hover_bkgr_fricc').show();
    });
    $('.hover_bkgr_fricc').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
    $('.popupCloseButton').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
});