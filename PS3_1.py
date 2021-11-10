#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import xarray as xr
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


ds = xr.open_dataset('NOAA_NCDC_ERSST_v3b_SST.nc', engine = 'netcdf4')
ds_region = ds.sel(lon = slice(190, 240), lat = slice(-5, 5))

group_data = ds_region.sst.groupby('time.month')
sst_anom = group_data - group_data.mean(dim = 'time')
sst_anom


# In[16]:


time = pd.date_range(start = '1960-01', periods = 684, freq = 'm')

plt.figure(figsize = (16, 9))
plt.plot(time, sst_anom, color = 'k')
plt.title('SST Anomaly in Nino 3.4 Region (5N-5S, 120-170W)',fontsize = 18)
plt.xlabel('Year', fontsize = 14)
plt.ylabel('Anomaly in Degrees C', fontsize = 14)
plt.ylim(-3, 3)

plt.grid(linestyle = '--', linewidth = 0.3, alpha = 0.5, color = 'k')

plt.hlines(y = 0.5, xmin = time[0], xmax = time[-1], color = 'r', linestyles = '--', lw = 0.5, label = 'EI Nino Threshold')
plt.hlines(y = -0.5, xmin = time[0], xmax = time[-1], color = 'b', linestyles = '--', lw = 0.5, label = 'La Nina Threshold')
plt.hlines(y = 0, xmin = time[0], xmax = time[-1], color = 'k', linestyles = 'solid', lw = 1, label = '3 mth running mean')

plt.legend(loc = 'best', fontsize = 12)

plt.fill_between(time, 0, sst_anom, where = (sst_anom > 0), color = 'r')
plt.fill_between(time, 0, sst_anom, where = (sst_anom < 0), color = 'b')

plt.show()


# In[ ]:




