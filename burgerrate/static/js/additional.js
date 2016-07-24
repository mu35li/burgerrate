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
				if (typeof data === "string") {
					var messageBox = $(this).closest(".field").find(".hint"); 
					messageBox.find('p').html("Sure you didn't mean <a href='' id='burgerReplaceLink'>"+data+"</button>");
					messageBox.removeClass('hidden');
				}else{
					console.log(data);
				}
			}
		});
	});

	$("body").on("click", "#burgerReplaceLink", function(event){
		event.preventDefault();
		replaceBurger($(this).text());
		$(this).closest(".hint").addClass("hidden");
	});
});

function replaceBurger(burgerName) {
	$("#burgerName").val(burgerName);
}