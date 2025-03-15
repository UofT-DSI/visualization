import pandas as pd
import numpy as np

# Read the dataset
file_path = '/home/troni/visualization/02_activities/assignments/onlinelearnenrolbycrs_1415-2122_en.txt'
data = pd.read_csv(file_path, delimiter='|')

# Replace '<10' with 5 for numerical analysis
data = data.replace('<10', 5)

# Convert year columns to numeric
year_columns = [col for col in data.columns if 'Enrolment Totals' in col]
data[year_columns] = data[year_columns].apply(pd.to_numeric, errors='coerce')

# Extract course subject from course code (first 3 letters)
data['Subject Code'] = data['Course Code'].str[:3]

# Define subject area categories
subject_categories = {
    'Arts': ['ADA', 'ADP', 'ADV', 'AEA', 'ALC', 'AMD', 'AMG', 'AMI', 'AMK', 'AMM', 'AMR', 'AMU', 'AMV', 'ASM', 'ATC', 'AVI', 'AWA', 'AWE', 'AWI', 'AWL', 'AWM', 'AWQ', 'AWR', 'AWS', 'AWT', 'AWU'],
    'Business': ['BAF', 'BAI', 'BAN', 'BAT', 'BBB', 'BBI', 'BDI', 'BDP', 'BDV', 'BMI', 'BMX', 'BOG', 'BOH', 'BTA', 'BTT', 'BTX'],
    'Canadian & World Studies': ['CGC', 'CGD', 'CGF', 'CGG', 'CGR', 'CGT', 'CGU', 'CGW', 'CHA', 'CHC', 'CHE', 'CHF', 'CHG', 'CHI', 'CHM', 'CHT', 'CHV', 'CHW', 'CHY', 'CIA', 'CIC', 'CIE', 'CLN', 'CLU', 'CPC', 'CPW'],
    'Computer Studies': ['ICS', 'TEJ'],
    'Co-operative Education': ['DCO'],
    'English': ['EAB', 'EAC', 'EAE', 'EAL', 'EAN', 'EBT', 'ELD', 'ELS', 'EMS', 'ENG', 'EPS', 'ESL', 'ETS', 'EWC'],
    'French': ['FCC', 'FEF', 'FFM', 'FIF', 'FLC', 'FLO', 'FRA', 'FSF'],
    'Guidance & Career Education': ['GLC', 'GLD', 'GLE', 'GLN', 'GLS', 'GPP', 'GWL'],
    'Health & Physical Education': ['PAD', 'PAF', 'PAI', 'PAL', 'PAQ', 'PAR', 'PLF', 'PPL', 'PPZ', 'PSE', 'PSK'],
    'Interdisciplinary Studies': ['IDC', 'IDP'],
    'Mathematics': ['MAT', 'MBF', 'MCF', 'MCR', 'MCT', 'MCV', 'MDM', 'MEL', 'MFM', 'MHF', 'MPM', 'MTH'],
    'Indigenous Studies': ['NAC', 'NBE', 'NBF', 'NBV', 'NDA', 'NDW'],
    'Science': ['SBI', 'SCH', 'SES', 'SNC', 'SPH', 'SVN'],
    'Social Sciences & Humanities': ['HFA', 'HFC', 'HFL', 'HFN', 'HHD', 'HHG', 'HHS', 'HIF', 'HIP', 'HLS', 'HNB', 'HNC', 'HPC', 'HPD', 'HPW', 'HRE', 'HRF', 'HRT', 'HSB', 'HSC', 'HSE', 'HSG', 'HSP', 'HZB', 'HZT'],
    'Technological Education': ['TCJ', 'TDJ', 'TFC', 'TFJ', 'TFR', 'TFS', 'TFT', 'TGG', 'TGI', 'TGJ', 'TGP', 'TGV', 'THJ', 'TIJ', 'TMJ', 'TMW', 'TOJ', 'TPJ', 'TTJ', 'TWJ', 'TXJ'],
    'Languages': ['LBG', 'LIG', 'LIH', 'LIP', 'LIS', 'LIT', 'LKC', 'LKK', 'LKM', 'LNM', 'LPV', 'LRP', 'LVL', 'LVV', 'LWE', 'LWG', 'LWI', 'LWS', 'LYA'],
    'Special Education': ['KAL', 'KCW', 'KEN', 'KHD', 'KMM', 'KNA', 'KPF', 'KSN', 'KTT']
}

# Create a reverse mapping from subject code to category
subject_to_category = {}
for category, codes in subject_categories.items():
    for code in codes:
        subject_to_category[code] = category

# Add category field to data
data['Category'] = data['Subject Code'].map(subject_to_category)
data['Category'] = data['Category'].fillna('Other')

# Extract course level from course code (4th character)
data['Level Code'] = data['Course Code'].str[3:4]

# Map level codes to descriptive names with simplified categories
level_mapping = {
    '1': 'Grade 9',
    '2': 'Grade 10',
    '3': 'Grade 11',
    '4': 'Grade 12',
    'A': 'Other',  # Changed from Level 1
    'B': 'Other',  # Changed from Level 2
    'C': 'Other',  # Changed from Level 3
    'D': 'Other',  # Changed from Level 4
    'E': 'Other',  # Changed from Level 5
    'F': 'Other',  # Changed from Level 6
    'O': 'Other'   # Changed from Open
}
data['Level'] = data['Level Code'].map(level_mapping).fillna('Other')

# Extract course type from course code (5th character)
data['Type Code'] = data['Course Code'].str[4:5]

# Map type codes to descriptive names
type_mapping = {
    'D': 'Academic',
    'P': 'Applied',
    'O': 'Open',
    'E': 'Workplace',
    'C': 'College',
    'U': 'University',
    'M': 'University/College',
    'L': 'Locally Developed',
    'N': 'Non-Credit'
}
data['Type'] = data['Type Code'].map(type_mapping).fillna('Other')

# Melt the year columns to create a long format suitable for Tableau
melted_data = pd.melt(
    data,
    id_vars=['Course Code', 'Course Name', 'Category', 'Subject Code', 'Level', 'Type'],
    value_vars=year_columns,
    var_name='Academic Year',
    value_name='Enrollment'
)

# Clean up the Academic Year column
melted_data['Academic Year'] = melted_data['Academic Year'].str.extract(r'(\d{4}-\d{4})')

# Save to CSV
output_path = '/home/troni/visualization/02_activities/assignments/tableau_data.csv'
melted_data.to_csv(output_path, index=False)
print(f"Data prepared for Tableau saved to: {output_path}")

# Print some summary statistics
print("\nSummary of the data:")
print(f"Total number of courses: {len(data['Course Code'].unique())}")
print(f"Number of categories: {len(data['Category'].unique())}")
print(f"Years covered: {len(year_columns)}")

# Print enrollment by level for 2021-2022
recent_year = '2021-2022 Online Learning Course Enrolment Totals'
print("\nEnrollment by level for 2021-2022:")
level_enrollments = data.groupby('Level')[recent_year].sum().sort_values(ascending=False)
for level, enrollment in level_enrollments.items():
    if enrollment > 0:
        print(f"{level}: {int(enrollment)}")

print("\nEnrollment by category for 2021-2022:")
category_enrollments = data.groupby('Category')[recent_year].sum().sort_values(ascending=False)
for category, enrollment in category_enrollments.items():
    if enrollment > 0:
        print(f"{category}: {int(enrollment)}") 