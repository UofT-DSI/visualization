# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto's Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario's Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  
- For each visualization, describe and justify: 
    > What software did you use to create your data visualization?

    > Who is your intended audience? 
    
    > What information or message are you trying to convey with your visualization? 
    
    > What design principles (substantive, perceptual, aesthetic) did you consider when making your visualization? How did you apply these principles? With what elements of your plots? 
    
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
    
    > How did you ensure that your data visualization is accessible?  
    
    > Who are the individuals and communities who might be impacted by your visualization?  
    
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    
    > What 'underwater labour' contributed to your final data visualization product?


Source data link: https://data.ontario.ca/dataset/online-learning-course-enrolment-totals-by-course 

Visualization 1: K-12 Online learning enrollments sunburst chart in plotly
The online learning enrollment visualization was created using Python, leveraging key libraries including Pandas, NumPy, Plotly, and Scikit-learn to generate interactive HTML visualizations through Plotly's Sunburst chart component. The visualization targets multiple stakeholders in the education sector, including administrators, curriculum planners, school board officials, teachers, department heads, and educational researchers.
The sunburst chart effectively communicates several key aspects of the 2021-2022 online learning enrollments, showcasing the hierarchical structure, relative popularity of subject areas, enrollment distribution across categories, and detailed breakdowns by subject, level, and course type. This comprehensive view enables stakeholders to understand enrollment patterns at both macro and micro levels.
The visualization adheres to robust design principles, balancing data integrity with visual clarity. Data integrity is maintained through complete dataset representation, meaningful hierarchical organization, and contextual enrollment data. The visual design incorporates a colorblind-friendly palette, clear hierarchy, interactive hover functionality, consistent typography, and balanced color scheme, all presented in an appropriate 1000x1000 pixel format.
Reproducibility is ensured through well-documented Python scripts, version-controlled code, fixed random seeds, specified library dependencies, and an automated workflow that produces browser-viewable HTML output. Accessibility features include colorblind-friendly colors, high contrast elements, clear text labels, interactive tooltips, full textual names, and screen reader compatibility through the HTML format.
The visualization impacts various communities differently. Students and parents can make informed course selections, while teachers use it for resource planning. Administrators leverage the data for staffing decisions, curriculum developers for program updates, and policymakers for evidence-based decision-making. It also provides insights for Indigenous communities tracking course enrollment and language communities assessing program support.
Feature selection focused on recent data (2021-2022), presenting a complete hierarchical structure with full subject names, enrollment counts, and percentages. The visualization uses updated terminology while intentionally excluding historical trends and geographic data to maintain clarity and focus. Behind the scenes, significant work went into data cleaning, subject code mapping, hierarchical structuring, color scheme research, accessibility testing, code optimization, terminology updates, technical troubleshooting, data aggregation, and documentation.
The visualization successfully balances comprehensive data presentation with accessibility and reproducibility, providing stakeholders with valuable insights into online learning enrollment patterns. Through careful attention to design principles, user needs, and technical implementation, it serves as an effective tool for understanding and decision-making in the education sector.

![Sunburst Visualization of Course Enrollments](/home/troni/visualization/02_activities/assignments/sunburst.png)

[Click here to view the interactive sunburst visualization](/home/troni/visualization/02_activities/assignments/course_category_improved_sunburst.html)

Visualization 2: High-school online course enrollments by delivery type in tableau
The visualization, created using Tableau Public with Python-preprocessed data, presents a comprehensive view of Ontario's online learning course enrollments. It targets education stakeholders including administrators, curriculum planners, department heads, and school board officials, offering insights into enrollment patterns across different subjects and grade levels. The visualization reveals several critical patterns: Grade 12 shows the highest enrollment across most categories, while English maintains strong enrollment in upper grades with diverse course types. Canadian & World Studies demonstrates significant Grade 10 enrollment, and there's a clear progression pattern showing increasing enrollment from Grade 9 to 12. Academic and University preparation courses dominate most subjects, while specialized areas like Languages and Special Education show minimal enrollment.
The design employs key principles including hierarchical organization (Category → Level → Type), meaningful color coding for course types, consistent scaling (0K-100K), and vertical alignment for easy comparison. Accessibility features include a colorblind-friendly palette, clear text labels, intuitive scales, and comprehensive legends. The visualization maintains readability through distinct category labels and supportive grid lines.
This data representation significantly impacts various educational communities. Students and parents can better understand available course options and common pathways, while teachers gain insight into course demand patterns. Administrators can use this information for resource allocation, and specific communities (Indigenous, ESL, Special Education) can track enrollment patterns in their respective programs. The visualization focuses on essential features including course categories, grade levels (9-12 plus Other), course types, enrollment numbers, and distribution patterns.
The visualization effectively communicates the complex relationships between subject areas, grade levels, and course types in Ontario's online learning system. It shows that while some subjects maintain consistent enrollment across grades, others show distinct patterns at specific grade levels. The dominance of certain course types (Academic, University) suggests a strong college-preparatory focus in online learning. Additionally, the varying enrollment patterns across subjects provide valuable insights for curriculum planning and resource allocation. This comprehensive view helps stakeholders make informed decisions about online education delivery while highlighting areas that might need additional attention or resources.

![Tableau Visualization of Course Enrollments by Grade Level and Type](/home/troni/visualization/02_activities/assignments/tableau.png)

[View the interactive Tableau visualization on Tableau Public](https://public.tableau.com/views/PublichighschoolonlinecourseenrollmentsbydeliverytypeinOntario/Sheet3?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

- This assignment is intentionally open-ended - you are free to create static or dynamic data visualizations, maps, or whatever form of data visualization you think best communicates your information to your audience of choice! 
- Total word count should not exceed **(as a maximum) 1000 words** 
 
### Why am I doing this assignment?:  
- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes: 
* Create and customize data visualizations from start to finish in Python
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story  
- This would be a great project to include in your GitHub Portfolio – put in the effort to make it something worthy of showing prospective employers!

### Rubric:

| Component         | Scoring  | Requirement                                                                 |
|-------------------|----------|-----------------------------------------------------------------------------|
| Data Visualizations | Complete/Incomplete | - Data visualizations are distinct from each other<br>- Data visualizations are clearly identified<br>- Different sources/rationales (text with two images of data, if visualizations are labeled)<br>- High-quality visuals (high resolution and clear data)<br>- Data visualizations follow best practices of accessibility |
| Written Explanations | Complete/Incomplete | - All questions from assignment description are answered for each visualization<br>- Explanations are supported by course content or scholarly sources, where needed |
| Code              | Complete/Incomplete | - All code is included as an appendix with your final submissions<br>- Code is clearly commented and reproducible |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 09/03/2025`
* The branch name for your repo should be: `assignment-4`
* What to submit for this assignment:
    * A folder/directory containing:
        * This file (assignment_3.md)
        * Two data visualizations 
        * Two markdown files for each both visualizations with their written descriptions.
        * Link to your dataset of choice.
        * Complete and commented code as an appendix (for your visualization made with Python, and for the other, if relevant) 
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-3`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
