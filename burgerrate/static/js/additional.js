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

    $('.ui.form')
    .form({
        fields: {
            burgerName : {
                rules: [
                {
                    type: "empty",
                    prompt: "Please enter the name of the burger you had."
                }
                ]
            }
        }
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