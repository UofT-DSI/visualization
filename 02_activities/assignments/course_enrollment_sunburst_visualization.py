import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.colors as colors

# Read the dataset
file_path = '/home/troni/visualization/02_activities/assignments/onlinelearnenrolbycrs_1415-2122_en.txt'
data = pd.read_csv(file_path, delimiter='|')

# Replace '<10' with 5 (midpoint) for numerical analysis
data = data.replace('<10', 5)

# Convert year columns to numeric
year_columns = [col for col in data.columns if 'Enrolment Totals' in col]
data[year_columns] = data[year_columns].apply(pd.to_numeric, errors='coerce')

# Extract course subject from course code (first 3 letters)
data['Subject Code'] = data['Course Code'].str[:3]

# Create a comprehensive mapping of subject codes to full subject names
# This ensures we have complete subject names rather than truncated ones
subject_mapping = {
    # Arts
    'ADA': 'Dramatic Arts',
    'ADP': 'Dance',
    'ADV': 'Visual Arts - Digital Media',
    'AEA': 'Exploring the Arts',
    'ALC': 'Integrated Arts',
    'AMD': 'Media Arts',
    'AMG': 'Guitar Music',
    'AMI': 'Instrumental Music',
    'AMK': 'Keyboard Music',
    'AMM': 'Music and Computers',
    'AMR': 'Repertoire',
    'AMU': 'Music',
    'AMV': 'Vocal Music',
    'ASM': 'Media Studies',
    'ATC': 'Dance',
    'AVI': 'Visual Arts',
    'AWA': 'Arts and Crafts',
    'AWE': 'Visual Arts - Information/Consumer Design',
    'AWI': 'Illustration',
    'AWL': 'Drawing',
    'AWM': 'Visual Arts - Drawing and Painting',
    'AWQ': 'Photography',
    'AWR': 'Film/Video',
    'AWS': 'Digital Media',
    'AWT': 'Visual Arts - Sculpture',
    'AWU': 'Visual Arts - Cultural/Historical Studies',
    
    # Business
    'BAF': 'Financial Accounting',
    'BAI': 'Accounting',
    'BAN': 'Accounting for Non-Accountants',
    'BAT': 'Accounting',
    'BBB': 'International Business',
    'BBI': 'Introduction to Business',
    'BDI': 'Entrepreneurship',
    'BDP': 'Entrepreneurship: Venture Planning',
    'BDV': 'Entrepreneurship: Building a Venture',
    'BMI': 'Marketing',
    'BMX': 'Marketing: Retail and Service',
    'BOG': 'Organizational Studies',
    'BOH': 'Business Leadership',
    'BTA': 'Information Technology Applications in Business',
    'BTT': 'Information and Communication Technology',
    'BTX': 'Information Technology in Business',
    
    # Canadian & World Studies
    'CGC': 'Geography of Canada',
    'CGD': 'Regional Geography',
    'CGF': 'Forces of Nature',
    'CGG': 'Regional Geography',
    'CGR': 'Environment and Resource Management',
    'CGT': 'Geotechnologies in Action',
    'CGU': 'Understanding Canadian Geography',
    'CGW': 'World Issues: A Geographic Analysis',
    'CHA': 'American History',
    'CHC': 'Canadian History',
    'CHE': 'Origins and Citizenship: The History of a Canadian Ethnic Group',
    'CHF': 'French-Canadian History',
    'CHG': 'Genocide and Crimes Against Humanity',
    'CHH': 'World History since 1900: Global and Regional Interactions',
    'CHI': 'Canada: History, Identity, and Culture',
    'CHM': 'Adventures in World History',
    'CHT': 'Twentieth-Century History',
    'CHV': 'Civics and Citizenship',
    'CHW': 'World History to the End of the Fifteenth Century',
    'CHY': 'World History since the Fifteenth Century',
    'CIA': 'Analyzing Current Economic Issues',
    'CIC': 'Making Personal Economic Choices',
    'CIE': 'The Individual and the Economy',
    'CLN': 'Canadian and International Law',
    'CLU': 'Canadian Law',
    'CPC': 'Canadian Politics and Citizenship',
    'CPW': 'Canadian and World Politics',
    
    # Computer Studies
    'ICS': 'Computer Studies',
    'TEJ': 'Computer Technology',
    
    # Co-operative Education
    'DCO': 'Creating Opportunities through Co-op',
    
    # English
    'EAB': 'English as a Second Language, Level 1',
    'EAC': 'English as a Second Language, Level 2',
    'EAE': 'English as a Second Language, Level 3',
    'EAL': 'English as a Second Language, Level 4',
    'EAN': 'English as a Second Language, Level 5',
    'EBT': 'Business and Technological Communication',
    'ELD': 'English Literacy Development',
    'ELS': 'English Literacy Skills',
    'EMS': 'Media Studies',
    'ENG': 'English',
    'EPS': 'Presentation and Speaking Skills',
    'ESL': 'English as a Second Language',
    'ETS': 'Studies in Literature',
    'EWC': 'The Writer\'s Craft',
    
    # French
    'FCC': 'Extended French',
    'FEF': 'Extended French',
    'FFM': 'French for Native Speakers',
    'FIF': 'French Immersion',
    'FLC': 'French Language and Communication',
    'FLO': 'French Language Arts',
    'FRA': 'Français',
    'FSF': 'French as a Second Language',
    
    # Guidance & Career Education
    'GLC': 'Career Studies',
    'GLD': 'Discovering the Workplace',
    'GLE': 'Advanced Learning Strategies',
    'GLN': 'Navigating the Workplace',
    'GLS': 'Learning Strategies',
    'GPP': 'Leadership and Peer Support',
    'GWL': 'Designing Your Future',
    
    # Health & Physical Education
    'PAD': 'Outdoor Activities',
    'PAF': 'Personal and Fitness Activities',
    'PAI': 'Individual and Small Group Activities',
    'PAL': 'Large Group Activities',
    'PAQ': 'Aquatics',
    'PAR': 'Rhythm and Movement',
    'PLF': 'Recreation and Fitness Leadership',
    'PPL': 'Healthy Active Living Education',
    'PPZ': 'Health for Life',
    'PSE': 'Exercise Science',
    'PSK': 'Kinesiology',
    
    # Interdisciplinary Studies
    'IDC': 'Interdisciplinary Studies',
    'IDP': 'Interdisciplinary Studies',
    
    # Mathematics
    'MAT': 'Mathematics',
    'MBF': 'Foundations of Mathematics',
    'MCF': 'Functions and Applications',
    'MCR': 'Functions',
    'MCT': 'Mathematics for College Technology',
    'MCV': 'Calculus and Vectors',
    'MDM': 'Mathematics of Data Management',
    'MEL': 'Mathematics for Work and Everyday Life',
    'MFM': 'Foundations of Mathematics',
    'MHF': 'Advanced Functions',
    'MPM': 'Principles of Mathematics',
    'MTH': 'Mathematics',
    
    # Indigenous Studies (formerly Native Studies)
    'NAC': 'First Nations, Métis, and Inuit Studies',
    'NBE': 'English: Understanding Contemporary First Nations, Métis, and Inuit Voices',
    'NBF': 'French: Understanding Contemporary First Nations, Métis, and Inuit Voices',
    'NBV': 'Expressing Aboriginal Cultures',
    'NDA': 'Contemporary First Nations, Métis, and Inuit Issues and Perspectives',
    'NDW': 'First Nations, Métis, and Inuit Governance in Canada',
    
    # Science
    'SBI': 'Biology',
    'SCH': 'Chemistry',
    'SES': 'Earth and Space Science',
    'SNC': 'Science',
    'SPH': 'Physics',
    'SVN': 'Environmental Science',
    
    # Social Sciences & Humanities
    'HFA': 'Food and Nutrition',
    'HFC': 'Food and Culture',
    'HFL': 'Food and Healthy Living',
    'HFN': 'Food and Nutrition',
    'HHD': 'Dynamics of Human Relationships',
    'HHG': 'Human Growth and Development',
    'HHS': 'Families in Canada',
    'HIF': 'Individual and Family Living',
    'HIP': 'Personal Life Management',
    'HLS': 'Housing and Home Design',
    'HNB': 'The Developing Child',
    'HNC': 'Fashion and Creative Expression',
    'HPC': 'Parenting',
    'HPD': 'Personal and Social Development',
    'HPW': 'Working with Infants and Young Children',
    'HRE': 'Religious Education',
    'HRF': 'Faith and Culture',
    'HRT': 'World Religions and Belief Traditions',
    'HSB': 'Challenge and Change in Society',
    'HSC': 'World Cultures',
    'HSE': 'Equity and Social Justice',
    'HSG': 'Gender Studies',
    'HSP': 'Introduction to Anthropology, Psychology, and Sociology',
    'HZB': 'Philosophy: Questions and Theories',
    'HZT': 'Philosophy',
    
    # Technological Education
    'TCJ': 'Construction Technology',
    'TDJ': 'Technological Design',
    'TFC': 'Hospitality and Tourism',
    'TFJ': 'Hospitality and Tourism',
    'TFR': 'Hospitality and Tourism',
    'TFS': 'Tourism and Travel Planning',
    'TFT': 'Tourism and Travel',
    'TGG': 'Communications Technology: Print and Graphic Communications',
    'TGI': 'Communications Technology: Interactive New Media and Animation',
    'TGJ': 'Communications Technology',
    'TGP': 'Communications Technology: Photography and Digital Imaging',
    'TGV': 'Communications Technology: TV, Video and Movie Production',
    'THJ': 'Green Industries',
    'TIJ': 'Exploring Technologies',
    'TMJ': 'Manufacturing Technology',
    'TMW': 'Manufacturing Technology',
    'TOJ': 'Transportation Technology',
    'TPJ': 'Health Care',
    'TTJ': 'Transportation Technology',
    'TWJ': 'Custom Woodworking',
    'TXJ': 'Hairstyling and Aesthetics',
    
    # International Languages (formerly Languages)
    'LBG': 'Bulgarian',
    'LIG': 'Greek',
    'LIH': 'Hebrew',
    'LIP': 'Polish',
    'LIS': 'Serbian',
    'LIT': 'Italian',
    'LKC': 'Cantonese',
    'LKK': 'Korean',
    'LKM': 'Mandarin',
    'LNM': 'Native Languages',
    'LPV': 'Portuguese',
    'LRP': 'Russian',
    'LVL': 'Latin',
    'LVV': 'Classical Civilization',
    'LWE': 'German',
    'LWG': 'German',
    'LWI': 'Italian',
    'LWJ': 'Japanese',
    'LWS': 'Spanish',
    'LYA': 'Arabic',
    
    # Special Education
    'KAL': 'Special Education - Creative Arts for Enjoyment and Expression',
    'KCW': 'Special Education - Exploring Our World',
    'KEN': 'Special Education - Language and Communication Development',
    'KHD': 'Special Education - Social Skills Development',
    'KMM': 'Special Education - Numeracy and Numbers',
    'KNA': 'Special Education - Personal Health and Fitness',
    'KPF': 'Special Education - Personal Life Skills',
    'KSN': 'Special Education - Exploring Our Environment',
    'KTT': 'Special Education - Computer Skills'
}

