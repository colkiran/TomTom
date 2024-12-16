
import geopandas as gpd
import matplotlib.pyplot as plt

# importing an plotting the cities shape file
cities = gpd.read_file("C:/Geopandas/Shapefiles/belgian_cities.shp")
cities.plot(cmap = 'jet', column='NAME_4', figsize=(10, 10))

# importing area of interest and plotting
AOI = gpd.read_file("C:/Geopandas/Shapefiles/area_of_interest_.shp")
AOI.plot()


# plot both the shape files together
fig, ax = plt.subplots(1)
cities.plot(ax = ax, cmap = 'rainbow', column = 'NAME_4' )
AOI.plot(ax = ax, facecolor = 'yellow')


# intersect both the shapes
cities_in_AOI = gpd.overlay(cities, AOI, how='intersection')
cities_in_AOI.plot(cmap = 'jet', column = 'NAME_4',  figsize = (10, 10))
plt.show()     

# Assigning a new column - Area
cities_in_AOI['Area(km2)'] = cities_in_AOI.area / 1000000
      
# save the geodatafreame into a new shape file .shp
cities_in_AOI.to_file('C:/Geopandas/T  arget/intersected_cities.shp')
