#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import xarray as xr
from matplotlib import pyplot as plt
import nc_time_axis
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


ds = xr.open_dataset('air temperature anomaly 2012.nc', engine = 'netcdf4')

group_data = ds.air.groupby('time.month')
air_anom = group_data - group_data.mean(dim = 'time')
line_air_anom = air_anom.mean(dim = {'lat','lon'})

time = pd.date_range(start = '2012-01-01', periods = 366, freq = 'd')
fig,ax = plt.subplots(1,1,figsize = [10, 6], dpi=300)

ax.plot(time, line_air_anom, color = 'k')

ax.set_ylabel('Anomaly Degrees C', color = 'k', fontsize = 15)
ax.set_xlabel('Time', color = 'k', fontsize = 15)
ax.set_title("2012 air temperature anomalies on the 0.995 sigma level", fontsize = 20)

ax.grid(linestyle = '--',linewidth = 0.3, alpha = 0.5, color = 'k')

ax.hlines(y = line_air_anom.max(), xmin = time[0], xmax = time[-1], color = 'b',linestyles = '--',lw = 0.5,label = 'Anomaly MAX positive value')
ax.hlines(y = line_air_anom.min(), xmin = time[0], xmax = time[-1], color = 'r',linestyles = '--',lw = 0.5,label = 'Anomaly MAX negative value')
ax.hlines(y = 0, xmin = time[0], xmax = time[-1], color = 'k', linestyles = 'solid', lw = 1, label = 'anomalies = 0')

ax.set_ylim(-2, 2)
ax.legend(loc = 'best', fontsize=12)

ax.fill_between(time, 0, line_air_anom, where = (line_air_anom > 0), color = 'b')
ax.fill_between(time, 0, line_air_anom, where = (line_air_anom < 0), color = 'r')


# In[4]:


fig, axes = plt.subplots(2, 3, figsize = (12,6), sharex = False, sharey = False, dpi = 400)
da_air = ds.air
da_air_Dec = ds.air.sel(time = slice('2012-12-01', '2012-12-31'))
da_air_Jul = ds.air.sel(time = slice('2012-07-01', '2012-07-31'))
da_air_shenzhen = ds.air.sel(lon = '114', lat = '22.5', method = 'nearest')
da_air_Ant = ds.air.sel(lat = '-90', method = 'nearest')

da_air_Dec.mean('time').plot(ax = axes[0,0])
da_air_Jul.mean('time').plot(ax = axes[1,0], cmap = 'rainbow')
da_air_Dec.mean('lon').transpose().plot(ax = axes[0,1])
da_air_Jul.mean('lon').transpose().plot(ax = axes[1,1], cmap = 'rainbow')
da_air_shenzhen.plot(ax = axes[1, 2], c = 'r')
da_air_Ant.mean('lon').plot(ax = axes[0, 2])

axes[0,2].grid(linestyle = '--', linewidth = 0.5, alpha = 0.5)
axes[1,2].grid(linestyle = '--', linewidth = 0.5, alpha = 0.5)

axes[0,0].set_title('Mean temperature in Dec 2012 (K)',fontsize = 14)
axes[1,0].set_title('Mean temperature in Jul 2012 (K)',fontsize = 14)
axes[0,1].set_title('Temperature in Dec 2012 mean lon (K)', fontsize = 14)
axes[1,1].set_title('Temperature in Jul 2012 mean lon (K)', fontsize = 14)
axes[1,2].set_title('Mean temperature in ShenZhen 2012 (K)', fontsize = 14)
axes[0,2].set_title('Mean temperature in Antarctica 2012 (K)', fontsize = 14)

plt.tight_layout()

