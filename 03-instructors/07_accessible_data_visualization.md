---
marp: true
theme: dsi-certificates-theme
_class: invert
paginate: true
---

# Data Visualization: Visualization with Purpose - Accessible Data Visualization

```code
$ echo "Data Science Institute"
```
---

# Today, we will...

- Discuss the real-world impacts of inaccessible data visualization
- Explore practical tips and resources that we can use to improve the accessibility of our data visualizations, especially relating to:
    - Colour
    - Text
    - Image Descriptions
    - Getting our visualizations to the intended audiences

---

# Case Study: Who gets to use data visualizations?

---

# ‘The Daily Routines of Famous Creative People’ Visualization

![w:700](./images/the_daily_routines_of_famous_creative_people.png)

[🔗 source](https://podio.com/site/creative-routines)

<!--
REFERENCES:
Currey, M. (2013). The Daily Routines of Famous Creative People—Citrix Podio. Podio.Com. https://www.podio.com/creative-routines 

-->

---

# ‘The Daily Routines of Famous Creative People’ Visualization

- The ‘Daily Routines’ plot is often used as an example of ‘good’ data visualization
- It includes its data source (substantive qualities), uses an appropriate plot type for comparison (perceptual qualities), and limits its colour scheme (aesthetic qualities)

![bg right:50% w:500](./images/the_daily_routines_of_famous_creative_people.png)

<!--
REFERENCES:
Currey, M. (2013). The Daily Routines of Famous Creative People—Citrix Podio. Podio.Com. https://www.podio.com/creative-routines 


-->

---

# Questioning assumptions

- Sarah L. Fossheim, a developer and designer,  [was curious](https://fossheim.io/writing/posts/accessible-dataviz-design/)  about how the visualization would be perceived by people with  deuteranopia  (a type of red-green colourblindness) and  achromatopsia  (partial or total lack of colour vision)

![bg right:50% w:500](./images/the_daily_routines_of_famous_creative_people.png)

<!--
REFERENCES:
Currey, M. (2013). The Daily Routines of Famous Creative People—Citrix Podio. Podio.Com. https://www.podio.com/creative-routines 
Sarah Fossheim (they/them) site https://fossheim.io/ 
Fossheim, S. L. (2020, January). An intro to designing accessible data visualizations. Sarah L. Fossheim. https://fossheim.io/writing/posts/accessible-dataviz-design/ 
-->

---

# A different picture

![w:900](./images/creative_routines.png)

<!-- 
NOTES: 
Fossheim created the images here, showing the ‘daily routines of famous creative people’ data viz as it would be perceived by people with deuteranopia (left, back) and achromatopsia (right, front)


REFERENCES:
Currey, M. (2013). The Daily Routines of Famous Creative People—Citrix Podio. Podio.Com. https://www.podio.com/creative-routines 
Fossheim, S. L. (2020, January). An intro to designing accessible data visualizations. Sarah L. Fossheim. https://fossheim.io/writing/posts/accessible-dataviz-design/ 
-->

---

# A different picture

- Some of the colours end up looking similar or the same, and the lack of specific labels on the plot makes it impossible for individuals with either form of colourblindness to make sense of the data the creator was trying to present
- This data visualization is **not accessible** to certain people

![bg right:50% w:500](./images/creative_routines.png)

<!--
REFERENCES:
Fossheim, S. L. (2020, January). An intro to designing accessible data visualizations. Sarah L. Fossheim. https://fossheim.io/writing/posts/accessible-dataviz-design/

-->

---

- In the case of the ‘Daily Routines of Famous Creative People’ visualization, a lack of accessibility is an inconvenience, but one with a relatively limited scope
- **But** what about when the ability to make sense of the data being shared visually has an impact on people’s daily lives and wellbeing?

<!-- 
REFERENCES:

-->

---

# ‘Flattening the Curve’

![w:900](./images/lower_and_delay_the_epidemic_peak.png)

<!-- 
NOTES: 
Variations of plots similar to the image shown here - showing the need to ‘flatten the curve’ of COVID-19 transmission with control measures to avoid overwhelming healthcare systems - have become incredibly common since March of 2020

REFERENCES:
Lundgard, A., & Satyanarayan, A. (2022). Accessible Visualization via Natural Language Descriptions: A Four-Level Model of Semantic Content. https://doi.org/10.1109/TVCG.2021.3114770  -->

---

# ‘Flattening the Curve’

- Data visualizations such as this one are an efficient and effective form of communicating public health information, but not to everyone
- **Activity:** In what ways is this data visualization inaccessible, and to whom? Let’s discuss!

![bg right:50% w:500](./images/lower_and_delay_the_epidemic_peak.png)

<!-- 
NOTES: 
Note again that this visualization meets most of our standards for substantively/perceptually/aesthetically ‘good’ data visualization
Some accessibility concerns with this image: lots of text-as-image (gets blurry if you zoom, might not be processed by a screen reader); no alt text/caption for screen readers, small font size

REFERENCES:
Lundgard, A., & Satyanarayan, A. (2022). Accessible Visualization via Natural Language Descriptions: A Four-Level Model of Semantic Content. https://doi.org/10.1109/TVCG.2021.3114770
-->

---

# Pandemic information and people with visual impairments

- Graphical and spatial visualizations of pandemic data are everywhere, and help the public see epidemiological trends at a glance, but most of these images are inaccessible
    - Lack of alternative descriptive text means that people using screen readers [cannot access the data](http://vis.csail.mit.edu/pubs/vis-text-model/#bib.bib55)
    - Tactile or braille versions of COVID-19 data visualizations are [rare and often expensive](https://www.vice.com/en/article/4ag9wb/vital-coronavirus-information-is-failing-the-blind-and-visually-impaired) to create
- From Lundgard & Satyanarayan (2022), “for readers with visual disabilities… inaccessible visualizations are, at best, demeaning and, at worst, damaging to health.”

<!-- 
NOTES: 
 


REFERENCES:
Lundgard, A., & Satyanarayan, A. (2022). Accessible Visualization via Natural Language Descriptions: A Four-Level Model of Semantic Content. https://doi.org/10.1109/TVCG.2021.3114770 
Ehrenkranz, M. (2020, April 9). Vital Coronavirus Information Is Failing the Blind and Visually Impaired. Vice. https://www.vice.com/en/article/4ag9wb/vital-coronavirus-information-is-failing-the-blind-and-visually-impaired  
-->

---


- Failing to consider best practices for accessible design means that our data visualization will not have the desired positive effect on all of our audience, and may even have a harmful effect by excluding them from important data

- As professionals and academics who went to communicate our data visually, we have a responsibility to prioritize accessibility

<!--
REFERENCES:



-->

---

# Government of Canada Principles for Accessible Design

- The Government of Canada provides four broad goals for what we should try to accomplish with accessible design:
    - Make information clear, concise and easy to use
    - Present information in predictable, barrier‑free ways
    - Provide barrier‑free ways for people to interact with you
    - Make sure technology-based products work with assistive technologies and devices

<!--
REFERENCES: 
Treasury Board of Canada. (2020, October 23). Making communications accessible in the Government of Canada. Government of Canada. https://www.canada.ca/en/treasury-board-secretariat/topics/government-communications/making-communications-accessible.html 


-->

---

### So how do we incorporate these accessibility goals into our data visualization practices?

---

# Colour

---

# Using colour

- Colour is one of the most useful features of many data visualizations
- We have to be aware of the ways that colour can be perceived differently by the audiences of our images

---

# Resource: Colour Blindness Simulator

- The [Colour Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/) allows you to upload an image and apply various filters to check how its colours would be perceived by people with various types of colourblindness

![w:500](./images/colour_blindness_simulator.png)

---

# Brightness and Contrast

- Overly bright colours can be painful to look at, and overwhelming for people with sensory issues and people [on the](https://a11y.canada.ca/docs/posters/AutismSpect-en.pdf) [autism](https://fossheim.io/writing/posts/accessible-dataviz-design/)   [spectrum](https://doi.org/10.1038/srep41155)
- **Contrast**  is the ratio between the brightness of two different colours
- A higher contrast generally makes colours and objects in our data visualizations easier to tell apart

![w:500](./images/low_high_contracts.png)

<!--
REFERENCES: 
Ward, J., Hoadley, C., Hughes, J. E. A., Smith, P., Allison, C., Baron-Cohen, S., & Simner, J. (2017). Atypical sensory sensitivity as a shared feature between synaesthesia and autism. Scientific Reports, 7(1), 41155. https://doi.org/10.1038/srep41155 
https://a11y.canada.ca/docs/posters/AutismSpect-en.pdf 
Fossheim, S. L. (2020, January). An intro to designing accessible data visualizations. Sarah L. Fossheim. https://fossheim.io/writing/posts/accessible-dataviz-design/ 

-->

---

# Resource: Check Contrast

- WebAIM offers an [online tool](https://webaim.org/resources/contrastchecker/) that lets you enter in two colour values and check if they are a ‘pass’ or ‘fail’ according to [Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/) standards for contrast
- Colours can be picked from a dropper or using hexadecimal code
- The tool delivers separate contrast scores for normal text, large text, and graphical components

---

# Check Contrast

![w:900](./images/check_contrast.png)

<!-- 
NOTES: 
This image shows the default test and output from the online webAIM contrast checker tool
 -->

---

# Resource: Viridis package

- Viridis was made as an R package designed to make plots easier to read by those with colourblindness, and to maintain contrast so plots are readable in grayscale (eg. in print)
- Viridis can be used in Python with matplotlib as a colormap [https://matplotlib.org/stable/users/explain/colors/colormaps.html](https://matplotlib.org/stable/users/explain/colors/colormaps.html)

<!--
REFERENCES:
Rudis, B., Ross, N., & Garnier, S. (2021). Viridis color maps [R]. https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html 

-->

---

# Viridis package - Example

![w:800](./images/viridis_package_example.png)

<!--
REFERENCES:
Rudis, B., Ross, N., & Garnier, S. (2021). Viridis color maps [R]. https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html 


-->

---

# Viridis package - As perceived with colourblindness

|                   | ggplot Default Colour Palettes        | viridis Default Colour       |
|-------------------|---------------------------------------|--------------------------------------|
| Base              | ![](./images/ggplot_default_colour_palettes_1.png) | ![](./images/viridis_default_colour_pallete_1.png)  |
| Green-Blind (Deuteranopia) | ![](./images/ggplot_default_colour_palettes_2.png) | ![](./images/viridis_default_colour_pallete_2.png) |
| Red-Blind (Protanopia) | ![](./images/ggplot_default_colour_palettes_3.png) | ![](./images/viridis_default_colour_pallete_3.png) |
| Desaturated       | ![](./images/ggplot_default_colour_palettes_4.png) | ![](./images/viridis_default_colour_pallete_4.png) |

<!-- 
NOTES: 
Viridis colour palettes show greater contrast and thus make data easier to perceive by people with varying forms of colourblindness, or when printed without colour


REFERENCES:
Rudis, B., Ross, N., & Garnier, S. (2021). Viridis color maps [R]. https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html 
-->

---

# Moving beyond colour

- Even when we make use of best practice for accessible use of colour in our data visualization, **we should  avoid relying only on colour, where possible**
- Think back to our ‘Daily Habits’ example - use of patterns or textures in addition to colour on our bars could have made the visualization more accessible to people with visual impairments, even with the current colour scheme

![w:500](./images/the_daily_routines_of_famous_creative_people.png)

---

# Text

---

# Labels and legends

- If we want to minimize colours and patterns, data labels (on individual data points or on bars in a bar graph) can make visualizations easier to follow
- Every visual element on our graph should be clearly described in a legend; additional, brief written descriptions of visual elements can also  [reduce anxiety](https://fossheim.io/writing/posts/accessible-dataviz-design/) for our audiences

<!--
REFERENCES:
Fossheim, S. L. (2020, January). An intro to designing accessible data visualizations. Sarah L. Fossheim. https://fossheim.io/writing/posts/accessible-dataviz-design/ 


-->

---

# Fonts and typefaces

- A **typeface** is a set of text characters (eg. Arial, Times New Roman)
- A **font** is a subset of a typeface (eg. 12 point Arial in italic)
- Certain typefaces and fonts are considered more accessible than others in design and data visualization contexts

<!--
REFERENCES:
WebAIM. (2020). WebAIM: Typefaces and Fonts. WebAIM. https://webaim.org/techniques/fonts/ 

-->

---

# Typeface

- There is no single ‘right’ typeface or font to use, but generally sans-serif fonts are more accessible for  [people with cognitive disabilities](https://a11y.canada.ca/docs/posters/Cognitive-en.pdf)
- Typefaces  [identified](https://dl.acm.org/doi/10.1145/2513383.2513447)  as easier to read for people with dyslexia include:
- `Helvetica, Courier, Arial, Verdana`
- We should  [also](https://webaim.org/techniques/fonts/) avoid overwhelming users by switching between too many different typefaces in one graphic

<!--
REFERENCES:
Rello, L., & Baeza-Yates, R. (2013). Good fonts for dyslexia. Proceedings of the 15th International ACM SIGACCESS Conference on Computers and Accessibility, 1–8. https://doi.org/10.1145/2513383.2513447 
WebAIM. (2020, October 27). WebAIM: Typefaces and Fonts. WebAIM. https://webaim.org/techniques/fonts/ 

-->

---

# Font size and spacing

- Text on our data visualizations should be at least 12 point size or greater, if possible
- Spacing also affects the readability of text on our visualizations
    - **Monospaced**  text (each character takes the same amount of space) is more widely accessible than  **proportionally spaced**  text (each character only takes the space it needs)

![](./images/font_size_and_spacing.png)

<!--
REFERENCES:
- Shared Services Canada. (2021). Design principles for users with cognitive disabilities. Government of Canada. https://a11y.canada.ca/docs/posters/Cognitive-en.pdf
- Rello, L., & Baeza-Yates, R. (2013). Good fonts for dyslexia. Proceedings of the 15th International ACM SIGACCESS Conference on Computers and Accessibility, 1–8. https://doi.org/10.1145/2513383.2513447 
- WebAIM. (2020). WebAIM: Typefaces and Fonts. WebAIM. https://webaim.org/techniques/fonts/ 

-->

---

# Describing data visualizations

---

# Alt-text

- To ensure that our data visualizations are accessible to people using a screen reader or unable to see the image, we include  **alternate text (alt-text)**
- Alt-text should convey all the essential information conveyed by an image
- Generally, alt-text consists of a description of the image; if there is text in the image, alt-text should include the text
- Alt-text should be in plain language and simple sentences, when possible

<!--
REFERENCES:
- University of Toronto. (2021). Accessible Images and Multimedia | Information & Instructional Technology. https://www.utm.utoronto.ca/iits/documentation/drupal-user-guide/accessible-images-and-multimedia 
 


-->

---

# Activity: Alt-text

![bg right:50% w:500](./images/DSI_DataViz_7_AccessibleDataVisualization21.png)

What would be suitable alt-text for this image?

<!--
REFERENCES:
University of Toronto. (2021). Accessible Images and Multimedia | Information & Instructional Technology. https://www.utm.utoronto.ca/iits/documentation/drupal-user-guide/accessible-images-and-multimedia 
-->

---
# Activity: Alt-text

- The most appropriate alt-text can depend on the intended purpose of an image or visualization:
    - **If the image is only for decoration**:  “Two scientists in discussion”
    - **If the focus is on specific individuals**:  “From left-to-right: Eugenia Duodu and Patrick Gunning”
    - **If the focus is on the actual events or contents of an image**:  “Professor Patrick Gunning and doctoral student Eugenia Duodo talking by a chemistry fume hood”

    ![w:300](./images/DSI_DataViz_7_AccessibleDataVisualization21.png)

<!--
REFERENCES:
University of Toronto. (2021). Accessible Images and Multimedia | Information & Instructional Technology. https://www.utm.utoronto.ca/iits/documentation/drupal-user-guide/accessible-images-and-multimedia 
-->


---

# Alt-text for graphs and plots of data

- Accessibly describing data-centric images for alt-text and figure captions requires additional considerations compared to describing photos such as the previous example
- Lundgard & Satyanarayan (2022) collected descriptions of sample data visualizations from graduate students and found that the descriptions could be grouped into four categories

<!--
REFERENCES:
Lundgard, A., & Satyanarayan, A. (2022). Accessible Visualization via Natural Language Descriptions: A Four-Level Model of Semantic Content. https://doi.org/10.1109/TVCG.2021.3114770  


-->

---

# Four types of descriptive content

| Level | Semantic Content and Keywords |
| :-: | :-: |
| 1 | - Focus on chart elements such as chart type, title, axis ranges, labels, colours |
| 2 | - Descriptive statistics (eg. mean), outliers, max and min points, correlations, comparing points |
| 3 | - Complex trends, pattern synthesis, clusters, exceptions, common concepts<br />- Perceptual interpretations of the data |
| 4 | - Context and domain insights, social and political context and explanations<br />- Subjective interpretations that go beyond the data |

<!--
REFERENCES:
Lundgard, A., & Satyanarayan, A. (2022). Accessible Visualization via Natural Language Descriptions: A Four-Level Model of Semantic Content. https://doi.org/10.1109/TVCG.2021.3114770  
-->

---

# Activity: Four types of descriptive content

- Describe the data visualization on this slide according to each of the four types of descriptive content (click to visit website).

![w:800](./images/the_daily_routines_of_famous_creative_people.png)

<!--
REFERENCES:
Lundgard, A., & Satyanarayan, A. (2022). Accessible Visualization via Natural Language Descriptions: A Four-Level Model of Semantic Content. https://doi.org/10.1109/TVCG.2021.3114770  
Currey, M. (2013). The Daily Routines of Famous Creative People—Citrix Podio. Podio.Com. https://www.podio.com/creative-routines
-->

---

# Alt-text for graphs and plots of data

- The four types of descriptive text are **not** equally helpful!
- Both blind and sighted participants in the original study found level 1 content on its own the least helpful
- Blind participants found level 4 content the least useful
    - Blind participants preferred descriptions to contain facts about the data, giving them the agency to interpret it for themselves, rather than editorializing by the creator
- 40% of blind participants thought that the most useful descriptions would combine content from multiple levels (2 and 3)

<!--
REFERENCES:
Lundgard, A., & Satyanarayan, A. (2022). Accessible Visualization via Natural Language Descriptions: A Four-Level Model of Semantic Content. https://doi.org/10.1109/TVCG.2021.3114770
-->

---

# Can people actually access our data visualizations?

<!--
NOTES: 
Once we put in all of this effort, there’s one last big component to accessibility: making sure that the people we want to see our data viz can actually see it!
There are a couple of different elements to this
-->

---

# Cross-browser functionality

- If our data visualization is going to be embedded in a web page or otherwise accessible online, it is important to check for cross-browser functionality
- Our data visualization should be functional and visible in:
    - Chrome
    - Firefox
    - Internet Explorer 11, Microsoft Edge (Windows)
    - Safari (Mac/iOS)
- This is especially important in some professional contexts, where browser use may be limited/regulated

<!--
NOTES: 
Especially given pandemic-induced requirements for remote work, many data visualizations are primarily shown/accessed online

REFERENCES:
Canadian Digital Service. (2022). Tools and resources—Canadian Digital Service. Canadian Digital Service. https://digital.canada.ca/a11y/tools-and-resources/ 
-->

---

# Cost and accessibility

- If our data visualization is intended to reach the public or a particular subgroup of the public, the cost of accessing our visualization (and surrounding content) is an accessibility issue
    - Eg. Most academic publications require a subscription
- To maximize the accessibility of our data products, we can consider:
    - **Open Access** (Per  [University of BC Libraries](https://pose.open.ubc.ca/open-access/pathways-to-open/open-access-basics/) , “a range of practices through which research outputs are distributed online, free of cost or other access barriers”)
    - **Creative Commons licenses** (standard and simple  [licenses](https://guides.library.ubc.ca/open-education/creative-commons) to facilitate sharing and reuse of work)

<!--
REFERENCES:
The University of British Columbia. (2021). Open Access Basics. Program for Open Scholarship and Education. https://pose.open.ubc.ca/open-access/pathways-to-open/open-access-basics/ 
-->

---

- When in doubt about the accessibility of our data visualizations…
- …show somebody!
- **User testing and gathering feedback**, even informally, is the best way to understand whether our data visualizations are accessible and understandable to our intended audiences

<!--
REFERENCES:

-->

---

# For more resources…

- The Government of Canada’s [Digital Accessibility Toolkit](https://a11y.canada.ca/en/guides/) contains guides and graphics in plain language to facilitate designing with accessibility in mind
- The [AccessAbility handbook](https://www.rgd.ca/database/files/library/RGD_AccessAbility_Handbook.pdf) is a detailed guide to accessible practices in graphic design, with useful insights for data visualization

<!--
REFERENCES:
https://www.rgd.ca/resources/accessibility/access 




-->

---

# Next...

- Data Visualization as Advocacy
- Examples of data visualization used for advocacy, and best practices
- Form, representation, and giving credit as means of incorporating advocacy into our own data visualization practices
- Moving beyond matplotlib – other data viz libraries in Python
