# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 


- For each visualization (good and bad):  
   Q1 - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.

      ```
      My answer...

    

Visualization Source: Heat Map  (source: fileattached https://datavizproject.com)
Classification: BAD Visualization

# Visualization Analysis:
This heat map visualization is classified as BAD based on three key failures that violate fundamental data visualization principles covered in our course materials:

1. Complete Lack of Context – Violates Perceptual Quality
The visualization completely fails the perceptual quality test (file 04) because viewers cannot understand what message the creator is trying to convey. With only generic labels (A-D for columns, 1-9 for rows) and no explanatory information, basic questions remain unanswered: What do the colors represent? What is being measured? What story does this data tell? This creates extremely high cognitive load (file 04) as viewers must expend unnecessary mental effort to decode meaning from an unlabeled grid.

2. Missing Legend and Scale – Violates Substantive Quality
The absence of a color legend or scale violates substantive quality requirements (Slide 01) that demand accurate and honest data presentation. Without a legend, it's impossible to determine what values the colors represent or whether darker colors indicate higher or lower values. The visualization also lacks any data source citation, breaking reproducibility principles (file 03) and undermining trustworthiness.

3. Poor Color Choice – Violates Accessibility Standards
The red-blue color scheme poses serious accessibility problems for colorblind users . The subtle gradations between colors are difficult to distinguish, and the diverging color scheme creates confusion without explanation. This contradicts the course emphasis on creating accessible and equitable visualizations (file 04) and increases unnecessary cognitive load.

      ```
    Q2- How could this data visualization have been improved?  
      ```
      My answer...


# Suggested Improvements:

1. Add Comprehensive Labels and Context

The primary issue with this visualization is a complete lack of context, which prevents the audience from understanding what the data represents. To resolve this, the visualization must be furnished with comprehensive labels. First, a descriptive and informative title should be added at the top to immediately communicate the chart's purpose, such as "Customer Satisfaction Scores Across Service Departments." Second, the current, generic labels on the axes (A-D, 1-9) must be replaced with meaningful category names that describe the actual data dimensions; for instance, columns could be labeled with product names or geographic regions, while rows could indicate time periods or different business units. Third, a color legend is essential to define what the colors represent, showing the scale of values from minimum to maximum and clarifying whether darker shades correspond to higher or lower values. Finally, citing the original data source at the bottom of the visualization is a critical step for establishing credibility, supporting reproducibility, and adhering to ethical data practices, as it allows others to verify the information presented.

2. Implement Accessible Design Choices

The current red-blue color scheme creates a significant accessibility barrier for a substantial portion of the audience, including individuals with color vision deficiencies. To create an equitable visualization, this palette must be replaced with a colorblind-friendly alternative. A perceptually uniform, sequential color scheme like "viridis" (which uses blues, greens, and yellows) is an excellent choice, as it remains distinguishable for people with common forms of colorblindness and prints clearly in grayscale. It is also important to limit the number of distinct color shades to between five and seven, as this reduces cognitive load and makes it easier for viewers to differentiate between value ranges without being overwhelmed. Furthermore, color should not be used as the only way to convey information. To ensure universal access, the visualization should be enhanced by directly adding text labels to display the precise numerical value within each cell, or by incorporating different patterns or symbols to highlight key data points, guaranteeing that the message is clear to all users, regardless of their ability to perceive color.


In conclusion, This heat map fails as an effective data visualization because it lacks the essential elements of context, clarity, and accessibility. It violates core principles of good visualization design by creating high cognitive load, preventing accurate data interpretation, and excluding colorblind users. With the suggested improvements focused on labeling, legend inclusion, and accessible color choices, this visualization could be transformed into an effective tool for data communication. 


      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 10/26/2025`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
