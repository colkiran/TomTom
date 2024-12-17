import geopandas as gpd

import matplotlib.pyplot as plt

in_geojson = r'C:\\Training\\PycharmProjects\\TomTom\\ShapeFiles\\municipality.json'
in_shp = r'C:\\Training\\PycharmProjects\\TomTom\\ShapeFiles\\municipality.shp'


gdf1 = gpd.read_file(in_geojson)
gdf2 = gpd.read_file(in_shp)

# from sqlalchemy import create_engine
# db_connection_url = "postgresql://myusername:mypassword@myhost:5432/mydb"
# con = create_engine(db_connection_url)
# sql = "select geon, highway from roads"
# df = gpd.GeoDataFrame().from_postgis(sql, con)

# import matplotlib.pyplot as pyplot
# df.plot()
# pyplot.show()

# gdf2.plot('DISTRICT')
# gdf2.plot('Province', legend=True)
fig, ax = plt.subplots(1, figsize=(10, 10))
gdf2.plot(ax = ax, column="Province", legend=True, legend_kwds={"loc": 'center left'})
leg = ax.get_legend()
leg.set_bbox_to_anchor((1, 0.5))


gddf2.to_file("C:\\Training\\PycharmProjects\\TomTom\\Output\\out_province.shp")
gdf2.to_file("C:\\Training\\PycharmProjects\\TomTom\\Output\\out_provinceJson.json", driver = 'GeoJSON', encoding="utf-8")

test = gpd.read_file("C:\\Training\\PycharmProjects\\TomTom\\Output\\out_province.shp")
test.plot()
plt.show()
