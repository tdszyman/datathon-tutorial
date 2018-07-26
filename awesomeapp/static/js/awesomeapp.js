$(document).ready(function() {

    // Fill in the HTML example data
    $.get(
    "/api/heatmap?format=html&limit=15",
    function(data) {
    console.log("Got the HTML data");
    console.log(data);
    $("#heatmap-html").html(data);
    }
    );

    // Fill in the JSON example data
    $.get(
    "/api/heatmap?format=json&limit=10",
    function(data) {
    console.log("Got the JSON data");
    console.log(data);
    $("#heatmap-json").html(data);
    }
    );

});