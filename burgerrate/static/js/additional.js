$('.ui.rating')
  .rating({
    initialRating: 3,
    maxRating: 10,
    interactive: false 
  })
;

$('.ratingBar').progress({
	total: 10,
	showActivity: true,
	label: 'ratio',
	text: {
		ratio: '{value} / {total}'
	}
});

$(document).ready(function (){
	var restaurantId = $('#restaurantId').val();
	$('#burgerName').on('focusout', function() {
		$.ajax({
			context: $(this),
			url: '/spellingHints/',
			method: "POST",
			data: {
				name: $(this).val(),
				mealType: "burger",
				restaurantId: restaurantId
			},
			success: function(data) {
				console.log("yey "+data);
				if (typeof data === "string") {
					console.log("is string");
					console.log($(this));
					var messageBox = $(this).closest(".field").find(".hint"); 
					console.log(messageBox);
					messageBox.find('p').append("<b>"+data)+"</b>";
					messageBox.removeClass('hidden');
				}else{
					console.log(data);
				}
			}
		});
	});
});