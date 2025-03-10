# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset using your file path
file_path = r'C:\workspaceRezaDSI\visualization\02_activities\assignments\ltep-survey-results-all.csv'
data = pd.read_csv(file_path)

# Check the first few rows to confirm successful loading
print(data.head())

# Extract data for bar chart (adjust column name accordingly)
column_name = 'Province-wide conservation programs are established by the Ontario government.'
response_counts = data[column_name].value_counts()

# Plotting bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=response_counts.values, y=response_counts.index, palette='viridis')
plt.title('Agreement on Conservation Programs', fontsize=16)
plt.xlabel('Number of Responses', fontsize=12)
plt.ylabel('Response Category', fontsize=12)
plt.tight_layout()
plt.savefig('conservation_programs_bar_chart.png', dpi=300)
plt.show()
