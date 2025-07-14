# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information
- To test your evaluation skills, locate two public data visualizations online, one good and one bad
  - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like!
- For each visualization (good and bad):
  - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
  ```
  Your answer...
  A) Good Visualization: Gapminder Bubble Chart
  Link: https://public.tableau.com/app/profile/psemeniuk/viz/DashboardBuild-Gapminder/Gapminder
  This is good visualization because:
  ```

The text describes a tool that uses rich multi-dimensional encoding to display historical data, including GDP per capita, life expectancy, bubble size, and color. It uses pre-attentive cues to convey four variables without overwhelming the viewer. The tool also features interactive storytelling, with time sliders and "play" controls allowing users to see trends and outliers dynamically. The tool also has a high data-ink ratio, with clean gridlines, subtle axes, and restrained typography minimizing non-data ink. The tool is accessible and clear, with a colorblind-safe palette distinguishing regions and tooltips presenting exact numbers on hover.

B) Bad visualization: 3D Bar Plot of Virginia Mortality Rates (1940)
Link: https://clauswilke.com/dataviz/no-3d.html

The text highlights several issues with the current 3D bar chart, including misleading perspective, occlusion and clutter, distortion of axis and gridlines, low data-ink ratio, and poor use of space. The added third dimension violates graphical integrity and leads to biased comparisons. The bar charts overlap in 3D space, hiding entire faces of some columns, increasing cognitive load and error rates. The perspective skews the x- and z-axes, making it difficult to align bar tops with gridlines and read exact values. Tick marks are at oblique angles, reducing legibility. The low data-ink ratio and chartjunk add visual noise without conveying new information, detracting from the data itself. Depth encoding consumes large screen real estate while providing no analytic benefit. A simple 2D trellis layout would display the same data more compactly and clearly.

      ```
    - How could this data visualization have been improved?

````
A) Good visualization:
The tool could be improved by adding contextual annotations, providing narrative guides, and ensuring mobile responsiveness. Contextual annotations highlight key historical events, while narrative guides provide a short, static sidebar summary for users less inclined to explore interactively. Finally, the tool should ensure bubble sizes and font scales adjust for small screens to maintain readability on tablets and phones.

B) Bad visualization:
To improve the chart, one could convert to 2D small multiples using a faceted (trellis) bar chart, one panel per demographic group (urban female, urban male, rural female, rural male). Direct value labeling would place labels at the end of each bar for precise values, eliminating reliance on gridlines entirely and speeding up interpretation. Standardizing scales and axes would ensure consistent comparison across groups. Simplifying styling would remove gradients and 3D effects, using a single, high-contrast color for all bars or distinguishing groups with a limited, colorblind-safe palette. Additionally, adding interactive filters or tooltips could enhance exploration without visual clutter. By implementing these improvements, the 3D bar chart can be improved to provide a more accurate and concise representation of data.


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
* Submission Due Date: `23:59 - 30/04/2025`
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
````
