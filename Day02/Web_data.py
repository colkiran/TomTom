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
            start_index = row["Name"].find('[')
            end_index = row['Name'].find(']')
            # population_data.loc[index, 'District2'] = population_data[index]['Name'][start_index+1 : end_index]
            print(start_index, end_index)
            
            
            
            
            