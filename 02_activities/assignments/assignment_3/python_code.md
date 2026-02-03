Python code: 

# Libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Read the data 
crime_data = pd.read_csv('1314-009crime_severity_index_csv_2008-12.csv', skiprows=2, nrows=25, encoding='latin1', names=['Geography', '2008', '2009', '2010', '2011', '2012'])

# Delete the numbers inside the parantheses in the Geography column
crime_data['Geography'] = crime_data['Geography'].str.replace(r'\s*\(.*\)', '', regex=True)

countries = 'Canada'
provinces = ['Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', 'New Brunswick',
             'Quebec', 'Ontario', 'Manitoba', 'Saskatchewan', 'Alberta', 'British Columbia',
             'Yukon', 'Northwest Territories', 'Nunavut']

provinces_crime_data = crime_data[crime_data['Geography'].isin(provinces)]
cities_crime_data = crime_data[~crime_data['Geography'].isin(provinces + [countries])]

## Order the data by 2012 crime severity index
cities_crime_data = cities_crime_data.sort_values(by='2012', ascending=False)

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(cities_crime_data['Geography'], cities_crime_data['2012'], color='tomato')
ax.set_ylabel('Crime Severity Index (2012) in Canadian Cities')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()

# save figure 
plt.savefig('python_visualization.png')

plt.show()