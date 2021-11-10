#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import xarray as xr
from matplotlib import pyplot as plt
import nc_time_axis
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


ds = xr.open_dataset("CERES_EBAF-TOA_200003-201701.nc", engine = 'netcdf4')

fig, axes = plt.subplots(2, 2, figsize = (10, 6), sharex = False, sharey = False, dpi = 400)
ds.toa_lw_all_mon.mean('time').plot(ax = axes[0, 0])
ds.toa_sw_all_mon.mean('time').plot(ax = axes[0, 1])
ds.solar_mon.mean('time').plot(ax = axes[1, 0])
ds.toa_net_all_mon.mean('time').plot(ax = axes[1, 1])

axes[0,0].set_title('TOA longwave', fontsize = 14)
axes[0,1].set_title('TOA shortwave', fontsize = 14)
axes[1,0].set_title('Solar radiation', fontsize = 14)
axes[1,1].set_title('Netflux', fontsize = 14)

plt.tight_layout()


# In[14]:


da_netflux = ds.solar_mon - ds.toa_lw_all_mon - ds.toa_sw_all_mon
da_netflux.mean('time').plot(figsize = (8, 5))
plt.title('Netflux')


# In[23]:


weights = np.cos(np.deg2rad(ds.lat))

weighted_solar = ds.solar_mon.weighted(weights)
weighted_lw = ds.toa_lw_all_mon.weighted(weights)
weighted_sw = ds.toa_sw_all_mon.weighted(weights)

print(weighted_solar.mean(dim = ('lon', 'lat','time')).values)
print(weighted_lw.mean(dim = ('lon', 'lat','time')).values)
print(weighted_sw.mean(dim = ('lon', 'lat','time')).values)


# In[25]:


weighted_net = ds.toa_net_all_mon.weighted(weights)

R = 6371393
pi = np.pi
weighted_lat = 4*pi*R**2*weights/180
total_amount = weighted_net.mean(dim='lon') * weighted_lat
total_amount.transpose().plot(figsize=(8, 5))
plt.title('Net radiation in each 1-degree latitude band', fontsize = 14)
plt.tight_layout()


# In[27]:


cldarea = ds.cldarea_total_daynight_mon.mean(dim='time').values

fig, axes = plt.subplots(2, 2, figsize=(16, 9), dpi = 400)

ds.toa_lw_all_mon.mean(dim='time').where(cldarea >= 75).plot(ax=axes[0, 0])
ds.toa_sw_all_mon.mean(dim='time').where(cldarea >= 75).plot(ax=axes[0, 1])
ds.toa_lw_all_mon.mean(dim='time').where(cldarea <= 25).plot(ax=axes[1, 0])
ds.toa_sw_all_mon.mean(dim='time').where(cldarea <= 25).plot(ax=axes[1, 1])

axes[0, 0].set_title('high cloud area outgoing longwave', fontsize = 14)
axes[0, 1].set_title('high cloud area outgoing shortwave', fontsize = 14)
axes[1, 0].set_title('low cloud area outgoing longwave', fontsize = 14)
axes[1, 1].set_title('low cloud area outgoing shortwave', fontsize = 14)

plt.tight_layout()


# In[28]:


print('high cloud longwave:',np.mean(ds.toa_lw_all_mon.mean(dim='time')))
print('high cloud shortwave:',np.mean(ds.toa_sw_all_mon.mean(dim='time')))
print('low cloud longwave:',np.mean(ds.toa_lw_all_mon.mean(dim='time')))
print('low cloud shortwave:',np.mean(ds.toa_sw_all_mon.mean(dim='time')))

