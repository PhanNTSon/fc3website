(function ($) {
    $(document).ready(function () {
        $(".nav-content-tab").click(function () {
            $("#department-tabs-detail article").hide();
            var target = $(this).data("target");
            $("#" + target).show();
        });
    });
    // Page loading animation
    $(window).on('load', function () {

        $('#js-preloader').addClass('loaded');

    });
})(window.jQuery);