Assignment 3: Toronto 311 Service Requests (2021–2024)

Dataset:
Source: City of Toronto Open Data – 311 Service Requests
Link: https://www.toronto.ca/city-government/data-research-maps/open-data/
Fields used: Creation Date, Service Request Type, Ward

Project Question:
When and where do Toronto residents most frequently request city services, and how can the City prioritize resources seasonally and geographically?

Visualization 1: Python – Seasonal Trends
Tool: Python (Matplotlib)
Output: seasonal_trends_grouped_bar.png
Audience: City operations managers and planners
Message: Shows seasonal demand patterns for the top 5 service request types
Design: Grouped bar chart with clear axis labels and a consistent color palette
Accessibility: Large font sizes, high contrast colors, and legend included

Visualization 2: Python – Heatmaps
Tool: Python (Seaborn)
Output: heatmaps_top5.png
Audience: Analysts looking for seasonal and yearly hotspots
Message: Shows which seasons and years had the highest requests for each type
Design: Annotated cells, logical seasonal order, single color scale
Accessibility: Values shown in each cell to support users with color vision difficulties

Visualization 3: Python – Horizontal Bar Chart
Tool: Python (Matplotlib)
Output: horizontal_bar_overall.png
Audience: Strategic decision makers
Message: Overall share of the top 5 request types
Design: Horizontal bars sorted descending, labeled with counts

Visualization 4: Excel – Ward Level Analysis
Tool: Excel (PivotTables and Clustered Bar Chart)
Output: 311_Excel_Viz.xlsx
Audience: Geographic planners and ward level managers
Message: Shows the top 10 wards generating the most requests, broken down by service type
Design: Clustered bar chart with slicers for year and a matching color palette
Accessibility: Bold labels, sorted bars, clear legend

Reproducibility:
All Python code is in Viz code-1.ipynb
Raw data CSV files are in the data directory
All figures regenerate by running the notebook
Excel workbook (311_Excel_Viz.xlsx) contains the pivot table and chart

Accessibility:
Colorblind friendly palettes used
Direct value annotations on charts
Clear headings, font sizes, and labels

Impacted Communities:
Residents: Data driven prioritization improves response times
City staff: Insights into seasonal and geographic peaks for better planning

Underwater Labour:
Data cleaning and merging from four CSV files
Creating seasonal and yearly fields
Aggregating counts by ward and request type
Iterating through design choices for clarity and accessibility
Husband taking care of kids

Files Included:
Viz code-1.ipynb
SR2021.csv
SR2022.csv
SR2023.csv
SR2024.csv
ward_requests.csv
heatmaps_top5.png
horizontal_bar_overall.png
seasonal_trends_grouped_bar.png
311_ward_vizualisation.png
311_Excel_Viz.xlsx
assignment_3.md
Assignment 3: Toronto 311 Service Reques.md