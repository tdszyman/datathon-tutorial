"use strict";

$(document).ready(function() {

    // Render the heatmap
    $.get(
        "/api/heatmap",
        function(apiData) {
            var data = [{ z: apiData, type: 'heatmap' }];
            var layout = {
                 title: "Level of Education by Age",
                 xaxis: {title: 'Age'},
                 yaxis: {title: 'Level of Education'}
             };
            Plotly.newPlot('heatmap-div', data, layout);
        }
    );

    // Put the table on the page
    $.get(
       "/api/top?num=8",
       function(data) {
           $("#top-div").html(data);
           $("#top-div table").addClass("table-striped");
       }
    );

});