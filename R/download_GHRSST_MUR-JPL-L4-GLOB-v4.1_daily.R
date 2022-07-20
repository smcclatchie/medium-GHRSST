#####################################################
# download GHRSST, MUR-JPL-L4-GLOB-v4.1 daily
#####################################################

setwd("/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/R")

start_date = paste(Sys.Date()-2, "T12:00:00Z", sep='') # just one day
end_date = paste(Sys.Date()-2, "T12:00:00Z", sep='') # today minus 2 days

 # download a specific date
 # url <- "https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(2022-06-22T09:00:00Z)%5D%5B(-38.0):(-36.0)%5D%5B(173.5):(175.5)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff"   
 
# New Zealand
 url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(-49.0):(-31.0)%5D%5B(160.5):(179.5)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="")  
filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_New_Zealand.nc"
download.file(url, filename)
# end New Zealand

# # New Zealand_Northland
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(-38.5):(-33.0)%5D%5B(171.5):(176.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_New_Zealand_Northland.nc"
# download.file(url, filename)
# # end New Zealand_Northland

# # New Zealand_Taranaki
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(-43.0):(-37.0)%5D%5B(170.5):(175.5)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_New_Zealand_Taranaki.nc"
# download.file(url, filename)
# # end New Zealand_Taranaki

# # New Zealand_East_Cape
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(-42.0):(-35.0)%5D%5B(175.0):(179.5)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_New_Zealand_East_Cape.nc"
# download.file(url, filename)
# # end New Zealand_East_Cape

# # Australia Tasmania
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(-45.0):(-37.0)%5D%5B(143.0):(150.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_Australia_Tasmania.nc"
# download.file(url, filename)
# # end Australia Tasmania

# # Australia NSW Sydney
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(-38.0):(-31.0)%5D%5B(149.0):(155.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_Australia_NSW_Sydney.nc"
# download.file(url, filename)
# # end Australia NSW Sydney

# # Australia QLD Brisbane
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(-32.0):(-20.0)%5D%5B(150.0):(157.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_Australia_QLD_Brisbane.nc"
# download.file(url, filename)
# # end Australia QLD Brisbane

# # Australia QLD central
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(-24.0):(-18.0)%5D%5B(145.0):(152.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_Australia_QLD_central.nc"
# download.file(url, filename)
# # end Australia QLD central

# # Australia QLD northern
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(-20.0):(-10.0)%5D%5B(141.5):(147.5)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_Australia_QLD_northern.nc"
# download.file(url, filename)
# # end Australia QLD northern

# # Baja Sur
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(15.0):(30.0)%5D%5B(-125.0):(-99.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_Baja_Sur.nc"
# download.file(url, filename)
# # end Baja sur

# # Costa Rica
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(5.0):(15.0)%5D%5B(-90.0):(-76.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_Costa_Rica.nc"
# download.file(url, filename)
# # end Costa Rica

# # Peru
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(-21.0):(-1.0)%5D%5B(-85.0):(-70.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_Peru_Cabo_Blanco.nc"
# download.file(url, filename)
# # end Cabo Blanco

# # California
 url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(30.0):(45.0)%5D%5B(-130.0):(-115.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_California.nc"
download.file(url, filename)

# # Southern California Southern California Bight
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(29.0):(37.0)%5D%5B(-130.0):(-115.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_SoCal_SCB.nc"
# download.file(url, filename)

# # Southern California Southern California Bight
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(29.0):(37.0)%5D%5B(-122.0):(-116.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_SoCal_SCB.nc"
# download.file(url, filename)

# # Gulf of Maine
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(33.5):(45.0)%5D%5B(-71.0):(-63.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_Gulf_of_Maine.nc"
# download.file(url, filename)
# # end Gulf of Maine

# # US Central Bight
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(32.5):(42.0)%5D%5B(-78.0):(-67.0)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_US_Central_Bight.nc"
# download.file(url, filename)
# # end US Central Bight

# # Florida
#  url <- paste("https://upwell.pfeg.noaa.gov/erddap/griddap/nasa_jpl_dde5_3be1_897b.nc?analysed_sst%5B(",start_date,"):(",end_date,")%5D%5B(24.0):(35.0)%5D%5B(-86.0):(-75.5)%5D&.draw=surface&.vars=longitude%7Clatitude%7Canalysed_sst&.colorBar=KT_thermal%7CD%7CLinear%7C15%7C18%7C6&.land=over&.bgColor=0xffccccff", sep="") 
# filename <-"/mnt/data/dynamic_data/projects/projects2022/GHRSST_and_anomalies/data/latest_MUR_SST_Florida.nc"
# download.file(url, filename)
# # end Florida
