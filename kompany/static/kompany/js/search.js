<
script >
// Implement realtime search with `keyup` function.

$('#search-input').keyup(function (event) {
    var query = ($("#search-input").val());

    if (query !== '' || query !== ' ') {
        $.ajax({
            type: 'GET',
            url: '{% url 'kompany: search' %}',
            data: {
                'csrfmiddlewaretoken': '{{ csrf_token }}',
                'q': query
            },
            success: function (data) {
                $('#main-results-search').html(data);
            },
            error: function (data) {
                console.log(data);
            }
        });
    }
});

$(document).click(function (event) {
    var $is_inside = $(event.target).closest('#main-results-search').length;

    if (event.target.id === 'search-input' || $is_inside) {
        return 0;
    } else {
        $('#results-search').remove();
    }
});
<
/script>