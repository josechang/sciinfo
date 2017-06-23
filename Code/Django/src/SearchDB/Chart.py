'''
from django.shortcuts import render
from django.http import HttpResponse

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from fusioncharts import FusionCharts
'''

# The `chart` function is defined to load data from a Python Dictionary. This data will be converted to
# JSON and the chart will be rendered in the browser.

def chart(article_info):
    
    tmp = [0, 0, 0, 0, 0]
    for element in article_info:
        if element[1] >= 0.9:
	    tmp[0] += 1
	if element[1] >= 0.8 and element[1] <= 0.9:
	    tmp[1] += 1
	if element[1] >= 0.7 and element[1] <= 0.8:
	    tmp[2] += 1
	if element[1] >= 0.6 and element[1] <= 0.7:
	    tmp[3] += 1
	if element[1] >= 0.5 and element[1] <= 0.6:
	    tmp[4] += 1


    dataSource = {}
    
    # Chart data is passed to the `dataSource` parameter, as hashes, in the form of
    # key-value pairs.
    dataSource['chart'] = { 
        "caption": "Similarity Score distribution",
        # "subCaption": "Harry's SuperMart",
        "xAxisname": "percentage (%)",
        "yAxisName": "no. of article",
        "numberPrefix": "$",
        "theme": "zune"
        }

    # The `category` dict is defined inside the `categories` array with four key-value pairs
    # that represent the x-axis labels for the four quarters.
    dataSource["categories"] = [{
                "category": [
                    { "label": "90-100" },
                    { "label": "80-90" },
                    { "label": "70-80" },
                    { "label": "60-70" },
                    { "label": "50-60" }
                ]
            }]
    
    # The `data` hash contains four key-value pairs that are the values for the revenue
    # generated in the previous year.

    dataSource["dataset"] = [{
                "data": [
			{ "value": tmp[0] },
                        { "value": tmp[1] },
                        { "value": tmp[2] },
                        { "value": tmp[3] },
                        { "value": tmp[4] }
                    ]
                }    
            ]

    # Create an object for the Multiseries column 2D charts using the FusionCharts class constructor
    mscol2D = FusionCharts("mscolumn2d", "ex1" , "600", "400", "chart-1", "json", dataSource)
    return render(request, 'index.html', {'output': mscol2D.render()})
