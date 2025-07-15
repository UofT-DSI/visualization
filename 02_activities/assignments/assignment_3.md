# Data Visualization

## Assignment 3: Final Project

### Requirements:

- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data.
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/).
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.
- For each visualization, describe and justify:

  > What software did you use to create your data visualization?

  - Python - Jupyter notebook: pandas and matplotlib.
  - I've used the pandas library for data preprocessing and matplotlib for plotting. These tools allowed full control over data manipulation and styling for reproducible, clean visualizations.

  > Who is your intended audience?

  - General public and/or Toronto residents. Especially those who regularly use the ferry service or are planning a visit to Toronto Island Park. City officials or ferry operators may also benefit from identifying peak periods

  > What information or message are you trying to convey with your visualization?

  - For visualization idea #1: I presented line plot of Sales vs Redemption Over Time. It showed how ticket sales and redemptions behave through time (in 15 minutes intervals). It is helpful for ferry operators to optimize schedule and staff, and help passengers kn ow peak travel times to avoid congestion.

  - For visualization idea #2: I presented bar plot of Average Count by Hour. It showed how much ticket being sold per hour. It shows a high level view of daily demand cycles. The plot is useful to identify busy hours, helping city planners and service staff to make informed decisions.

  > What aspects of design did you consider when making your visualization? How did you apply them? With what elements of your plots?

  - Clarity and readability: I used clear font size and labels. Grid lines and tick marks were added to avoid visual clutter.
  - Color choice: I selected distinctive colors to differentiate between sales(blue) and redemptions(orange).
  - Time axis handling: For the line plots, the x-axis uses rotated time stamp for readability across time intervals.
  - Bar spacing: For the bar plots, the spaced bars and grouped value were evenly spaced for easy comparison.

  > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization?
  > The entire process was done in a Jupiter Notebook with all the steps mentioned.

  > How did you ensure that your data visualization is accessible?  
  >  I used high contrast colors and marker shapes for clarity and visibility. The axis labels, legends and titles were all added with appropriate font size and descriptive wording. The plots were saved at high resolution (300 dpi) for readability in different screen size or when printed.

  > Who are the individuals and communities who might be impacted by your visualization?

  - ferry passengers
  - City planners and ferry operators
  - Tourists and event organizers
  - urban researchers or accessibility advocates

- > How did you choose which features of your chosen dataset to include or exclude from your visualization?
  > -There were 4 columns (ID, timestamp, sales count, redemption count). The ID column was excluded as it has the least importance towards the insight.
  > -The focus was placed on the timestamp trends as this best support the goal of understanding temporal usage pattern.

  > What ‘underwater labour’ contributed to your final data visualization product?\

  - Data cleaning and time formatting
  - Plot tuning and iteration
  - Accessability considerations
  - Markdown writing and documentation
  - File management and reproducibility

- This assignment is intentionally open-ended - you are free to create static or dynamic data visualizations, maps, or whatever form of data visualization you think best communicates your information to your audience of choice!
- Total word count should not exceed **(as a maximum) 1000 words**

### Why am I doing this assignment?:

- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes:

* Create and customize data visualizations from start to finish in Python
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

- This would be a great project to include in your GitHub Portfolio – put in the effort to make it something worthy of showing prospective employers!

### Rubric:

| Component            | Scoring             | Requirement                                                                                                                                                                                                                                                                                                                   |
| -------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Data Visualizations  | Complete/Incomplete | - Data visualizations are distinct from each other<br>- Data visualizations are clearly identified<br>- Different sources/rationales (text with two images of data, if visualizations are labeled)<br>- High-quality visuals (high resolution and clear data)<br>- Data visualizations follow best practices of accessibility |
| Written Explanations | Complete/Incomplete | - All questions from assignment description are answered for each visualization<br>- Explanations are supported by course content or scholarly sources, where needed                                                                                                                                                          |
| Code                 | Complete/Incomplete | - All code is included as an appendix with your final submissions<br>- Code is clearly commented and reproducible                                                                                                                                                                                                             |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:

- Submission Due Date: `23:59 - 09/05/2025`
- The branch name for your repo should be: `assignment-3`
- What to submit for this assignment:
  - A folder/directory containing:
    - This file (assignment_3.md)
    - Two data visualizations
    - Two markdown files for each both visualizations with their written descriptions.
    - Link to your dataset of choice.
    - Complete and commented code as an appendix (for your visualization made with Python, and for the other, if relevant)
- What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
  - Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:

- [ ] Create a branch called `assignment-3`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
