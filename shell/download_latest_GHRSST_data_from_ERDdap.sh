#!/bin/bash
###########################################
# download_latest_GHRSST_data_from_ERDdap.sh
###########################################
# activate the conda environment for python
# NOTE: ~/.bashrc was modified so conda activate will work in a shell script 
conda activate geo_env

##########################################
# Download the latest GHRSST data for each of the regions from ERDDAP. 
# NOTE: Edit the R script to add more regions
##########################################
Rscript "../R/download_GHRSST_MUR-JPL-L4-GLOB-v4.1_daily.R"

##########################################
# Process the downloaded data and draw maps
###########################################
python "/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/python/batch_process_sst_and_plots.py"

##########################################
# Call "at" recursively to reset the job each time the shell script runs. 
# NOTE: before resetting the at commands, use:
# atq | cut -f 1 | xargs atrm# to remove all previous jobs 
# (which can be shown with: at -l)
########################################
at -f "../shell/download_latest_GHRSST_data_from_ERDdap.sh" 12:00 + 24 hours