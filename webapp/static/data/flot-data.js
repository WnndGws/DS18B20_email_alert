//Flot Multiple Axes Line Chart
$(function() {
    $.getJSON("data.json", function(json){
        var freezerTemp = json.data 
    })
    ;

    function doPlot(position) {
        $.plot($("#flot-line-chart-multi"), [{
            data: freezerTemp,
            label: "Freezer Temperature"
        }
        ], {
            xaxes: [{
                mode: 'time'
            }],
            yaxes: [{
                min: -30
            }, {
                // align if we are to the right
                alignTicksWithAxis: position == "right" ? 1 : null,
                position: position,
            }],
            legend: {
                position: 'sw'
            },
            grid: {
                hoverable: true //IMPORTANT! this is needed for tooltip to work
            },
            tooltip: true,
            tooltipOpts: {
                content: "%s for %x was %y",
                xDateFormat: "%HH:%MM",

                onHover: function(flotItem, $tooltipEl) {
                    // console.log(flotItem, $tooltipEl);
                }
            }

        });
    }

    doPlot("right");

    $("button").click(function() {
        doPlot($(this).text());
    });
});