# Apply the mapping to create a subject name column
data['Subject'] = data['Subject Code'].map(subject_mapping)

# Fill missing subjects with the code itself
data['Subject'] = data['Subject'].fillna(data['Subject Code'])

# Extract course level from course code (4th character)
data['Level Code'] = data['Course Code'].str[3:4]

# Map level codes to descriptive names
level_mapping = {
    '1': 'Grade 9',
    '2': 'Grade 10',
    '3': 'Grade 11',
    '4': 'Grade 12',
    'A': 'Level 1',
    'B': 'Level 2',
    'C': 'Level 3',
    'D': 'Level 4',
    'E': 'Level 5',
    'F': 'Level 6',
    'O': 'Open'
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

# Calculate total enrollment for the most recent year
recent_year = '2021-2022 Online Learning Course Enrolment Totals'
data['Recent Enrollment'] = data[recent_year].fillna(0)

# Calculate total enrollment for all courses
total_enrollment = data['Recent Enrollment'].sum()
print(f"Total enrollment for all courses (2021-2022): {total_enrollment}")

# Prepare data for the sunburst chart
sunburst_data = []

# Add root node with enrollment count on a separate line
root_label = f"All Courses<br>{int(total_enrollment)} enrollments"
sunburst_data.append({
    'id': 'All Courses',
    'parent': '',
    'value': total_enrollment,
    'label': root_label
})

# Add subject level WITHOUT enrollment counts in the labels
for subject in data['Subject'].dropna().unique():
    subject_enrollment = data[data['Subject'] == subject]['Recent Enrollment'].sum()
    if subject_enrollment > 0:
        # Don't include enrollment count in the subject label
        sunburst_data.append({
            'id': subject,
            'parent': 'All Courses',
            'value': subject_enrollment,
            'label': subject
        })
        
        # Add level within subject
        for level in data[data['Subject'] == subject]['Level'].dropna().unique():
            level_id = f"{subject}-{level}"
            level_enrollment = data[(data['Subject'] == subject) & (data['Level'] == level)]['Recent Enrollment'].sum()
            if level_enrollment > 0:
                sunburst_data.append({
                    'id': level_id,
                    'parent': subject,
                    'value': level_enrollment,
                    'label': level
                })
                
                # Add type within level
                for type_name in data[(data['Subject'] == subject) & (data['Level'] == level)]['Type'].dropna().unique():
                    type_id = f"{level_id}-{type_name}"
                    type_enrollment = data[(data['Subject'] == subject) & 
                                          (data['Level'] == level) & 
                                          (data['Type'] == type_name)]['Recent Enrollment'].sum()
                    if type_enrollment > 0:
                        sunburst_data.append({
                            'id': type_id,
                            'parent': level_id,
                            'value': type_enrollment,
                            'label': type_name
                        })
                        
                        # Add individual courses
                        for _, course in data[(data['Subject'] == subject) & 
                                             (data['Level'] == level) & 
                                             (data['Type'] == type_name)].iterrows():
                            if course['Recent Enrollment'] > 0:
                                course_id = f"{type_id}-{course['Course Code']}"
                                # Include enrollment count on a separate line
                                course_label = f"{course['Course Name']}<br>{int(course['Recent Enrollment'])} enrollments"
                                sunburst_data.append({
                                    'id': course_id,
                                    'parent': type_id,
                                    'value': course['Recent Enrollment'],
                                    'label': course_label
                                })

# Convert to DataFrame
sunburst_df = pd.DataFrame(sunburst_data)

# Create the sunburst chart
fig = go.Figure(go.Sunburst(
    ids=sunburst_df['id'],
    labels=sunburst_df['label'],
    parents=sunburst_df['parent'],
    values=sunburst_df['value'],
    branchvalues='total',
    maxdepth=3,
    insidetextorientation='radial',
    hovertemplate='<b>%{label}</b><br>Enrollments: %{value}<br>Percentage: %{percentRoot:.2%}<extra></extra>',
    # Use a colorblind-friendly discrete color sequence
    marker=dict(
        line=dict(color='white', width=1)  # Add white borders for better contrast
    )
))

# Update layout
fig.update_layout(
    title={
        'text': 'Online Learning Course Enrolment Totals by Course (2021-2022)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    width=1000,
    height=1000,
    margin=dict(t=100, l=0, r=0, b=0)
)

# Save the figure as HTML
output_path = '/home/troni/visualization/02_activities/assignments/course_hierarchy_improved_sunburst.html'
fig.write_html(output_path)
print(f"Improved sunburst chart saved to: {output_path}")

# Create a second version with subject areas grouped by category
print("\nCreating alternative sunburst chart with subject areas grouped by category...")

# Define full category names (instead of abbreviations)
category_full_names = {
    'Arts': 'Arts',
    'Business': 'Business',
    'Canadian & World Studies': 'Canadian & World Studies',
    'Computer Studies': 'Computer Studies',
    'Co-operative Education': 'Co-operative Education',
    'English': 'English',
    'French': 'French',
    'Guidance & Career Education': 'Guidance & Career Education',
    'Health & Physical Education': 'Health & Physical Education',
    'Interdisciplinary Studies': 'Interdisciplinary Studies',
    'Mathematics': 'Mathematics',
    'Native Studies': 'Indigenous Studies',  # Updated to more appropriate term
    'Science': 'Science',
    'Social Sciences & Humanities': 'Social Sciences & Humanities',
    'Technological Education': 'Technological Education',
    'Languages': 'International Languages',  # More descriptive
    'Special Education': 'Special Education',
    'Other': 'Other Courses'  # More descriptive
}

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
    'Native Studies': ['NAC', 'NBE', 'NBF', 'NBV', 'NDA', 'NDW'],
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

# Prepare data for the category-based sunburst chart
category_sunburst_data = []

# Add root node with enrollment count on a separate line
category_sunburst_data.append({
    'id': 'All Courses',
    'parent': '',
    'value': total_enrollment,
    'label': root_label
})

# Define small categories threshold (categories with less than this percentage will get annotations)
small_category_threshold = 2.0  # percentage

# Store small categories for annotations
small_categories = []

# Add category level with percentages instead of enrollment counts
for category in data['Category'].unique():
    category_enrollment = data[data['Category'] == category]['Recent Enrollment'].sum()
    if category_enrollment > 0:
        # Calculate percentage
        percentage = (category_enrollment / total_enrollment) * 100
        
        # Use full category name
        full_category_name = category_full_names.get(category, category)
        
        # Include percentage on a separate line
        category_label = f"{full_category_name}<br>{percentage:.1f}%"
        
        category_sunburst_data.append({
            'id': category,
            'parent': 'All Courses',
            'value': category_enrollment,
            'label': category_label
        })
        
        # Add subject within category WITHOUT enrollment counts
        for subject in data[data['Category'] == category]['Subject'].unique():
            subject_id = f"{category}-{subject}"
            subject_enrollment = data[(data['Category'] == category) & (data['Subject'] == subject)]['Recent Enrollment'].sum()
            if subject_enrollment > 0:
                # Don't include enrollment count in the subject label
                category_sunburst_data.append({
                    'id': subject_id,
                    'parent': category,
                    'value': subject_enrollment,
                    'label': subject
                })
                
                # Add level within subject
                for level in data[(data['Category'] == category) & (data['Subject'] == subject)]['Level'].unique():
                    level_id = f"{subject_id}-{level}"
                    level_enrollment = data[(data['Category'] == category) & 
                                           (data['Subject'] == subject) & 
                                           (data['Level'] == level)]['Recent Enrollment'].sum()
                    if level_enrollment > 0:
                        category_sunburst_data.append({
                            'id': level_id,
                            'parent': subject_id,
                            'value': level_enrollment,
                            'label': level
                        })
                        
                        # Add type within level
                        for type_name in data[(data['Category'] == category) & 
                                             (data['Subject'] == subject) & 
                                             (data['Level'] == level)]['Type'].unique():
                            type_id = f"{level_id}-{type_name}"
                            type_enrollment = data[(data['Category'] == category) & 
                                                  (data['Subject'] == subject) & 
                                                  (data['Level'] == level) & 
                                                  (data['Type'] == type_name)]['Recent Enrollment'].sum()
                            if type_enrollment > 0:
                                category_sunburst_data.append({
                                    'id': type_id,
                                    'parent': level_id,
                                    'value': type_enrollment,
                                    'label': type_name
                                })

# Convert to DataFrame
category_sunburst_df = pd.DataFrame(category_sunburst_data)

# Create the category-based sunburst chart with colorblind-friendly colors
# Using a colorblind-friendly palette based on ColorBrewer's "Set3" palette
colorblind_palette = [
    '#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', 
    '#fdb462', '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd',
    '#ccebc5', '#ffed6f', '#a6cee3', '#1f78b4', '#b2df8a',
    '#33a02c', '#fb9a99', '#e31a1c', '#fdbf6f'
]

category_fig = go.Figure(go.Sunburst(
    ids=category_sunburst_df['id'],
    labels=category_sunburst_df['label'],
    parents=category_sunburst_df['parent'],
    values=category_sunburst_df['value'],
    branchvalues='total',
    maxdepth=3,
    insidetextorientation='radial',
    hovertemplate='<b>%{label}</b><br>Enrollments: %{value}<br>Percentage: %{percentRoot:.2%}<extra></extra>',
    marker=dict(
        line=dict(color='white', width=1)  # Add white borders for better contrast
    )
))

# Manually set colors for each sector to use the colorblind-friendly palette
# This is a workaround since we can't directly set the 'colors' property
category_fig.update_traces(marker_colors=colorblind_palette)

# Update layout without annotations
category_fig.update_layout(
    title={
        'text': 'Online Learning Course Enrolment Totals by Course Category (2021-2022)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    width=1000,
    height=1000,
    margin=dict(t=100, l=0, r=0, b=0)
)

# Save the category-based figure as HTML
category_output_path = '/home/troni/visualization/02_activities/assignments/course_category_improved_sunburst.html'
category_fig.write_html(category_output_path)
print(f"Category-based improved sunburst chart saved to: {category_output_path}")

# Print the enrollment counts and percentages for the first level of groups
print("\nEnrollment counts and percentages for first-level groups:")
print("\nBy Subject:")
subject_enrollments = data.groupby('Subject')['Recent Enrollment'].sum().sort_values(ascending=False)
for subject, enrollment in subject_enrollments.head(10).items():
    if enrollment > 0:
        percentage = (enrollment / total_enrollment) * 100
        print(f"{subject}: {int(enrollment)} enrollments ({percentage:.1f}%)")

print("\nBy Category:")
category_enrollments = data.groupby('Category')['Recent Enrollment'].sum().sort_values(ascending=False)
for category, enrollment in category_enrollments.items():
    if enrollment > 0:
        full_name = category_full_names.get(category, category)
        percentage = (enrollment / total_enrollment) * 100
        print(f"{full_name}: {int(enrollment)} enrollments ({percentage:.1f}%)") 