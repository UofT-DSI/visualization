# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      Example: [Gapminder: Wealth & Health of Nations](https://www.gapminder.org/tools/#$chart-type=bubbles)
      
      This interactive bubble chart by Gapminder effectively communicates the relationship between life expectancy and income per person across countries and over time. According to the principles discussed in the “05_customizing_our_plots” and “09_beyond_matplotlib” slides:
      
      1. Clarity and Simplicity: The visualization uses clear axes, labels, and a legend, making it easy to interpret. The use of color and size encodes additional variables (region and population), as recommended in the slides for encoding multiple variables visually (see Seaborn scatterplot and relplot examples).
      2. Interactivity: Users can filter, animate, and explore the data, which aligns with the benefits of dynamic visualizations discussed in “09_beyond_matplotlib.pdf” (e.g., supporting transparency, engagement, and exploration).
      3. Accessibility: The chart uses distinguishable colors and provides tooltips, supporting accessibility and user engagement, as emphasized in the course materials.
      4. Storytelling: The animation over time helps tell a compelling story about global development, which is a key goal of effective data visualization (see “telling a story” in the assignment rubric).
      
      References: “05_customizing_our_plots.pdf” and “09_beyond_matplotlib.pdf” (course slides)
      ```
      
    - How could this data visualization have been improved?  
      ```
      Example: 3D Pie Chart of Market Share (as seen in many business reports)
      
      A 3D pie chart is often cited as a poor practice in data visualization, and this example demonstrates several issues:
      
      1. Distortion and Misleading Perception: The 3D effect distorts the size of the slices, making it difficult to accurately compare values. This violates the principle of clarity and accurate mapping between data and visual elements (see “semantic mapping” in the slides).
      2. Overuse of Color: Too many similar colors make it hard to distinguish between categories, which is discouraged in both “05_customizing_our_plots” and “09_beyond_matplotlib” (see the discussion on color palettes and accessibility).
      3. Lack of Labels and Legends: Often, 3D pie charts omit clear labels or legends, forcing users to guess what each slice represents, which goes against the best practices for axis labeling and legends.
      4. No Story or Context: The chart does not provide context or highlight key insights, failing to support data-driven storytelling.
      
      References: “05_customizing_our_plots.pdf” and “09_beyond_matplotlib.pdf” (course slides)
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
* Submission Due Date: `23:59 - 01/26/2026`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [x] Create a branch called `assignment-2`.
- [x] Ensure that the repository is public.
- [x] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [x] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
