$(document).ready(function () {
        $("nav a").attr("style", "color: #ffffff; font-size: 20px;");
    });
    $(document).ready(function () {
        $("nav a").hover(
            function () {
                $(this).attr("style", "color: #FFFF00; background-color: #0099FF; font-size: 20px;");
            }, function () {
                $(this).attr("style", "background-color: #0099FF; color: #ffffff;  font-size: 20px;");
            }
        )
    });

    $(".carousel").carousel({
        interval: 5000
    });

     $(document).ready(function () {
        $('#media').carousel({
            pause: true,
            interval: false,
        });
    });

     //Responsive Images for each category
// $(document).ready(function () {
//
//         $("[id=laptop]").each(function () {
//             var width = $(this).prop('naturalWidth');
//             var height = $(this).prop('naturalHeight');
//             $(this).attr("height", height / 8 );
//             $(this).attr("width", width / 6);
//             $(this).css("padding", "10px");
//         })
//     });
// $(document).ready(function () {
//
//         $("[id=mobile]").each(function () {
//             var width = $(this).prop('naturalWidth');
//             var height = $(this).prop('naturalHeight');
//             $(this).attr("height", height / 32);
//             $(this).attr("width", width / 8);
//             $(this).css("padding", "10px");
//         })
//     });