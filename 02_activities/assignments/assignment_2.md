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
##  Good Visualization Example  
**Source**: [Covid-19 Vaccination Dashboard – Tableau Public](https://public.tableau.com/app/profile/shailendhra.venkat/viz/Covid-19VaccinationDashboard_16391002140220/CovidVaccinationDashboard) :contentReference[oaicite:1]{index=1}

### Why I classified this visualization as good:
1. **Appropriate chart selection**  
   It combines maps, bar charts, and line plots to represent different aspects of vaccination data, following the principle of matching visualization types to data types from our lectures.
2. **Clean and accessible layout**  
   With clear headers, legends, and consistent formatting, it supports perceptual clarity and ease of navigation—aligned with information design principles.
3. **Interactive features**  
   Filters and hover tooltips allow users to explore by country, vaccine type, and timeline. This enhances equity and accessibility in data exploration.
4. **Minimal chart junk**  
   The dashboard avoids unnecessary embellishments, maintaining focus on the data—demonstrating good use of data-ink ratio (Tufte, 1983).
5. **Contextual labeling**  
   Captions, axis labels, and legends are all present, helping users understand what is being shown without needing backstory.

## Bad Visualization Example  
**Title**: Angular Gauge Chart – Speedometer Style  
**Source**: [https://medium.com/@e0032148/data-viz-gauge-chart-bdba8ac4fcb9](https://medium.com/@e0032148/data-viz-gauge-chart-bdba8ac4fcb9)
### Why I classified this visualization as bad:
1. **Hard to read precisely**  
   The needle and arc rely on estimating angles, which is perceptually weaker than comparing lengths or positions. Viewers can’t easily gauge small differences (Cleveland & McGill, 1984).
2. **Low data density**  
   The chart only shows one metric without allowing comparisons or trends. It fails to convey meaningful relationships between multiple values or over time.
3. **Visual distortion**  
   The arc length does not proportionally reflect numeric values. For example, 75% often looks more than 1.5x as large as 50%, which visually exaggerates differences.
4. **Inefficient use of space**  
   The circular format takes up significant real estate on a dashboard to display a single value, violating the principle of effective data-ink use.
5. **Emotional bias**  
   The speedometer aesthetic can cause users to overreact to moderate changes—especially when red/yellow color scales are used without justification.

      ```
    
    
    - How could this data visualization have been improved?  
      ```
      Your answer...
## Good Visualization Example
- **Add annotations for events**: Mark key moments (e.g. vaccine approvals) on the time series to build narrative context.
- **Include uncertainty bands**: Show confidence intervals or report delays to communicate data reliability clearly.
- **Improve accessibility**: Use color-blind-safe palettes and provide alt text for screen readers to reach a wider audience.

## Bad Visualization Example 
- Replace with a **bar chart** or **bullet chart** to show the metric linearly.
- Include **exact numeric labels** to remove ambiguity.
- Add **comparative benchmarks** (e.g., targets, thresholds).
- Use **neutral, accessible color schemes**, and avoid red unless the value truly represents danger.
- If multiple metrics are needed, use **small multiples of bars** instead of stacked gauges.

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
* Submission Due Date: `23:59 - 06/07/2025`
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
