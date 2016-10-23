$(function(){
	$('#search').keyup(function() {

		$.ajax({
			type: "POST",
			url: "/books/search/",
			data: {
				'search' : $('#search').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType:'html'
		});
	});
});

function searchSuccess(data, textStatus, jqXHR)
{
	$('#book-search').html(data);
}