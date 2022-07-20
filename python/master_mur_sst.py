#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
master_mur_sst.py
Created on Sat June 16 12:25:14 2022

@author: smcc
# NOTE: Need to run this file in my Geo_env environment to gain access to required packages (use ctrl-shift-p 'select interpreter' in VS Code to change environment as necessary). 

"""
import numpy as np
from netCDF4 import Dataset
import xarray as xr
import os

def sst_by_region(region):

    ############################################################################
    ## Extracting the MUR data
    ############################################################################
    # define extract_mur()
    #############################################################################
    def extract_mur():
        if region == "New_Zealand":
            file_name_original = ("latest_MUR_SST_New_Zealand.nc")
        # elif region == "New_Zealand_Northland":
        #     file_name_original = ("latest_MUR_SST_New_Zealand_Northland.nc")
        # elif region == "New_Zealand_Taranaki":
        #     file_name_original = ("latest_MUR_SST_New_Zealand_Taranaki.nc")
        # elif region == "New_Zealand_East_Cape":
        #     file_name_original = ("latest_MUR_SST_New_Zealand_East_Cape.nc")
        # elif region == "Peru":
        #     file_name_original = ("latest_MUR_SST_Peru_Cabo_Blanco.nc")
        # elif region == "Australia_QLD_Brisbane":
        #     file_name_original = ("latest_MUR_SST_Australia_QLD_Brisbane.nc")  
        # elif region == "Australia_QLD_central":
        #     file_name_original = ("latest_MUR_SST_Australia_QLD_central.nc")  
        # elif region == "Australia_QLD_northern":
        #     file_name_original = ("latest_MUR_SST_Australia_QLD_northern.nc") 
        # elif region == "Australia_NSW_Sydney":
        #     file_name_original = ("latest_MUR_SST_Australia_NSW_Sydney.nc") 
        # elif region == "Australia_Tasmania":
        #     file_name_original = ("latest_MUR_SST_Australia_Tasmania.nc")  
        # elif region == "Baja_Sur":
        #     file_name_original = ("latest_MUR_SST_Baja_Sur.nc")  
        # elif region == "Costa_Rica":
            # file_name_original = ("latest_MUR_SST_Costa_Rica.nc")  
        elif region == "California":
            file_name_original = ("latest_MUR_SST_California.nc") 
        # elif region == "SoCal_SCB":
        #     file_name_original = ("latest_MUR_SST_SoCal_SCB.nc") 
        # elif region == "Gulf_of_Maine":
        #     file_name_original = ("latest_MUR_SST_Gulf_of_Maine.nc")
        # elif region == "US_Central_Bight":
        #     file_name_original = ("latest_MUR_SST_US_Central_Bight.nc")  
        # elif region == "Florida":
        #     file_name_original = ("latest_MUR_SST_Florida.nc")  
        file_base = (
            "/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/"
        )
        
        if region == "New_Zealand":
            lat_min = (-49.0,)  # needs to exactly match the ERDDAP lat/lon ranges
            lat_max = (-31.0,)
            lon_min = (160.5,)
            lon_max = (179.5,)
        # elif region == "New_Zealand_Northland":
        #     lat_min = (-38.5,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (-33.0,)
        #     lon_min = (171.5,)
        #     lon_max = (176.0,)
        # elif region == "New_Zealand_Taranaki":
        #     lat_min = (-43.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (-37,)
        #     lon_min = (170.5,)
        #     lon_max = (175.5,)
        # elif region == "New_Zealand_East_Cape":
        #     lat_min = (-42.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (-35.0,)
        #     lon_min = (175.0,)
        #     lon_max = (179.5,)
        # elif region == "Peru":
        #     lat_min = (-21.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (-1.0,)
        #     lon_min = (-85.0,)
        #     lon_max = (-70.0,)
        # elif region == "Australia_QLD_Brisbane":
        #     lat_min = (-32.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (-20.0,)
        #     lon_min = (150.0,)
        #     lon_max = (157.0,)
        # elif region == "Australia_QLD_central":
        #     lat_min = (-24.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (-18.0,)
        #     lon_min = (145.0,)
        #     lon_max = (152.0,)
        # elif region == "Australia_QLD_northern":
        #     lat_min = (-20.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (-10.0,)
        #     lon_min = (141.5,)
        #     lon_max = (147.5,)
        # elif region == "Australia_NSW_Sydney":
        #     lat_min = (-38.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (-31.0,)
        #     lon_min = (149.0,)
        #     lon_max = (155.0,)
        # elif region == "Australia_Tasmania":
        #     lat_min = (-45.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (-37.0,)
        #     lon_min = (143.0,)
        #     lon_max = (150.0,)
        # elif region == "Baja_Sur":
        #     lat_min = (15.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (30.0,)
        #     lon_min = (-125.0,)
        #     lon_max = (-99.0,)
        # elif region == "Costa_Rica":
        #     lat_min = (5.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (15.0,)
        #     lon_min = (-90.0,)
        #     lon_max = (-76.0,)
        elif region == "California":
            lat_min = (30.0,)  # needs to exactly match the ERDDAP lat/lon ranges
            lat_max = (45.0,)
            lon_min = (-130.0,)
            lon_max = (-115.0,)
        # elif region == "SoCal_SCB":
        #     lat_min = (29.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (35.0,)
        #     lon_min = (-122.0,)
        #     lon_max = (-116.0,)
        # elif region == "Gulf_of_Maine":
        #     lat_min = (33.5,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (45.0,)
        #     lon_min = (-71.0,)
        #     lon_max = (-63.0,)
        # elif region == "US_Central_Bight":
        #     lat_min = (32.5,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (42.0,)
        #     lon_min = (-78.0,) 
        #     lon_max = (-67.0,) 
        # elif region == "Florida":
        #     lat_min = (24.0,)  # needs to exactly match the ERDDAP lat/lon ranges
        #     lat_max = (35.0,)
        #     lon_min = (-86.0,) 
        #     lon_max = (-75.5,) 

        nc_file = file_base + file_name_original
        root = Dataset(nc_file)
        lat = root.variables["latitude"][:]
        lon = root.variables["longitude"][:]
        lat_min_index = np.argwhere(lat == lat_min)
        lat_min_index = lat_min_index[0, 0]
        lat_max_index = np.argwhere(lat == lat_max)
        lat_max_index = lat_max_index[0, 0]
        lon_min_index = np.argwhere(lon == lon_min)
        lon_min_index = lon_min_index[0, 0]
        lon_max_index = np.argwhere(lon == lon_max)
        lon_max_index = lon_max_index[0, 0]
        lon_mur = lon[lon_min_index : lon_max_index + 1]
        lat_mur = lat[lat_min_index : lat_max_index + 1]
        sst_mur = root.variables["analysed_sst"][
            0, lat_min_index : lat_max_index + 1, lon_min_index : lon_max_index + 1
        ]
        sst_mur = np.squeeze(sst_mur)
        sst_mur = sst_mur - 273.15
        # smcc edit ###################
        image_time = root.variables["time"][:]
        #############################
        root.close()
        return sst_mur, lon_mur, lat_mur, image_time, file_name_original


    ############################################################################
    # call function extract_mur()
    #############################################################################
    sst_mur, lon_mur, lat_mur, image_time, file_name_original = extract_mur()

    ############################################################################
    # extract relevant components of the date from the SST image (smcc edit)
    #############################################################################
    import time

    t = time.localtime(image_time[0])
    print(t)
    year = t.tm_year
    month = t.tm_mon
    day = t.tm_mday

    ## End Extracting the MUR data

    #############################################################################
    ## Creating an xarray dataset
    
    # define create_xarray_dataset()
    #############################################################################
    def create_xarray_dataset(lat_mur, lon_mur, image_time):

        # create dataset
        # sobel gradient in the x-direction
        ds = xr.Dataset(
            {
                # sst
                "sst": xr.DataArray(
                    data=sst_mur,
                    dims=["Lat", "Lon"],
                    coords={"Lat": lat_mur, "Lon": lon_mur},
                    attrs={"_FillValue": -999.9, "units": "degrees C"},
                ),
                # image_time
                "image_time": xr.DataArray(
                    data=image_time,
                    dims=["Time"],
                    coords={"Time": image_time},
                    attrs={
                        "_FillValue": -999.9,
                        "units": "seconds since 1970-01-01T00:00:00Z",
                    },
                ),
            }
        )

        return ds


    # ###########################################################################
    # # call function create_xarray_dataset()
    # ###########################################################################
    ds = create_xarray_dataset(
        lat_mur, lon_mur, image_time
    )

    #############################################################################
    # write the netCDF file/ smcc addition
    base_dir = (
        "/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/"
    )
    # file_year=year, file_month=month, file_day=day
    c_file_year = str(year)
    c_file_month = str(month).rjust(2, "0")
    c_file_day = str(day).rjust(2, "0")

    # don't regionalize this statement ...
    file_name = base_dir + "SST_" + "latest" + ".nc"
    os.system("rm " + file_name)
    ds.to_netcdf(path=file_name,mode="w")
    ds.close()
