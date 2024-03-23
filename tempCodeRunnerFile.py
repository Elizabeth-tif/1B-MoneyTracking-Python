def graph():
    data = [
        {"x": "A", "y": 10},
        {"x": "B", "y": 15},
        {"x": "C", "y": 12},
        {"x": "D", "y": 18},
    ]

    # Create a chart with x-values as prefixes
    chart = asciichartpy.plot(data)

    # Customize the appearance of the chart
    asciichartpy.plot.format(chart, prefix="%s:", width=4, align="right")

graph()