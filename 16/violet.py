"""
Violet Mission Debrief
"""
from os import environ
from os.path import join, dirname
from re import findall
from dotenv import load_dotenv
from bokeh.io import output_file, show
from bokeh.models import (
    GMapPlot,
    GMapOptions,
    ColumnDataSource,
    Circle,
    Range1d,
    PanTool,
    WheelZoomTool,
    BoxSelectTool,
)

files = lambda x: join(dirname(__file__), x)


def main():
    """
    main function
    """
    load_dotenv()
    with open(files("message_new_pen.txt"), encoding="utf-8") as fil:
        text = fil.read()
    print(text)
    results = findall(r"[\d]+.[\d]+,-[\d]+.[\d]+", text)
    print(results)
    lats = []
    longs = []
    for sul in results:
        lat, long = sul.split(",")
        lats.append(float(lat))
        longs.append(float(long))
    map_options = GMapOptions(lat=0, lng=0, zoom=3)
    plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
    plot.title.text = "Example Plot"
    # plot.api_key = environ["API"]
    plot.api_key = ""
    source = ColumnDataSource(data=dict(lat=lats, lon=longs))
    circle = Circle(
        x="lon", y="lat", size=10, fill_color="red", fill_alpha=0.6, line_color=None
    )
    plot.add_glyph(source, circle)
    plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
    output_file(files("gmap_plot.html"))
    show(plot)


if __name__ == "__main__":
    main()
