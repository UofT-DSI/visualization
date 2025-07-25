# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```

Good visualization: Charles Joseph Minard’s “Napoleon’s March” (1812–1813 Flow Map)

Why It's Excellent
Minard’s flow map is widely recognized as a paragon of effective data visualization. It depicts six dimensions of data—army size, geography, direction of movement, temperature, time, and position—within a single static graphic. This multifactorial integration allows viewers to understand both the quantitative loss of life and its contextual drivers (e.g., cold, distance) in a cohesive narrative.

Tufte (1983) famously hailed this chart as “probably the best statistical graphic ever drawn,” emphasizing its high data-ink ratio, minimal chartjunk, and intuitive visual metaphor of decay through band shrinkage. Each inch of the graphic is informative, avoiding unnecessary embellishment, aligning with the principle that good graphics maximize data density while maintaining clarity (Tufte, 1983).

Recent scholarship continues to reference Minard’s map as a model for multidimensional representation. Kosara (2016) highlights its narrative power and cognitive efficiency, noting how the flow direction and width changes naturally communicate temporal and quantitative trends. Similarly, Harris (1999) underscores how Minard’s visualization prefigured modern storytelling graphics by effectively embedding quantitative data in a geographic and temporal narrative.

How It Aligns with Core Principles
Cognitive accessibility: The declining band width visually encodes troop loss, immediately intuitive even without deep statistical knowledge (Few, 2009).
Appropriate encoding: Band thickness represents army size, a perceptually efficient use of area encoding for quantitative values (Cleveland & McGill, 1984).
High data density: The chart presents large amounts of information without overwhelming the user—a hallmark of well-constructed complex visuals (Tufte, 1983; Heer et al., 2010).


    - How could this data visualization have been improved?  
Despite its excellence, a few enhancements could increase its accessibility for modern audiences:

Modern geographic context: Including recognizable political borders could help current viewers better orient the map spatially.
Interactive elements: In digital format, adding tooltips with detailed figures, timelines, and sources would enhance engagement and transparency (Segel & Heer, 2010).
Uncertainty display: Minard’s map assumes precise data; however, annotating possible ranges for troop estimates or weather data could increase interpretive fidelity, in line with modern best practices (Hullman et al., 2018).

Bad Visualization: 
A frequently cited bad visualization example involves bar charts that do not begin their y-axis at zero, especially when comparing absolute quantities. A notorious case comes from a Fox News chart (2012), where unemployment data from three months (8.6%, 8.3%, and 8.1%) were plotted on a bar chart with a y-axis starting at 7.8%. Though the differences were minor (0.5%), the bars’ lengths exaggerated the drop by visualizing it as dramatic. Similarly, many corporate or media bar graphs show financial or policy trends by cropping y-axes to highlight a story, often misleadingly.

Why It’s Problematic
Truncating the y-axis on bar charts distorts the visual encoding of quantity. Since bar lengths are interpreted perceptually as proportional to values, cropping the axis falsely amplifies small changes. According to Cleveland and McGill’s (1984) foundational work, length is a strong perceptual cue, and its misuse leads to misinterpretation.

Tufte (1983) described such distortions using the concept of the “lie factor”, defined as the ratio between the effect shown in the graphic and the actual statistical effect. A lie factor significantly >1 (or <1) indicates misleading presentation. Bar charts with truncated axes often violate this standard, displaying visual differences much larger than their numerical counterparts.

Research by Correll and Gleicher (2014) confirmed that truncating bar chart baselines significantly skews user perception, leading viewers to overestimate effect size, even when axes are labeled. This persists despite prior warnings or disclaimers, indicating that people rely heavily on visual heuristics rather than analytical labels.

Violated Principles
Integrity (Tufte, 1983): The chart violates the principle of “graphical integrity”—the representation does not reflect the true magnitude of change.
Appropriate chart selection: Bar charts encode quantities through height or length. If the axis doesn’t start at zero, this proportional encoding becomes unreliable (Few, 2009).
Data-ink ratio and context: Often, truncated charts include extra “design flourishes” (e.g. 3D bars or gradients) that distract and obscure core values (Tufte, 1983; Pandey et al., 2014).
How to Improve It
Start y-axes at zero: When using bar or column charts for absolute quantities, the baseline must begin at zero to preserve proportionality (Cairo, 2016).
Use line charts or dot plots: When depicting small changes or deltas over time, these alternatives convey trend without relying on bar length, avoiding false comparisons (Few, 2009; Wilke, 2019).
Add contextual information: Clear axis labels, reference points, and narrative context help viewers accurately interpret significance (Segel & Heer, 2010).
Highlight percent change separately: When absolute values are close, directly labeling percent change may be more effective than misleading bar differences.



References:
Good example:
Cleveland, W. S., & McGill, R. (1984). Graphical perception: Theory, experimentation, and application to the development of graphical methods. Journal of the American Statistical Association, 79(387), 531–554. https://doi.org/10.2307/2288400
Few, S. (2009). Now You See It: Simple Visualization Techniques for Quantitative Analysis. Analytics Press.
Harris, R. L. (1999). Information Graphics: A Comprehensive Illustrated Reference. Oxford University Press.
Heer, J., Bostock, M., & Ogievetsky, V. (2010). A tour through the visualization zoo. Communications of the ACM, 53(6), 59–67. https://doi.org/10.1145/1743546.1743567
Hullman, J., Resnick, P., & Adar, E. (2018). Hypothetical outcome plots outperform error bars and violin plots for inferences about reliability of variable ordering. PLoS ONE, 13(3), e0193875. https://doi.org/10.1371/journal.pone.0193875
Kosara, R. (2016). An Empire Built on Sand: Reexamining What We Think We Know About Visualization. Computer Graphics and Applications, IEEE, 36(1), 48–57. https://doi.org/10.1109/MCG.2016.2
Segel, E., & Heer, J. (2010). Narrative visualization: Telling stories with data. IEEE Transactions on Visualization and Computer Graphics, 16(6), 1139–1148. https://doi.org/10.1109/TVCG.2010.179
Tufte, E. R. (1983). The Visual Display of Quantitative Information. Graphics Press.

Bad example:
Cairo, A. (2016). The Truthful Art: Data, Charts, and Maps for Communication. New Riders.
Cleveland, W. S., & McGill, R. (1984). Graphical perception: Theory, experimentation, and application to the development of graphical methods. Journal of the American Statistical Association, 79(387), 531–554. https://doi.org/10.2307/2288400
Correll, M., & Gleicher, M. (2014). Error bars considered harmful: Exploring alternate encodings for mean and error. IEEE Transactions on Visualization and Computer Graphics, 20(12), 2142–2151. https://doi.org/10.1109/TVCG.2014.2346298
Few, S. (2009). Now You See It: Simple Visualization Techniques for Quantitative Analysis. Analytics Press.
Pandey, A. V., Manivannan, A., Nov, O., Satterthwaite, M., & Bertini, E. (2014). The persuasive power of data visualization. IEEE Transactions on Visualization and Computer Graphics, 20(12), 2211–2220. https://doi.org/10.1109/TVCG.2014.2346419
Segel, E., & Heer, J. (2010). Narrative visualization: Telling stories with data. IEEE Transactions on Visualization and Computer Graphics, 16(6), 1139–1148. https://doi.org/10.1109/TVCG.2010.179
Tufte, E. R. (1983). The Visual Display of Quantitative Information. Graphics Press.
Wilke, C. O. (2019). Fundamentals of Data Visualization: A Primer on Making Informative and Compelling Figures. O’Reilly Media.



      
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
