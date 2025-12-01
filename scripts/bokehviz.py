#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

import geopandas

gdf = geopandas.read_file("/Users/sidi/Workspace/teaching/sid31-pyds/tdp/src/data/shape/mrt_admbnda_adm1_gov_20200801.shp")

df = pd.read_csv("/Users/sidi/Workspace/teaching/sid31-pyds/tdp/src/data/poverty-dataset.csv", sep=";")

df = df.drop(['moughataa', 'c0_', 'c1_', 'c2_'], axis=1)
df['index_mean'] = df.iloc[:, 1:4].mean(axis=1)
df


# In[ ]:


poverty_by_wilaya = df.groupby(['willaya'])['index_mean'].mean().reset_index(name='index_wilaya').sort_values(by=['index_wilaya'], ascending=False).reset_index(drop=True)
poverty_by_wilaya


# In[ ]:


wilayas_map = {'Hodh ech Chargui':"MR07", 'Hodh el Gharbi':"MR08",'Assaba':"MR02",'Gorgol':"MR05",'Brakna':"MR03",'Trarza':"MR12",'Adrar':"MR01",'Dakhlet Nouadhibou':"MR04",'Tagant':"MR11",'Guidimaka':"MR06",'Tiris Zemmour':"MR13",'Inchiri':"MR09",'Nouakchott':"MR10"}
poverty_by_wilaya['ADM1_PCODE'] =  poverty_by_wilaya.willaya.map(wilayas_map)
poverty_by_wilaya




# In[ ]:


poverty_by_wilaya_geo = gdf.merge(poverty_by_wilaya, on='ADM1_PCODE')
poverty_by_wilaya_geo


# In[ ]:


import matplotlib as mpl
from matplotlib import pyplot as plt

poverty_by_wilaya_geo.plot("index_wilaya", figsize=(15,15), cmap=plt.cm.Reds, legend=True, legend_kwds={"label":"% de poverty"}, vmin=5, vmax=15)




# In[ ]:


import matplotlib as mpl
from matplotlib import pyplot as plt
from bokeh.plotting import figure, show, curdoc
from bokeh.io import output_file
from bokeh.models import ColumnDataSource
from bokeh.colors import named
from bokeh.palettes import Spectral3
from bokeh.models.tools import HoverTool
from bokeh.transform import dodge
from bokeh.palettes import brewer
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool

wi_geojson=GeoJSONDataSource(geojson=poverty_by_wilaya_geo.to_json())

palette = brewer['Reds'][9]
palette = palette[::-1]
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 20)
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500,
                     border_line_color=None,location = (0,0))

p = figure(title="Poverty Index")
p.patches("xs","ys",source=wi_geojson,
          fill_color = {'field' :'index_wilaya', 'transform' : color_mapper}, line_color = 'black', line_width = 1.25)
p.add_layout(color_bar, 'below')
#poverty_by_wilaya_geo.explore()
#show(p)
from bokeh.layouts import column

curdoc().add_root(column(p, p))






