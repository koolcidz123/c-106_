import plotly.express as px
import csv
import numpy as np

def _get_data_(datapath):
    Size = []
    Time = []
    with open(datapath) as f:
        df = csv.DictReader(f)
        for row in df:
            Size.append(float(row["Size of TV"]))
            Time.append(float(row["Time"]))
    return{"x": Size, "y": Time}

def _find_correlation_(datasource):
    print(datasource)
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print (correlation[0,1])

def _setup():
    datapath = "Size of TVAverage time.csv"
    datasource = _get_data_(datapath)
    _find_correlation_(datasource)


with open("Student Marks vs Days Present.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
    fig.show()

_setup()