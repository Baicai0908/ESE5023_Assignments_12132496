#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Read the file
ds = xr.open_dataset('sst.mnmean.nc', engine = 'netcdf4')
sst_month = ds.sst.isel(time = -1)

plt.figure(figsize = (10, 5), dpi = 100)

# Create an axes with an basic PlateCarree projection style
ax = plt.axes(projection = ccrs.PlateCarree(central_longitude = 180))
ax.set_global()
ax.coastlines()

# Set xticks and yticks
ax.set_xticks([0, 60, 120, 180, 240, 300, 360], crs = ccrs.PlateCarree())
ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs = ccrs.PlateCarree())
lon_formatter = LongitudeFormatter(zero_direction_label = True)
lat_formatter = LatitudeFormatter()
ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)

# Add feature to the map
ax.add_feature(cfeature.OCEAN, zorder = 0)
ax.add_feature(cfeature.LAND, edgecolor = 'black', facecolor = 'grey', zorder = 1)
ax.add_feature(cfeature.RIVERS, edgecolor = 'blue', zorder = 2)

# Plot the gridlines
ax.gridlines(crs = ccrs.PlateCarree(), linewidth = 0.3, color = 'black', alpha = 0.5)


sst_month.plot.contourf(ax = ax, transform = ccrs.PlateCarree(),cmap = 'magma',add_colorbar = True)

# Set title and x,y labels
ax.set_title('Sea Surface Temperature 2021-10-01', fontsize = 16)
ax.set_xlabel('Longitude', fontsize = 14)
ax.set_ylabel('Latitude', fontsize = 14)


# In[7]:


# Create and define the size of a figure object 
plt.figure(figsize = (10, 5), dpi = 100)

# Set Orthographic projection style
central_lon, central_lat = 114.06, 22.54 # Shenzhen
proj = ccrs.Orthographic(central_lon, central_lat) 

# Create an axes with Orthographic projection style
ax = plt.axes(projection=proj)

# Set a region and plot
extent = [central_lon-10, central_lon+10, central_lat-10, central_lat+10]
ax.set_extent(extent)

# Add features to axes using cartopy.feature (cfeature)
ax.add_feature(cfeature.LAND, edgecolor = 'black', facecolor = 'grey', zorder = 2)
ax.add_feature(cfeature.RIVERS, edgecolor = 'blue', zorder = 3)

# Add features to axes using methods
ax.coastlines(resolution = '10m', linewidth = 0.5)
ax.gridlines()

# Plot the colorbar
sst_month.plot.contourf(ax = ax, transform = ccrs.PlateCarree(),cmap = 'magma',add_colorbar = True)

# Set the title and x,y labels
ax.set_title('Near Shenzhen Sea Surface Temperature 2021-10-01', fontsize = 16)
ax.set_xlabel('Longitude', fontsize = 14)
ax.set_xticks(ticks = np.arange(100, 1, 5))
ax.set_ylabel('Latitude', fontsize = 14)

# Add the annotations
ax.annotate('Xisha', xy = (112.01, 11.2), xytext = (120, -10),
             bbox = dict(boxstyle = 'square', fc = 'green', linewidth = 0.1),
             arrowprops = dict(facecolor = 'black', shrink = 0.01, width = 0.1), 
             fontsize = 12, color = 'white', horizontalalignment = 'center')

