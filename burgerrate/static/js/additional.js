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

	$(".ui.button.next").on("click", function(event){
		event.preventDefault();
		var nextPage = $(this).parents(".wizzardpage").next(".wizzardpage");
		$(this).parents(".wizzardpage").addClass("hidden");
		nextPage.removeClass("hidden");
		if (nextPage.attr("id") === "final") {
			$(".step").removeClass("active").addClass("completed");
		}else{
			updateStep(nextPage.data("step"));
		}
	});

	$(".ui.button.previous").on("click", function(event){
		event.preventDefault();
		$(this).parents(".wizzardpage").addClass("hidden");
		$(this).parents(".wizzardpage").prev(".wizzardpage").removeClass("hidden");
		updateStep($(this).parents(".wizzardpage").prev(".wizzardpage").data("step"));
	});

	$(".addrating").on("click", function() {
		location.href=$(this).data("url");
	});
});

function replaceBurger(burgerName) {
	$("#burgerName").val(burgerName);
}

function updateStep(stepId) {
	$(".step").removeClass("active");
	$(".step[data-step='"+stepId+"']").prevAll().addClass("completed");
	$(".step[data-step='"+stepId+"']").removeClass("completed");
	$(".step[data-step='"+stepId+"']").addClass("active");
}