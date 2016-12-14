$(document).ready(function (){
    var brugers;
    var sides;
    var restaurantId = $('#restaurantId').val();

    $.ajax({
        context: $(this),
        url: '/autocomplete/',
        method: "POST",
        data: {
            mealType: "burger",
            restaurantId: restaurantId
        },
        success: function(data) {
        	burgers = data;
        	availableTags = Object.keys(burgers);
        	$( "#burgerName" ).autocomplete({
        		source: availableTags
        	});
        }		
    });

    $.ajax({
        context: $(this),
        url: '/autocomplete/',
        method: "POST",
        data: {
            mealType: "side",
            restaurantId: restaurantId
        },
        success: function(data) {
        	sides = data;
        	availableTags = Object.keys(sides);
        	$( "#sideName" ).autocomplete({
        		source: availableTags
        	});
        }		
    });
});