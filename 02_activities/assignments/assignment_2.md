# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
     
     I classify Minard's flow map of Napoleon's 1812 Russian campaign as a strong
      visualization for three reasons.

      First, it achieves an exceptionally high data-ink ratio (Tufte, "The Visual
      Display of Quantitative Information," 1983). Six variables — army size, two
      spatial coordinates (latitude/longitude), direction of travel, location relative
      to dates, and temperature on the retreat — are encoded without decorative
      clutter. Nearly every mark carries information, which is the principle Tufte
      uses to define graphical excellence.

      Second, it uses pre-attentive visual channels effectively. The width of the
      band redundantly encodes the magnitude of the army through position and size,
      two of the most accurate perceptual channels in Cleveland and McGill's (1984)
      ranking of elementary graphical-perception tasks. The collapse of the band from
      ~422,000 to ~10,000 men is legible instantly, before any reading of numbers
      occurs.

      Third, it tells a story (a stated learning outcome). The dark outbound flow and
      the pale returning flow, anchored to a temperature line below, let the viewer
      reconstruct cause and consequence — the catastrophic toll of the winter retreat —
      in a single integrated frame. This narrative integration of space, time, and
      magnitude is why Tufte called it possibly "the best statistical graphic ever
      drawn."

      I classify the Fox News ACA-enrollment bar chart as a poor visualization for three reasons.
      
      First, it violates the proportional-ink / Lie Factor principle (Tufte 1983). The chart compares a March 27 enrollment figure of about 6 million to a target of 7  million, but the 6-million bar is drawn at roughly one-third the height of the 7-million bar. The bars' visual sizes are wildly disproportionate to the values they represent; Tufte's Lie Factor (size of effect shown ÷ size of effect in data) is far from the ideal of 1, manufacturing a sense of failure not present in the numbers.
      
      Second, it manipulates the baseline. The y-axis does not begin at zero. For bar charts, where the encoded quantity is bar length/area, a non-zero baseline distorts the very channel the reader is meant to decode (Cleveland & McGill, 1984, identify length/position judgments as the perceptual basis of bar charts). Truncating that baseline breaks the mapping between data and ink.
      
      Third, it fails the test of integrity and equity. Cairo (*The Functional Art*, 2013; *How Charts Lie*, 2019) argues a chart's first duty is to be truthful and to let readers draw their own conclusions. This graphic instead engineers a predetermined political conclusion, encoding rhetoric rather than data — the opposite of supporting critical, informed consumption.

    - How could this data visualization have been improved?  
     
      Minard's flow map of Napoleon's 1812 Russian campaign:
      First, the graphic relies on a brown/black versus tan colour contrast to
      distinguish the advance from the retreat. This single redundant cue can fail for
      viewers with low vision or in poor reproductions; adding a clear directional
      label or arrowheads on each band, and testing the palette for sufficient
      luminance contrast (WCAG-style guidance), would make the advance/retreat
      distinction non-reliant on a single channel.

      Second, the temperature scale at the bottom is in Réaumur degrees and the
      distances/dates are sparse, demanding prior context most modern readers lack. A
      brief integrated legend converting units (Réaumur to Celsius), and a short title
      caption stating the question being answered, would lower the barrier to entry and
      make the chart self-explanatory for a general audience rather than only for
      readers already familiar with the campaign.



      First, and most fundamentally, the y-axis should start at zero so that bar heights are proportional to the values (Tufte 1983; Cairo 2019). With a zero baseline, 6 million versus 7 million reads as a modest shortfall — roughly 86% of target — rather than a near-total collapse. This single change restores a Lie Factor close to 1 and lets the bars do honest perceptual work.
      
      Second, the chart should add context and accurate labelling to tell the real story. Showing the enrollment trajectory over time (a line or column series across the sign-up period) rather than two isolated snapshots would convey momentum an the late surge, and clear value labels plus a neutral, descriptive title would let the audience interpret the data themselves. Choosing an appropriate chart type for a part-to-whole-against-target comparison — for example a labelled progress bar o bullet chart (Few, *Show Me the Numbers*, 2004) — would communicate "progress toward goal" far more truthfully than two mismatched columns.

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
* Submission Due Date: `23:59 -  2026-06-09`
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
