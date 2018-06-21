// $(document).ready(function () {
//     $('.likescount').each(function () {
//         $(this).load($(this).data('likes-url'))
//     })
// });

$(document).ready(
    function () {



        $("#category-new-a").click(function () {


            // $("#category-new-modal").popover('show');
            // $("#category-new-modal").show();
            // $("#category-new-content").load(this.href);
            $('*[data-url]').hover(function() {
                var e = $(this);
                e.off('hover');
                $.get(e.data('url'), function(d) {
                    e.popover({
                        content: d
                    }).popover('show');
                });
            });
            return false;
        });

        $(document).on("submit", ".ajaxform", function () {
            $.post(
                $(this).data('url'),
                $(this).serialize()
            );
            return false;
        })

    }
);