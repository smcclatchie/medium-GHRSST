# batch_process_sst_and_plots.py
############################################################################
# This script calls other python scripts
# master_mur_sst.py
# plot_SST_map.py
# that define the region, extract the data variables, and then plot them.
# All regions are processed in a loop
############################################################################

# define regions to process
# region_list = ["New_Zealand_Northland","New_Zealand_Taranaki","New_Zealand_East_Cape","Australia_QLD_Brisbane","Australia_QLD_central","Australia_QLD_northern","Australia_NSW_Sydney","Australia_Tasmania","Costa_Rica","Baja_Sur","California","Gulf_of_Maine","US_Central_Bight","Florida"]
# to process one or more only ...
region_list = ["New_Zealand", "California"]

for region in region_list:
    # NOTE: Not needed for straight plotting of netcdf download
    # import master_mur_sst
    # master_mur_sst.sst_by_region(region)

    import plot_SST_map
    plot_SST_map.plot_map(region)

    # No longer needed. Keep for reference
    # import plot_canny_fronts_Sobel_gradients_two_panel
    # plot_canny_fronts_Sobel_gradients_two_panel.plot_canny_fronts_from_latest_canny(region)