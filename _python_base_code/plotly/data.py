# %%
# ? making line graph
from plotly.graph_objs import Scatter
from plotly import offline
#define the data
x_values = list(range(11))
squares = [x**2 for x in x_values]
#pass the data to a graph object, and store it in a list
data = [Scatter(x=x_values, y=squares)]
# data = [Scatter(x=x_values, y=squares, mode='markers')]
#pass the data and a filename to plot()
offline.plot(data, filename='squares.html')
# %%
# ? Making bar graph
from plotly.graph_objs import Bar
from plotly import offline
#define the data
x_values = list(range(11))
squares = [x**2 for x in x_values]
data = [Bar(x=x_values, y=squares)]
#pass data and filename to plot
offline.plot(data, filename='squares.html')
# %%
# ? Using layout objects
from plotly.graph_objs import Scatter, Layout
from plotly import offline
#define the data
x_values = list(range(11))
squares = [x**2 for x in x_values]
#pass the data to a graph object, and store it in a list
data = [Scatter(x=x_values, y=squares)]
title = 'Square Numbers'
x_axis_config = {
    "title" : 'x'
}
y_axis_config ={
    'title' : 'Square of x'
}
my_layout = Layout(title=title, xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({
    'data' : data,
    'layout' : my_layout
}, filename='squares.html')
# %%
# ? data as dictionary
from plotly.graph_objs import Scatter
from plotly import offline
#define the data
x_values = list(range(11))
squares = [x**2 for x in x_values]
#pass the data to a graph object, and store it in a list
data = [{
    'type' : 'scatter',
    'x' : x_values,
    'y' : squares,
    'mode' : 'markers',
}]
offline.plot(data, filename='squares.html')
# %%
# ? squares and cubes
from plotly.graph_objs import Scatter
from plotly import offline
#define the data
x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]
#pass the data to a graph object, and store it in a list
data = [{
            #trace 1 squares
            'type' : 'scatter',
            'x' : x_values,
            'y' : squares,
            'name' : 'Squares',
        },
        {
            #trace 2 cubes
            'type' : 'scatter',
            'x' : x_values,
            'y' : cubes,
            'name' : 'Cubes',
        }
]
offline.plot(data, filename='squares_cubes.html')
# %%
# ? layout as dictionary
from plotly.graph_objs import Scatter
from plotly import offline
#define the data
x_values = list(range(11))
squares = [x**2 for x in x_values]
#pass the data to a graph object, and store it in a list
data = [{
            #trace 1 squares
            'type' : 'scatter',
            'x' : x_values,
            'y' : squares,
            'mode' : 'markers',
            'marker' : {
                'size' : 10,
                'color' : '#6688dd'
            }
        },
]
my_layout = {
            'title' : 'Square Numbers',
            'xaxis' : {
                'title' : 'x',
                'titlefont' : {
                    'family' : 'monospace'
                }
            },
            'yaxis' : {
                'title' : 'Square of x',
                'titlefont' : {
                    'family' : 'monospace'
                }
            }
}
offline.plot({
    'data' : data,
    'layout' : my_layout
}, filename='squares.html')
# %%
# ? using colorscale
from plotly.graph_objs import Scatter
from plotly import offline
#define the data
x_values = list(range(11))
squares = [x**2 for x in x_values]
#pass the data to a graph object, and store it in a list
data = [{
            #trace 1 squares
            'type' : 'scatter',
            'x' : x_values,
            'y' : squares,
            'mode' : 'markers',
            'marker' : {
                'colorscale' : "Viridis",
                'color' : squares,
                'colorbar' : {
                    'title' : 'Value'
                }
            }
        },
]
my_layout = {
            'title' : 'Square Numbers',
            'xaxis' : {
                'title' : 'x',
                'titlefont' : {
                    'family' : 'monospace'
                }
            },
            'yaxis' : {
                'title' : 'Square of x',
                'titlefont' : {
                    'family' : 'monospace'
                }
            }
}
offline.plot({
    'data' : data,
    'layout' : my_layout
}, filename='squares.html')
# %%
# ? Adding subplots to a figure
from plotly.subplots import make_subplots
from plotly.graph_objs import Scatter
from plotly import offline
#define the data
x_values = list(range(11))
squares = [x**2 for x in x_values]
cubes = [x**3 for x in x_values]

fig = make_subplots(rows=1, cols=2, shared_xaxes=True)
#pass the data to a graph object, and store it in a list
data = {
            'type' : 'scatter',
            'x' : x_values,
            'y' : squares,
}
fig.add_trace(data, row=1, col=1)
data = {
            'type' : 'scatter',
            'x' : x_values,
            'y' : squares,
}
fig.add_trace(data, row=1, col=2)

offline.plot(fig, filename='subplots.html')
# %%
# ? Plotting global datasets, scattergeo chart type
from plotly import offline
#Points in (lat, lon) format.
peak_coords = [
    (63.069, -151.0063),
    (60.5671, -140.4055),
    (46.8529, -121.7604)
]
#make matching lists of lats, lons, and labels
lats = [pc[0] for pc in peak_coords]
lons = [pc[1] for pc in peak_coords]
peak_names = ['Denali', 'Mt logan', 'Mt Rainier']
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker' : {
        'size' : 20,
        'color' : '#227722'
    },
    'text' : peak_names
}]
my_layout1 = {
    'title' : 'Selected High Peaks',
    'geo' : {
        'scope' : 'north america',
        'showland' : True,
        'showocean' : True,
        'showlakes' : True,
        'showrivers' : True,
            }
}
offline.plot({
    'data' : data,
    'layout' : my_layout1
}, filename='peaks.html')
# %%
# ? Plotting global datasets, scattergeo chart type
from plotly import offline
#Points in (lat, lon) format.
peak_coords = [
    (54.423459, 18.483281),
    (53.821852, 22.368968),
    (50.399905, 18.893328)
]
#make matching lists of lats, lons, and labels
lats = [pc[0] for pc in peak_coords]
lons = [pc[1] for pc in peak_coords]
peak_names = ['Nike', 'Ełk', 'Radzionków']
data = [{
    'type' : 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker' : {
        'size' : 20,
        'color' : '#227722'
    },
    'text' : peak_names
}]
my_layout1 = {
    'title' : 'Polska',
    'geo' : {
        'scope' : 'europe',
        'showland' : True,
        'showocean' : True,
        'showlakes' : True,
        'showrivers' : True,
        'showlegend' : True,
        
            }
}
offline.plot({
    'data' : data,
    'layout' : my_layout1
}, filename='polska.html')
# %%
