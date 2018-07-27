"use strict";

$(document).ready(function() {

    $.ajax(
        "/api/education",
        {
            data: {
                limit: 0
            },
            method: "GET"
        }
    ).done(r => {
        r = JSON.parse(r);
        console.log(r)
        var data = r.data
        var meta = r.metadata[0]
        var graphs = []

        var graph_data = []
        var colours = ['#333333', '#666666', '#999999', '#cccccc', '#ffffff'];

        for(var i = 0; i <= meta.max_age - meta.min_age; i++){
            graph_data[i] = {
                age: i + meta.min_age
            };
            for(var j = 0; j <= (meta.max_education_num - meta.min_education_num); j++){
                graph_data[i]["education" + j] = 1;
                graph_data[i]["colour" + j] = colours[0];
                graph_data[i]["value" + j] = 0;
            }
        }

        for(var i = 0; i < data.length; i++){
            var normalised = ((data[i].value - meta.min_education_num) - 1) / (meta.max_education_num - meta.min_education_num)
            var colour_ind = Math.floor((normalised * 5) % 5)
            graph_data[Number(data[i].age) - Number(meta.min_age)]["education" + data[i].education_num] = 1;
            graph_data[Number(data[i].age) - Number(meta.min_age)]["colour" + data[i].education_num] = colours[colour_ind];
            graph_data[Number(data[i].age) - Number(meta.min_age)]["value"  + data[i].education_num] = data[i].value;
        }

        console.log(graph_data);

        for(var i = 0; i < meta.max_education_num; i++){
            graphs.push({
                "fillAlphas": 1,
                "lineAlpha": 0,
                "type": "column",
                "colorField": "colour" + i,
                "valueField": "education" + i
            })
        }

        var chart = AmCharts.makeChart("chartDiv", {
            type: "serial",
            dataProvider: graph_data,
            "valueAxes": [{
                "stackType": "regular",
                "axisAlpha": 0.3,
                "gridAlpha": 0,
                "maximum": meta.max_education_num,
                //"minimum": meta.min_education_num
              }],
              "graphs": graphs,
              "columnWidth": 1,
              "categoryField": "age",
              "categoryAxis": {
                "gridPosition": "start",
                "axisAlpha": 0,
                "gridAlpha": 0,
                "position": "left"
              }
        });

    })
});