#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
plot_SST_map.py
Created on 16 July, 2022

@author: smcc
"""

def plot_map(region):
    #########################################################
    # Import packages:
    #########################################################
    import matplotlib.pyplot as plt
    import matplotlib.ticker as mticker
    from matplotlib.pyplot import tick_params
    # from matplotlib.font_manager import get_fontconfig_fonts
    from datetime import datetime
    import cartopy.crs as ccrs
    import cartopy.feature as cfeature
    import cmocean as cmo
    import numpy as np
    import pandas as pd
    import xarray as xr
    import os 
    from pyproj import transform 

    ########################################################
    # Load data 
    # Open a netCDF data file using xarray
    ########################################################
    f = "latest_MUR_SST_" + region + ".nc"
    datadir = ("/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data")
    d = datadir + "/" + f

    # open netcdf file as an xarray dataset
    ds = xr.open_dataset(d)
    
    # open single variables in the xarray dataset
    sst_3d = ds["analysed_sst"] 
    #reduce dimensions to 2d
    sst = sst_3d.squeeze()

    # Generate figure (set its size (width, height) in inches). 
    fig = plt.figure(figsize=(5, 8))

    ax = plt.subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.coastlines(linewidths=0.5)
    ax.add_feature(cfeature.LAND, facecolor="lightgray")
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.RIVERS)

    # get the min, max for SST, convert to a scalar, and round off
    varmin = sst.min()
    sstmin = int(round(varmin.item(),0))
    varmax = sst.max()
    sstmax = int(round(varmax.item(),0))

    sst_int = int(sstmax - sstmin)
    if sst_int >=6: 
        contour_levels = np.array(range(sstmin,sstmax,2))
    elif sst_int <6:
        contour_levels = np.array(range(sstmin,sstmax,1))

    # Plot data
    pt_sst = sst.plot.contourf(
        ax=ax,
        transform=ccrs.PlateCarree(),
        levels=contour_levels,
        cmap=cmo.cm.ice,
         add_colorbar=False,
        zorder=0, 
        )
    
    # color bar ################
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    cax = inset_axes(ax,
                    width="80%",  # width = 80% of parent_bbox width
                    height="5%",  # height : 5%
                    loc='upper right',
                    )
    # axins1.gridlines(draw_labels=False)
    cbar = plt.colorbar(
        pt_sst,
        cax=cax,
        orientation="horizontal",
        extendrect=True,
    )
    cbar.ax.tick_params(labelsize=7, colors='salmon') 
    # cbar.set_label('SST $^0C$', size='xx-small')

    # test change from drawl_labels = True
    gl = ax.gridlines(
        draw_labels=True,
        dms=True,
        x_inline=False,
        y_inline=False,
        linewidth=0.25,
        color="black",
        alpha=0.25,
    )

    # Manipulate latitude and longitude gridline numbers and spacing
    gl.top_labels = False
    gl.right_labels = False
    if region == "New_Zealand":
        gl.xlocator = mticker.FixedLocator([163, 167, 171, 175, 179])
        gl.ylocator = mticker.FixedLocator([-48, -46, -44, -42, -40, -38, -36, -34, -32])
    elif region == "California":
        gl.xlocator = mticker.FixedLocator([-130, -128, -126, -124, -122, -120, -118, -116])
        gl.ylocator = mticker.FixedLocator([31, 33, 35, 37, 39, 41, 43])

    gl.xlabel_style = {"rotation": 0, "size": 12}
    gl.ylabel_style = {"rotation": 0, "size": 12}

    
    ########################################################
    # Save the plot  
    ########################################################
    # tidy by removing any previous file
    os.system("rm /mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/figures/latest_MUR_SST_"+region+".png")

    plt.savefig(
            "/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/figures/latest_MUR_SST_"+region+".png",
            format="png",
            bbox_inches='tight', 
            pad_inches=0,
            dpi=300
        )
    
  