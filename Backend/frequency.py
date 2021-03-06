# Learn about API authentication here: https://plot.ly/pandas/getting-started
# Find your api_key here: https://plot.ly/settings/api
# Cufflinks binds plotly to pandas dataframes in IPython notebook. Read more

import plotly.plotly as py
# Learn about API authentication here: https://plot.ly/pandas/getting-started
# Find your api_key here: https://plot.ly/settings/api
# Cufflinks binds plotly to pandas dataframes in IPython notebook. Read more

import plotly.plotly as py
import cufflinks as cf
import pandas as pd

cf.set_config_file(offline=False, world_readable=True, theme='ggplot')


# Create a simple dataframe..
df = cf.datagen.lines(3)

colors = ['red', 'blue', 'black'] # Individual Line Color
dashes = ['solid', 'dash', 'dashdot'] # Individual Line Style
widths = [2, 4, 6] # Individual Line Width

plot_url = df.iplot(kind='scatter', mode='lines', colors=colors, dash=dashes, filename='cufflinks/line-style-and-color')
