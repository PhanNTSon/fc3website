$(document).ready(function(){
    $(".nav-content-tab").click(function(){
        $("#department-tabs-detail article").hide();
        var target = $(this).data("target");
        $("#"+target).show();
    });
});