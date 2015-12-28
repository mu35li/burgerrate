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