import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file('C:\\Training\\PycharmProjects\\TomTom\\ShapeFiles\\world\\world_data_Administrative_Country_Boundaries.shp')
world.plot(figsize = (10, 10))


world[world.country_na  =='Central African Republic'].plot()
world[world.country_na  =='Bhutan'].plot()

africa = world[world.country_na  =='Central African Republic']
africa["area_km2"] = africa.area

africa.plot(column='area_km2', legend=True)

plt.show()