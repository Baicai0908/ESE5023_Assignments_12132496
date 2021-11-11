#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import pandas as pd
import xarray as xr
from matplotlib import pyplot as plt
import nc_time_axis
get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


ds = xr.open_dataset('air temperature anomaly 2012.nc', engine = 'netcdf4')

group_data = ds.air.groupby('time.month')
air_anom = group_data - group_data.mean(dim = 'time')
new_air_anom = air_anom.sel(lon = slice(190, 240), lat = slice(-30, 30))
new_air_anom = new_air_anom.mean(dim = {'lon', 'lat'})
time = pd.date_range(start = '2012-01-01', periods = 366, freq = 'd')
fig,ax = plt.subplots(1, 1, figsize = (8, 5), dpi = 300)

ax.plot(time, new_air_anom, color = 'k')

ax.set_ylabel('Anomaly Degrees C', color = 'k', fontsize = 15)
ax.set_xlabel('Time', color = 'k', fontsize = 15)
ax.set_title("sigma 0.995", fontsize = 20)

ax.grid(linestyle = '--',linewidth = 0.3, alpha = 0.5, color = 'k')

ax.hlines(y = 0.5, xmin = time[0], xmax = time[-1], color = 'b',linestyles = '--',lw = 0.5,label = 'upper 0.5')
ax.hlines(y = -0.5, xmin = time[0], xmax = time[-1], color = 'r',linestyles = '--',lw = 0.5,label = 'lower 0.5')
ax.hlines(y = 0, xmin = time[0], xmax = time[-1], color = 'k', linestyles = 'solid', lw = 1, label = 'normal')

ax.set_ylim(-2, 2)
ax.legend(loc = 'best', fontsize = 12)

ax.fill_between(time, 0, line_air_anom, where = (line_air_anom > 0), color = 'b')
ax.fill_between(time, 0, line_air_anom, where = (line_air_anom < 0), color = 'r')


# In[45]:


fig, axes = plt.subplots(2, 3, figsize = (16, 9), sharex = False, sharey = False, dpi = 400)

ds_air_Nov = ds.air.sel(time = slice('2012-11-01', '2012-11-30'))
ds_air_June = ds.air.sel(time = slice('2012-06-01', '2012-06-30'))
ds_air_luan = ds.air.sel(lon = '116', lat = '31', method = 'nearest')
ds_air_day = ds.air.isel(time = -1)

ds_air_Nov.mean('time').plot(ax = axes[0,0])
ds_air_Nov.max('lon').transpose().plot(ax = axes[0,1])
ds_air_day.plot(ax = axes[0, 2])
ds_air_June.mean('time').plot(ax = axes[1,0], cmap = 'jet')
ds_air_June.min('lon').transpose().plot(ax = axes[1,1], cmap = 'jet', alpha = 1)
ds_air_luan.plot(ax = axes[1, 2], c = 'b')

axes[1,2].grid(linestyle = '-.', linewidth = 1, alpha = 0.3)

axes[0,0].set_title('average temp in Nov 2012', fontsize = 16)
axes[0,1].set_title('Nov 2012 max lon', fontsize = 16)
axes[0,2].set_title('2012-12-31', fontsize = 16)
axes[1,0].set_title('average temp in June 2012', fontsize = 16)
axes[1,1].set_title('June 2012 min lon', fontsize = 16)
axes[1,2].set_title('luan 2012 average temp', fontsize = 16)

plt.tight_layout()


# In[ ]:





# In[ ]:




