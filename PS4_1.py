#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
get_ipython().run_line_magic('matplotlib', 'inline')


# In[54]:


# Read the file and sort
ue = pd.read_csv('usgs_earthquakes.csv')
ue_top50 = ue.sort_values('mag', ascending = False).head(50)

# Create and define the size of a figure object 
plt.figure(figsize = (10, 5), dpi = 100)

# Create an axes with an Robinson projection style
proj = ccrs.Robinson(central_longitude = 180)
ax = plt.axes(projection = proj)

# Use background image as the bottom image
ax.stock_img()

# Set a title 
ax.set_title('Top 50 Earthquakes of 2014')

# Scatter plot 
plt.scatter('longitude', 'latitude', data = ue_top50, c = 'mag', cmap = 'Reds', edgecolors = 'black', linewidth = 1, transform = ccrs.PlateCarree())

# Colorbar plot
plt.colorbar(label = 'magnitude', fraction = 0.02)

