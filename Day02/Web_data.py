import pandas as pd
import geopandas as gpd

import matplotlib.pyplot as plt

# data = pd.read_html("https://www.citypopulation.de/en/nepal/mun/admin/")


# mydata = data[0]
# print(mydata)

# mydata.to_excel("C:\\Training\\PycharmProjects\\TomTom\\Output\\mydata.xlsx")

population_data = pd.read_excel("C:\\Training\\PycharmProjects\\TomTom\\Output\\mydata.xlsx")

population_data = population_data[['Name', 'Status', 'Population Census 2011-06-22']]

population_data.rename(columns = {'Population Census 2011-06-22' : 'Population'}, inplace=True)

population_data = population_data.loc[population_data['Status'] == 'District']


for index, row in population_data.iterrows():
        if "[" and "]" in row['Name']:
            start_index = row['Name'].find("[")
            end_index = row['Name'] .find("]") 
            # print(row['Name'][start_index+1:end_index])
            population_data.loc[index, 'district'] = population_data.loc[index]['Name'][start_index+1:end_index]
        else:
            population_data.loc[index, 'district'] = population_data.loc[index]['Name']
            
population_data = population_data[['Population', 'district']]

# ----------------------------------------------------------------------
# reading data from the shape file
nep_districts = gpd.read_file("C:\\Training\\PycharmProjects\\TomTom\\ShapeFiles\\NPL_adm3.shp")

nep_districts.plot()
plt.show()

# nep_districts = nep_districts[['NAME_3', 'geometry' ]]
# nep_districts.rename(columns = {'NAME_3' : 'district'}, inplace = True)
          
# Reprojection to projected coordinate system
# nep_districts.to_crs(epsg=32645, inplace = True)

population_data.replace('Sindhupalchowk', 'Sindhupalchok', inplace = True)
population_data.replace('Chitwan', 'Chitawan', inplace = True)
population_data.replace('Tehrathum', 'Terhathum', inplace = True)
population_data.replace('Dang Deukhuri', 'Dang', inplace = True)
population_data.replace('Tanahun', 'Tanahu', inplace = True)
population_data.replace('Kapilvastu', 'Kapilbastu', inplace = True)
 

for index, row in nep_districts['district'].iteritems():
    for row in population_data['district'].tolist():
        pass
    else:
        print("The district ", row, "is not in the population_data list")
        
 # create a new column and calculate the area of the districts
nep_districts['area'] = nep_districts.area / 1000000
    
 # do an attribute join
nep_districts = nep_districts.merge(population_data, on = 'district')

# crete a  population destiny column   
nep_disricts['pop_den (people / sq. km) '] = nep_districts['Population'] / nep_districts['area']
 
# plotting 

nep_disticts.plot(column = 'pop_den (people / sq. km)', cmap = 'spectral', legend=True)

newdistrct.plot()    
plt.show()


plt.savefig('Population_destiny_NEPAL.jpg')
