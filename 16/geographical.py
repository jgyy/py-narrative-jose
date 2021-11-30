"""
Geographical Mapping with Python
"""
from os import environ
from os.path import join, dirname
from csv import reader
from dotenv import load_dotenv
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html
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
    with open(files("countries.csv"), encoding = "ISO-8859-1") as fil:
        file = reader(fil)
        for row in file:
            print(row)
    lats = []
    longs = []
    with open(files("countries.csv"), encoding="ISO-8859-1") as fil:
        file = reader(fil)
        for _, lat, long, _ in list(file)[1:]:
            lats.append(float(lat))
            longs.append(float(long))
    map_options = GMapOptions(lat=0, lng=0, zoom=3)
    plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
    plot.title.text = "Example Plot"
    plot.api_key = environ["API"]
    print(plot.api_key)
    source = ColumnDataSource(data=dict(lat=lats, lon=longs))
    circle = Circle(
        x="lon", y="lat", size=15, fill_color="red", fill_alpha=0.6, line_color=None
    )
    plot.add_glyph(source, circle)
    plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
    output_file(files("gmap_plot.html"))
    show(plot)
    file_html(plot, CDN, "Example Plot File")


if __name__ == "__main__":
    main()
