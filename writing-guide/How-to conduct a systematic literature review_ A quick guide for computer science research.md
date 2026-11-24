---
title: "How-to conduct a systematic literature review: A quick guide for computer science research"
source: "https://pmc.ncbi.nlm.nih.gov/articles/PMC9672331/?utm_source=chatgpt.com"
author:
  - "[[Angela Carrera-Rivera]]"
  - "[[William Ochoa]]"
  - "[[Felix Larrinaga]]"
  - "[[Ganix Lasa]]"
published:
created: 2026-11-24
description: "Performing a literature review is a critical first step in research to understanding the state-of-the-art and identifying gaps and challenges in the field. A systematic literature review is a method which sets out a series of steps to methodically ..."
tags:
  - "clippings"
---
. 2022 Nov 4;9:101895. doi: [10.1016/j.mex.2022.101895](https://doi.org/10.1016/j.mex.2022.101895)

[Angela Carrera-Rivera](https://pubmed.ncbi.nlm.nih.gov/?term=%22Carrera-Rivera%20A%22[Author]) <sup>a,</sup><sup>⁎</sup>, [William Ochoa](https://pubmed.ncbi.nlm.nih.gov/?term=%22Ochoa%20W%22[Author]) <sup>a</sup>, [Felix Larrinaga](https://pubmed.ncbi.nlm.nih.gov/?term=%22Larrinaga%20F%22[Author]) <sup>a</sup>, [Ganix Lasa](https://pubmed.ncbi.nlm.nih.gov/?term=%22Lasa%20G%22[Author]) <sup>b</sup>

PMCID: PMC9672331 PMID: [36405369](https://pubmed.ncbi.nlm.nih.gov/36405369/)

## Abstract

Performing a literature review is a critical first step in research to understanding the state-of-the-art and identifying gaps and challenges in the field. A systematic literature review is a method which sets out a series of steps to methodically organize the review. In this paper, we present a guide designed for researchers and in particular early-stage researchers in the computer-science field. The contribution of the article is the following:

- •

	Clearly defined strategies to follow for a systematic literature review in computer science research, and
- •

	Algorithmic method to tackle a systematic literature review.

**Keywords:** Systematic literature reviews, literature reviews, research methodology, computer science, doctoral studies

## Graphical abstract

![Image, graphical abstract](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8334/9672331/555e10aa298f/ga1.jpg)

[Open in a new tab](https://pmc.ncbi.nlm.nih.gov/articles/PMC9672331/figure/fig0005/)

---

Specifications table

<table><tbody><tr><td colspan="1" rowspan="1">Subject area:</td><td colspan="1" rowspan="1">Computer-science</td></tr><tr><td colspan="1" rowspan="1">More specific subject area:</td><td colspan="1" rowspan="1">Software engineering</td></tr><tr><td colspan="1" rowspan="1">Name of your method:</td><td colspan="1" rowspan="1">Systematic literature review</td></tr><tr><td colspan="1" rowspan="1">Name and reference of original method:</td><td colspan="1" rowspan="1"><em>N.A.</em></td></tr><tr><td colspan="1" rowspan="1">Resource availability:</td><td colspan="1" rowspan="1">Resources referred to in this article:<ul><li>•<p>Parsif.al (<a href="https://parsif.al/">https://parsif.al/</a>)</p></li><li>•<p>VosViewer (<a href="https://www.vosviewer.com/">https://www.vosviewer.com/</a>)</p></li></ul></td></tr></tbody></table>

[Open in a new tab](https://pmc.ncbi.nlm.nih.gov/articles/PMC9672331/table/utbl0001/)

## Method details

### Overview

A Systematic Literature Review (SLR) is a research methodology to collect, identify, and critically analyze the available research studies (e.g., articles, conference proceedings, books, dissertations) through a systematic procedure [^13]. An SLR updates the reader with current literature about a subject [^7]. The goal is to review critical points of current knowledge on a topic about research questions to suggest areas for further examination [^6]. Defining an “Initial Idea” or interest in a subject to be studied is the first step before starting the SLR. An early search of the relevant literature can help determine whether the topic is too broad to adequately cover in the time frame and whether it is necessary to narrow the focus. Reading some articles can assist in setting the direction for a formal review., and formulating a potential research question (e.g., how is semantics involved in Industry 4.0?) can further facilitate this process. Once the focus has been established, an SLR can be undertaken to find more specific studies related to the variables in this question. Although there are multiple approaches for performing an SLR ([^6], [^27], [^28]), this work aims to provide a step-by-step and practical guide while citing useful examples for computer-science research. The methodology presented in this paper comprises two main phases: “Planning” described in section 2, and “Conducting” described in section 3, following the depiction of the graphical abstract.

### Planning

Defining the protocol is the first step of an SLR since it describes the procedures involved in the review and acts as a log of the activities to be performed. Obtaining opinions from peers while developing the protocol, is encouraged to ensure the review's consistency and validity, and helps identify when modifications are necessary [^21]. One final goal of the protocol is to ensure the replicability of the review.

### Define PICOC and synonyms

The PICOC (Population, Intervention, Comparison, Outcome, and Context) criteria break down the SLR's objectives into searchable keywords and help formulate research questions \[[^28]\]. PICOC is widely used in the medical and social sciences fields to encourage researchers to consider the components of the research questions [^15]. Kitchenham & Charters [^7] compiled the list of PICOC elements and their corresponding terms in computer science, as presented in [Table 1](#tbl0001), which includes keywords derived from the PICOC elements. From that point on, it is essential to think of synonyms or “alike” terms that later can be used for building queries in the selected digital libraries. For instance, the keyword “context awareness” can also be linked to “context-aware”.

#### Table 1.

Planning Step 1 “Defining PICOC keywords and synonyms”.

<table><thead><tr><th colspan="1" rowspan="1"></th><th colspan="1" rowspan="1">Description</th><th colspan="1" rowspan="1">Example (PICOC)</th><th colspan="1" rowspan="1">Example (Synonyms)</th></tr></thead><tbody><tr><td colspan="1" rowspan="1">Population</td><td colspan="1" rowspan="1">Can be a specific role, an application area, or an industry domain.</td><td colspan="1" rowspan="1">Smart Manufacturing</td><td colspan="1" rowspan="1">• Digital Factory<br>• Digital Manufacturing<br>• Smart Factory</td></tr><tr><td colspan="1" rowspan="1">Intervention</td><td colspan="1" rowspan="1">The methodology, tool, or technology that addresses a specific issue.</td><td colspan="1" rowspan="1">Semantic Web</td><td colspan="1" rowspan="1">• Ontology<br>• Semantic Reasoning</td></tr><tr><td colspan="1" rowspan="1">Comparison</td><td colspan="1" rowspan="1">The methodology, tool, or technology in which the <em>Intervention</em> is being compared (if appropriate).</td><td colspan="1" rowspan="1">Machine Learning</td><td colspan="1" rowspan="1">• Supervised Learning<br>• Unsupervised Learning</td></tr><tr><td colspan="1" rowspan="1">Outcome</td><td colspan="1" rowspan="1">Factors of importance to practitioners and/or the results that <em>Intervention</em> could produce.</td><td colspan="1" rowspan="1">Context-Awareness</td><td colspan="1" rowspan="1">• Context-Aware<br>• Context-Reasoning</td></tr><tr><td colspan="1" rowspan="1">Context</td><td colspan="1" rowspan="1">The context in which the comparison takes place. Some systematic reviews might choose to exclude this element.</td><td colspan="1" rowspan="1">Business Process Management</td><td colspan="1" rowspan="1">• BPM<br>• Business Process Modeling</td></tr></tbody></table>

[Open in a new tab](https://pmc.ncbi.nlm.nih.gov/articles/PMC9672331/table/tbl0001/)

### Formulate research questions

Clearly defined research question(s) are the key elements which set the focus for study identification and data extraction [^22]. These questions are formulated based on the PICOC criteria as presented in the example in [Table 2](#tbl0002) (PICOC keywords are underlined).

#### Table 2.

Research questions examples.

<table><thead><tr><th colspan="1" rowspan="1">Research Questions examples</th></tr></thead><tbody><tr><td colspan="1" rowspan="1">• <strong>RQ1</strong>: What are the current challenges of context-aware systems that support the decision-making of business processes in smart manufacturing?<br>• <strong>RQ2</strong>: Which technique is most appropriate to support decision-making for business process management in smart factories?<br>• <strong>RQ3</strong>: In which scenarios are semantic web and machine learning used to provide context-awareness in business process management for smart manufacturing?</td></tr></tbody></table>

[Open in a new tab](https://pmc.ncbi.nlm.nih.gov/articles/PMC9672331/table/tbl0002/)

### Select digital library sources

The validity of a study will depend on the proper selection of a database since it must adequately cover the area under investigation [^20]. The Web of Science (WoS) is an international and multidisciplinary tool for accessing literature in science, technology, biomedicine, and other disciplines. Scopus is a database that today indexes 40,562 peer-reviewed journals, compared to 24,831 for WoS. Thus, Scopus is currently the largest existing multidisciplinary database. However, it may also be necessary to include sources relevant to computer science, such as EI Compendex, IEEE Xplore, and ACM. [Table 3](#tbl0003) compares the area of expertise of a selection of databases.

#### Table 3.

Planning Step 3 “Select digital libraries”. Description of digital libraries in computer science and software engineering.

<table><thead><tr><th colspan="1" rowspan="1">Database</th><th colspan="1" rowspan="1">Description</th><th colspan="1" rowspan="1">URL</th><th colspan="1" rowspan="1">Area</th><th colspan="1" rowspan="1">Advanced Search Y/N</th></tr></thead><tbody><tr><td colspan="1" rowspan="1">Scopus</td><td colspan="1" rowspan="1">From Elsevier. sOne of the largest databases. Very user-friendly interface</td><td colspan="1" rowspan="1"><a href="http://www.scopus.com/">http://www.scopus.com</a></td><td colspan="1" rowspan="1">Interdisciplinary</td><td colspan="1" rowspan="1">Y</td></tr><tr><td colspan="1" rowspan="1">Web of Science</td><td colspan="1" rowspan="1">From Clarivate. Multidisciplinary database with wide ranging content.</td><td colspan="1" rowspan="1"><a href="https://www.webofscience.com/">https://www.webofscience.com/</a></td><td colspan="1" rowspan="1">Interdisciplinary</td><td colspan="1" rowspan="1">Y</td></tr><tr><td colspan="1" rowspan="1">EI Compendex</td><td colspan="1" rowspan="1">From Elsevier. Focused on engineering literature.</td><td colspan="1" rowspan="1"><a href="http://www.engineeringvillage.com/">http://www.engineeringvillage.com</a></td><td colspan="1" rowspan="1">Engineering</td><td colspan="1" rowspan="1">Y (Query view not available)</td></tr><tr><td colspan="1" rowspan="1">IEEE Digital Library</td><td colspan="1" rowspan="1">Contains scientific and technical articles published by IEEE and its publishing partners.</td><td colspan="1" rowspan="1"><a href="http://ieeexplore.ieee.org/">http://ieeexplore.ieee.org</a></td><td colspan="1" rowspan="1">Engineering and Technology</td><td colspan="1" rowspan="1">Y</td></tr><tr><td colspan="1" rowspan="1">ACM Digital Library</td><td colspan="1" rowspan="1">Complete collection of ACM publications.</td><td colspan="1" rowspan="1"><a href="https://dl.acm.org/">https://dl.acm.org/</a></td><td colspan="1" rowspan="1">Computing and information technology</td><td colspan="1" rowspan="1">Y</td></tr></tbody></table>

[Open in a new tab](https://pmc.ncbi.nlm.nih.gov/articles/PMC9672331/table/tbl0003/)

### Define inclusion and exclusion criteria

Authors should define the inclusion and exclusion criteria before conducting the review to prevent bias, although these can be adjusted later, if necessary. The selection of primary studies will depend on these criteria. Articles are included or excluded in this first selection based on abstract and primary bibliographic data. When unsure, the article is skimmed to further decide the relevance for the review. [Table 4](#tbl0004) sets out some criteria types with descriptions and examples.

#### Table 4.

Planning Step 4 “Define inclusion and exclusion criteria”. Examples of criteria type.

<table><thead><tr><th colspan="1" rowspan="1">Criteria Type</th><th colspan="1" rowspan="1">Description</th><th colspan="1" rowspan="1">Example</th></tr></thead><tbody><tr><td colspan="1" rowspan="1">Period</td><td colspan="1" rowspan="1">Articles can be selected based on the time period to review, e.g., reviewing the technology under study from the year it emerged, or reviewing progress in the field since the publication of a prior literature review.</td><td colspan="1" rowspan="1"><strong><em>Inclusion</em></strong>:<br>From 2015 to 2021<br><strong><em>Exclusion</em></strong><em>:</em><br>Articles prior 2015</td></tr><tr><td colspan="1" rowspan="1">Language</td><td colspan="1" rowspan="1">Articles can be excluded based on language.</td><td colspan="1" rowspan="1"><strong><em>Exclusion</em></strong>:<br>Articles not in English</td></tr><tr><td colspan="1" rowspan="1">Type of Literature</td><td colspan="1" rowspan="1">Articles can be excluded if they are fall into the category of grey literature.</td><td colspan="1" rowspan="1"><strong><em>Exclusion</em></strong><em>:</em><br>Reports, policy literature, working papers, newsletters, government documents, speeches</td></tr><tr><td colspan="1" rowspan="1">Type of source</td><td colspan="1" rowspan="1">Articles can be included or excluded by the type of origin, i.e., conference or journal articles or books.</td><td colspan="1" rowspan="1"><strong><em>Inclusion</em></strong>:<br>Articles from Conferences or Journals<br><strong><em>Exclusion</em></strong><em>:</em><br>Articles from books</td></tr><tr><td colspan="1" rowspan="1">Impact Source</td><td colspan="1" rowspan="1">Articles can be excluded if the author limits the impact factor or quartile of the source.</td><td colspan="1" rowspan="1"><strong><em>Inclusion</em></strong><br>Articles from Q1, and Q2 sources<br><strong><em>Exclusion</em></strong>:<br>Articles with a Journal Impact Score (JIS) lower than <em>x</em></td></tr><tr><td colspan="1" rowspan="1">Accessibility</td><td colspan="1" rowspan="1">Not accessible in specific databases.</td><td colspan="1" rowspan="1"><strong><em>Exclusion</em></strong>:<br>Not accessible</td></tr><tr><td colspan="1" rowspan="1">Relevance to research questions</td><td colspan="1" rowspan="1">Articles can be excluded if they are not relevant to a particular question or to “<em>n</em>” number of research questions.</td><td colspan="1" rowspan="1"><strong><em>Exclusion</em></strong><br>Not relevant to at least 2 research questions</td></tr></tbody></table>

[Open in a new tab](https://pmc.ncbi.nlm.nih.gov/articles/PMC9672331/table/tbl0004/)

### Define the Quality Assessment (QA) checklist

Assessing the quality of an article requires an artifact which describes how to perform a detailed assessment. A typical quality assessment is a checklist that contains multiple factors to evaluate. A numerical scale is used to assess the criteria and quantify the QA [^23]. Zhou et al. [^26] presented a detailed description of assessment criteria in software engineering, classified into four main aspects of study quality: Reporting, Rigor, Credibility, and Relevance. Each of these criteria can be evaluated using, for instance, a Likert-type scale [^18], as shown in [Table 5](#tbl0005). It is essential to select the same scale for all criteria established on the quality assessment.

#### Table 5.

Planning Step 5 “Define QA assessment checklist”. Examples of QA scales and questions.

<table><tbody><tr><td colspan="1" rowspan="1"><strong><em>Example 1:</em></strong><br>Do the researchers discuss any problems (limitations, threats) with the validity of their results (reliability)?</td><td colspan="1" rowspan="1"><strong>Level of Participation</strong><br>1 – No, and not considered (Score: 0)<br>2 – Partially (Score: 0.5)<br>3 – Yes (Score: 1)</td></tr><tr><td colspan="1" rowspan="1"><strong><em>Example 2:</em></strong><br>Is there a clear definition/ description/ statement of the aims/ goals/ purposes/ motivations/ objectives/ questions of the research?</td><td colspan="1" rowspan="1"><strong>Level of agreement</strong><br>1 – Disagree (Score: 1)<br>2 – Somewhat disagree (Score: 2)<br>3 – Neither agree nor disagree (Score: 3)<br>4 – Somewhat agree (Score: 4)<br>5 – Agree (Score: 5)</td></tr></tbody></table>

[Open in a new tab](https://pmc.ncbi.nlm.nih.gov/articles/PMC9672331/table/tbl0005/)

### Define the “Data Extraction” form

The data extraction form represents the information necessary to answer the research questions established for the review. Synthesizing the articles is a crucial step when conducting research. Ramesh et al. [^16] presented a classification scheme for computer science research, based on topics, research methods, and levels of analysis that can be used to categorize the articles selected. Classification methods and fields to consider when conducting a review are presented in [Table 6](#tbl0006).

#### Table 6.

Planning Step 6 “Define data extraction form”. Examples of fields.

<table><thead><tr><th colspan="1" rowspan="1">Classification and fields to consider for data extraction</th><th colspan="1" rowspan="1">Description and examples</th></tr></thead><tbody><tr><td colspan="1" rowspan="1">Research type</td><td colspan="1" rowspan="1">• <em>Theoretical research</em> focuses on abstract ideas, concepts, and theories built on literature reviews <sup><a href="#fn:10">10</a></sup>.<br>• <em>Empirical research</em> uses scientific data or case studies for explorative, descriptive, explanatory, or measurable findings <sup><a href="#fn:10">10</a></sup>.<br><strong>Example:</strong><br><sup><a href="#fn:2">2</a></sup> an SLR on context-awareness for S-PSS and categorized the articles in theoretical and empirical research.</td></tr><tr><td colspan="1" rowspan="1">By process phases, stages</td><td colspan="1" rowspan="1">When analyzing a process or series of processes, an effective way to structure the data is to find a well-established framework of reference or architecture. <strong>Examples</strong>:<br>• <sup><a href="#fn:9">9</a></sup> an SLR on self-adaptive systems uses the MAPE-K model to understand how the authors tackle each module stage.<br>• <sup><a href="#fn:14">14</a></sup> presented a context-awareness survey using the stages of context-aware lifecycle to review different methods.</td></tr><tr><td colspan="1" rowspan="1">By technology, framework, or platform</td><td colspan="1" rowspan="1">When analyzing a computer science topic, it is important to know the technology currently employed to understand trends, benefits, or limitations.<br><strong>Example</strong>:<br>• <sup><a href="#fn:4">4</a></sup> an SLR on the big data ecosystem in the manufacturing field that includes frameworks, tools, and platforms for each stage of the big data ecosystem.</td></tr><tr><td colspan="1" rowspan="1">By application field and/or industry domain</td><td colspan="1" rowspan="1">If the review is not limited to a specific “Context” or “Population&#34; (industry domain), it can be useful to identify the field of application<br><strong>Example</strong>:<br>• <sup><a href="#fn:24">24</a></sup> an SLR on adaptive training using virtual reality (VR). The review presents an extensive description of multiple application domains and examines related work.</td></tr><tr><td colspan="1" rowspan="1">Gaps and challenges</td><td colspan="1" rowspan="1">Identifying gaps and challenges is important in reviews to determine the research needs and further establish research directions that can help scholars act on the topic.</td></tr><tr><td colspan="1" rowspan="1">Findings in research</td><td colspan="1" rowspan="1">Research in computer science can deliver multiple types of findings, e.g.: <em>Framework, algorithm, methodology, data model, development approach.</em></td></tr><tr><td colspan="1" rowspan="1">Evaluation method</td><td colspan="1" rowspan="1">Case studies, experiments, surveys, mathematical demonstrations, and performance indicators.</td></tr></tbody></table>

[Open in a new tab](https://pmc.ncbi.nlm.nih.gov/articles/PMC9672331/table/tbl0006/)

The data extraction must be relevant to the research questions, and the relationship to each of the questions should be included in the form. Kitchenham & Charters [^7] presented more pertinent data that can be captured, such as conclusions, recommendations, strengths, and weaknesses. Although the data extraction form can be updated if more information is needed, this should be treated with caution since it can be time-consuming. It can therefore be helpful to first have a general background in the research topic to determine better data extraction criteria.

## Conducting

After defining the protocol, conducting the review requires following each of the steps previously described. Using tools can help simplify the performance of this task. Standard tools such as Excel or Google sheets allow multiple researchers to work collaboratively. Another online tool specifically designed for performing SLRs is Parsif.al[^1]. This tool allows researchers, especially in the context of software engineering, to define goals and objectives, import articles using BibTeX files, eliminate duplicates, define selection criteria, and generate reports.

### Build digital library search strings

Search strings are built considering the PICOC elements and synonyms to execute the search in each database library. A search string should separate the synonyms with the boolean operator OR. In comparison, the PICOC elements are separated with parentheses and the boolean operator AND. An example is presented next:

*(“Smart Manufacturing” OR “Digital Manufacturing” OR “Smart Factory”) AND (“Business Process Management” OR “BPEL” OR “BPM” OR “BPMN”) AND (“Semantic Web” OR “Ontology” OR “Semantic” OR “Semantic Web Service”) AND (“Framework” OR “Extension” OR “Plugin” OR “Tool”*

### Gather studies

Databases that feature advanced searches enable researchers to perform search queries based on titles, abstracts, and keywords, as well as for years or areas of research. [Fig. 1](#fig0001) presents the example of an advanced search in Scopus, using titles, abstracts, and keywords (TITLE-ABS-KEY). Most of the databases allow the use of logical operators (i.e., AND, OR). In the example, the search is for *“BIG DATA”* and *“USER EXPERIENCE”* or *“UX”* as a synonym.

[![Fig 1](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8334/9672331/0b8713a3a74e/gr1.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9672331_gr1.jpg)

Example of Advanced search on Scopus.

In general, bibliometric data of articles can be exported from the databases as a comma-separated-value file (CSV) or BibTeX file, which is helpful for data extraction and quantitative and qualitative analysis. In addition, researchers should take advantage of reference-management software such as Zotero, Mendeley, Endnote, or Jabref, which import bibliographic information onto the software easily.

### Study Selection and Refinement

The first step in this stage is to identify any duplicates that appear in the different searches in the selected databases. Some automatic procedures, tools like Excel formulas, or programming languages (i.e., Python) can be convenient here.

In the second step, articles are included or excluded according to the selection criteria, mainly by reading titles and abstracts. Finally, the quality is assessed using the predefined scale. [Fig. 2](#fig0002) shows an example of an article QA evaluation in Parsif.al, using a simple scale. In this scenario, the scoring procedure is the following *YES= 1, PARTIALLY= 0.5,* and *NO or UNKNOWN = 0*. A cut-off score should be defined to filter those articles that do not pass the QA. The QA will require a light review of the full text of the article.

[![Fig 2](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8334/9672331/52f50c7b7034/gr2.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9672331_gr2.jpg)

Performing quality assessment (QA) in Parsif.al.

### Data extraction

Those articles that pass the study selection are then thoroughly and critically read. Next, the researcher completes the information required using the “data extraction” form, as illustrated in [Fig. 3](#fig0003), in this scenario using Parsif.al tool.

[![Fig 3](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8334/9672331/26d5136f62c6/gr3.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9672331_gr3.jpg)

Example of data extraction form using Parsif.al.

The information required (study characteristics and findings) from each included study must be acquired and documented through careful reading. Data extraction is valuable, especially if the data requires manipulation or assumptions and inferences. Thus, information can be synthesized from the extracted data for qualitative or quantitative analysis [^17]. This documentation supports clarity, precise reporting, and the ability to scrutinize and replicate the examination.

### Analysis and Report

The analysis phase examines the synthesized data and extracts meaningful information from the selected articles [^11]. There are two main goals in this phase.

The first goal is to analyze the literature in terms of leading authors, journals, countries, and organizations. Furthermore, it helps identify correlations among topics. Even when not mandatory, this activity can be constructive for researchers to position their work, find trends, and find collaboration opportunities. Next, data from the selected articles can be analyzed using bibliometric analysis (BA). BA summarizes large amounts of bibliometric data to present the state of intellectual structure and emerging trends in a topic or field of research [^5]. [Table 7](#tbl0007) sets out some of the most common bibliometric analysis representations.

#### Table 7.

Techniques for bibliometric analysis and examples.

<table><thead><tr><th colspan="1" rowspan="1">Publication-related analysis</th><th colspan="1" rowspan="1">Description</th><th colspan="1" rowspan="1">Example</th></tr></thead><tbody><tr><td colspan="1" rowspan="1">Years of publications</td><td colspan="1" rowspan="1">Determine interest in the research topic by years or the period established by the SLR, by quantifying the number of papers published. Using this information, it is also possible to forecast the growth rate of research interest.</td><td colspan="1" rowspan="1">&#91;<sup><a href="#fn:12">12</a></sup>&#93; identified the growth rate of research interest and the yearly publication trend.</td></tr><tr><td colspan="1" rowspan="1">Top <em>k</em> contribution journals/conferences</td><td colspan="1" rowspan="1">Identify the leading journals and conferences in which authors can share their current and future work.</td><td colspan="1" rowspan="1"><sup><a href="#fn:2">2</a></sup>,<sup><a href="#fn:3">3</a></sup></td></tr><tr><td colspan="1" rowspan="1">Top <em>k</em> countries&#39; or affiliation contributions</td><td colspan="1" rowspan="1">Examine the impacts of countries or affiliations leading the research topic.</td><td colspan="1" rowspan="1">&#91;<sup><a href="#fn:12">12</a></sup>, <sup><a href="#fn:25">25</a></sup>&#93; identified the most influential countries.</td></tr><tr><td colspan="1" rowspan="1">Leading authors</td><td colspan="1" rowspan="1">Identify the most significant authors in a research field.</td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">Keyword correlation analysis</td><td colspan="1" rowspan="1">Explore existing relationships between topics in a research field based on the written content of the publication or related keywords established in the articles.</td><td colspan="1" rowspan="1"><sup><a href="#fn:2">2</a></sup> using keyword clustering analysis (<a href="#fig0004">Fig. 4</a>). <sup><a href="#fn:3">3</a></sup> using frequency analysis.</td></tr><tr><td colspan="1" rowspan="1">Total and average citation</td><td colspan="1" rowspan="1">Identify the most relevant publications in a research field.</td><td colspan="1" rowspan="1"><sup><a href="#fn:8">8</a></sup><br>Scatter plot citation scores and journal factor impact</td></tr></tbody></table>

[Open in a new tab](https://pmc.ncbi.nlm.nih.gov/articles/PMC9672331/table/tbl0007/)

Several tools can perform this type of analysis, such as Excel and Google Sheets for statistical graphs or using programming languages such as Python that has available multiple data visualization libraries (i.e. Matplotlib, Seaborn). Cluster maps based on bibliographic data(i.e keywords, authors) can be developed in **VosViewer** which makes it easy to identify clusters of related items [^19]. In [Fig. 4](#fig0004), node size is representative of the number of papers related to the keyword, and lines represent the links among keyword terms.

[![Fig 4](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8334/9672331/8fbc16127da7/gr4.jpg)](https://www.ncbi.nlm.nih.gov/core/lw/2.0/html/tileshop_pmc/tileshop_pmc_inline.html?title=Click%20on%20image%20to%20zoom&p=PMC3&id=9672331_gr4.jpg)

[^2] Keyword co-relationship analysis using clusterization in vos viewer.

This second and most important goal is to answer the formulated research questions, which should include a quantitative and qualitative analysis. The **quantitative** analysis can make use of data categorized, labelled, or coded in the extraction form (see Section 1.6). This data can be transformed into numerical values to perform statistical analysis. One of the most widely employed method is *frequency analysis,* which shows the recurrence of an event, and can also represent the percental distribution of the population (i.e., percentage by technology type, frequency of use of different frameworks, etc.). Q **ualitative** analysis includes the narration of the results, the discussion indicating the way forward in future research work, and inferring a conclusion.

Finally, the literature review report should state the protocol to ensure others researchers can replicate the process and understand how the analysis was performed. In the protocol, it is essential to present the inclusion and exclusion criteria, quality assessment, and rationality beyond these aspects.

The presentation and reporting of results will depend on the structure of the review given by the researchers conducting the SLR, there is no one answer. This structure should tie the studies together into key themes, characteristics, or subgroups \[[^29]\].

## Conclusion

SLR can be an extensive and demanding task, however the results are beneficial in providing a comprehensive overview of the available evidence on a given topic. For this reason, researchers should keep in mind that the entire process of the SLR is tailored to answer the research question(s). This article has detailed a practical guide with the essential steps to conducting an SLR in the context of computer science and software engineering while citing multiple helpful examples and tools. It is envisaged that this method will assist researchers, and particularly early-stage researchers, in following an algorithmic approach to fulfill this task. Finally, a quick checklist is presented in [Appendix A](#sec0114) as a companion of this article.

## CRediT author statement

**Angela Carrera-Rivera:** Conceptualization, Methodology, Writing-Original. **William Ochoa-Agurto**: Methodology, Writing-Original. **Felix Larrinaga**: Reviewing and Supervision **Ganix Lasa:** Reviewing and Supervision.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

**Funding***:* This project has received funding from the European Union's Horizon 2020 research and innovation programme under the Marie Sklodowska-Curie Grant No. 814078.

## Footnotes

Carrera-Rivera, A., Larrinaga, F., & Lasa, G. (2022). Context-awareness for the design of Smart-product service systems: Literature review. Computers in Industry, 142, 103730.

<sup>1</sup>

[https://parsif.al/](https://parsif.al/)

## Contributor Information

Angela Carrera-Rivera, Email: aicarrera@mondragon.edu.

William Ochoa, Email: wsochoa@mondragon.edu.

Felix Larrinaga, Email: flarrinaga@mondragon.edu.

Ganix Lasa, Email: glasa@mondragon.edu.

## Appendix A

![graphic file with name fx1.gif](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/8334/9672331/e3b790dd149b/fx1.gif)

## Data Availability

- No data was used for the research described in the article.

## References

- 1.Carrera-Rivera A., Larrinaga F., Lasa G. Context-Awareness for the design of Smart-Product Service Systems: Literature Review. Comput. Ind. 2022 \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Comput.%20Ind.&title=Context-Awareness%20for%20the%20design%20of%20Smart-Product%20Service%20Systems:%20Literature%20Review&author=A.%20Carrera-Rivera&author=F.%20Larrinaga&author=G.%20Lasa&publication_year=2022&)\]
- 2.Cong J., Chen C.-H., Zheng P., Li X., Wang Z. A holistic relook at engineering design methodologies for smart product-service systems development. J. Cleaner Prod. 2020;272 doi: 10.1016/j.jclepro.2020.122737. \[[DOI](https://doi.org/10.1016/j.jclepro.2020.122737)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Cleaner%20Prod.&title=A%20holistic%20relook%20at%20engineering%20design%20methodologies%20for%20smart%20product-service%20systems%20development&author=J.%20Cong&author=C.-H.%20Chen&author=P.%20Zheng&author=X.%20Li&author=Z.%20Wang&volume=272&publication_year=2020&doi=10.1016/j.jclepro.2020.122737&)\]
- 3.Cui Y., Kara S., Chan K.C. Manufacturing big data ecosystem: A systematic literature review. Rob. Comput. Integr. Manuf. 2020;62 \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Rob.%20Comput.%20Integr.%20Manuf.&title=Manufacturing%20big%20data%20ecosystem:%20A%20systematic%20literature%20review&author=Y.%20Cui&author=S.%20Kara&author=K.C.%20Chan&volume=62&publication_year=2020&)\]
- 4.Donthu N., Kumar S., Mukherjee D., Pandey N., Lim W.M. How to conduct a bibliometric analysis: An overview and guidelines. J. Bus. Res. 2021;133:285–296. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Bus.%20Res.&title=How%20to%20conduct%20a%20bibliometric%20analysis:%20An%20overview%20and%20guidelines&author=N.%20Donthu&author=S.%20Kumar&author=D.%20Mukherjee&author=N.%20Pandey&author=W.M.%20Lim&volume=133&publication_year=2021&pages=285-296&)\]
- 5.Kitchenham B., Brereton O.P., Budgen D., Turner M., Bailey J., Linkman S. Systematic literature reviews in software engineering–a systematic literature review. Inf. Softw. Technol. 2009;51(1):7–15. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Inf.%20Softw.%20Technol.&title=Systematic%20literature%20reviews%20in%20software%20engineering%E2%80%93a%20systematic%20literature%20review&author=B.%20Kitchenham&author=O.P.%20Brereton&author=D.%20Budgen&author=M.%20Turner&author=J.%20Bailey&volume=51&issue=1&publication_year=2009&pages=7-15&)\]
- 6.Kitchenham B., Charters S. 2007. Guidelines for performing systematic literature reviews in software engineering.[https://www.cs.auckland.ac.nz/~norsaremah/2007%20Guidelines%20for%20performing%20SLR%20in%20SE%20v2.3.pdf](https://www.cs.auckland.ac.nz/~norsaremah/2007%20Guidelines%20for%20performing%20SLR%20in%20SE%20v2.3.pdf) Technical report, EBSE Technical Report EBSE-2007-01. \[[Google Scholar](https://scholar.google.com/scholar_lookup?Kitchenham%20B.,%20Charters%20S.%202007.%20Guidelines%20for%20performing%20systematic%20literature%20reviews%20in%20software%20engineering.https://www.cs.auckland.ac.nz/~norsaremah/2007%20Guidelines%20for%20performing%20SLR%20in%20SE%20v2.3.pdf%20Technical%20report,%20EBSE%20Technical%20Report%20EBSE-2007-01.)\]
- 7.Machchhar R.J., Toller C.N.K., Bertoni A., Bertoni M. Data-driven value creation in Smart Product-Service System design: State-of-the-art and research directions. Comput. Ind. 2022;137 doi: 10.1016/j.compind.2022.103606. \[[DOI](https://doi.org/10.1016/j.compind.2022.103606)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Comput.%20Ind.&title=Data-driven%20value%20creation%20in%20Smart%20Product-Service%20System%20design:%20State-of-the-art%20and%20research%20directions&author=R.J.%20Machchhar&author=C.N.K.%20Toller&author=A.%20Bertoni&author=M.%20Bertoni&volume=137&publication_year=2022&doi=10.1016/j.compind.2022.103606&)\]
- 8.Mahdavi-Hezavehi S., Durelli V.H., Weyns D., Avgeriou P. A systematic literature review on methods that handle multiple quality attributes in architecture-based self-adaptive systems. Inf. Softw. Technol. 2017;90:1–26. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Inf.%20Softw.%20Technol.&title=A%20systematic%20literature%20review%20on%20methods%20that%20handle%20multiple%20quality%20attributes%20in%20architecture-based%20self-adaptive%20systems&author=S.%20Mahdavi-Hezavehi&author=V.H.%20Durelli&author=D.%20Weyns&author=P.%20Avgeriou&volume=90&publication_year=2017&pages=1-26&)\]
- 9.Marczyk G.R., DeMatteo D., Festinger D. Vol. 2. John Wiley & Sons; 2010. (Essentials of research design and methodology). \[[Google Scholar](https://scholar.google.com/scholar_lookup?Marczyk%20G.R.,%20DeMatteo%20D.,%20Festinger%20D.%20Vol.%202.%20John%20Wiley%20&%20Sons;%202010.%20\(Essentials%20of%20research%20design%20and%20methodology\).)\]
- 10.Mengist W., Soromessa T., Legese G. Method for conducting systematic literature review and meta-analysis for environmental science research. MethodsX. 2020;7 doi: 10.1016/j.mex.2019.100777. \[[DOI](https://doi.org/10.1016/j.mex.2019.100777)\] \[[PMC free article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6974768/)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/31993339/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=MethodsX&title=Method%20for%20conducting%20systematic%20literature%20review%20and%20meta-analysis%20for%20environmental%20science%20research&author=W.%20Mengist&author=T.%20Soromessa&author=G.%20Legese&volume=7&publication_year=2020&pmid=31993339&doi=10.1016/j.mex.2019.100777&)\]
- 11.Ngoc H.N., Lasa G., Iriarte I. Human-centred design in industry 4.0: Case study review and opportunities for future research. J. Intell. Manuf. 2021:1–42. doi: 10.1007/s10845-021-01796-x. \[[DOI](https://doi.org/10.1007/s10845-021-01796-x)\] \[[PMC free article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8195456/)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/34149201/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Intell.%20Manuf.&title=Human-centred%20design%20in%20industry%204.0:%20Case%20study%20review%20and%20opportunities%20for%20future%20research&author=H.N.%20Ngoc&author=G.%20Lasa&author=I.%20Iriarte&publication_year=2021&pages=1-42&pmid=34149201&doi=10.1007/s10845-021-01796-x&)\]
- 12.Pati D., Lorusso L.N. How to write a systematic review of the literature. HERD. 2018;11(1):15–30. doi: 10.1177/1937586717747384. \[[DOI](https://doi.org/10.1177/1937586717747384)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/29283007/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=HERD&title=How%20to%20write%20a%20systematic%20review%20of%20the%20literature&author=D.%20Pati&author=L.N.%20Lorusso&volume=11&issue=1&publication_year=2018&pages=15-30&pmid=29283007&doi=10.1177/1937586717747384&)\]
- 13.Perera C., Zaslavsky A., Christen P., Georgakopoulos D. Context aware computing for the internet of things: A survey. IEEE Communications Surveys & Tutorials. 2013;16(1):414–454. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=IEEE%20Communications%20Surveys%20&%20Tutorials&title=Context%20aware%20computing%20for%20the%20internet%20of%20things:%20A%20survey&author=C.%20Perera&author=A.%20Zaslavsky&author=P.%20Christen&author=D.%20Georgakopoulos&volume=16&issue=1&publication_year=2013&pages=414-454&)\]
- 14.Petticrew M., Roberts H. John Wiley & Sons; 2008. Systematic reviews in the social sciences: A practical guide. \[[Google Scholar](https://scholar.google.com/scholar_lookup?Petticrew%20M.,%20Roberts%20H.%20John%20Wiley%20&%20Sons;%202008.%20Systematic%20reviews%20in%20the%20social%20sciences:%20A%20practical%20guide.)\]
- 15.Ramesh V., Glass R.L., Vessey I. Research in computer science: An empirical study. J. Syst. Softw. 2004;70(1–2):165–176. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Syst.%20Softw.&title=Research%20in%20computer%20science:%20An%20empirical%20study&author=V.%20Ramesh&author=R.L.%20Glass&author=I.%20Vessey&volume=70&issue=1%E2%80%932&publication_year=2004&pages=165-176&)\]
- 16.Taylor K.S., Mahtani K.R., Aronson J.K. Summarising good practice guidelines for data extraction for systematic reviews and meta-analysis. BMJ Evid. Based Med. 2021;26(3):88–90. doi: 10.1136/bmjebm-2020-111651. \[[DOI](https://doi.org/10.1136/bmjebm-2020-111651)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/33632720/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMJ%20Evid.%20Based%20Med.&title=Summarising%20good%20practice%20guidelines%20for%20data%20extraction%20for%20systematic%20reviews%20and%20meta-analysis&author=K.S.%20Taylor&author=K.R.%20Mahtani&author=J.K.%20Aronson&volume=26&issue=3&publication_year=2021&pages=88-90&pmid=33632720&doi=10.1136/bmjebm-2020-111651&)\]
- 17.Vagias W.M. Clemson International Institute for Tourism & Research Development, Department of Parks, Recreation and Tourism Management. Clemson University; 2006. Likert-type scale response anchors. \[[Google Scholar](https://scholar.google.com/scholar_lookup?Vagias%20W.M.%20Clemson%20International%20Institute%20for%20Tourism%20&%20Research%20Development,%20Department%20of%20Parks,%20Recreation%20and%20Tourism%20Management.%20Clemson%20University;%202006.%20Likert-type%20scale%20response%20anchors.)\]
- 18.Van Eck N.J., Waltman L. Software survey: VOSviewer, a computer program for bibliometric mapping. Scientometrics. 2010;84(2):523–538. doi: 10.1007/s11192-009-0146-3. \[[DOI](https://doi.org/10.1007/s11192-009-0146-3)\] \[[PMC free article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2883932/)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/20585380/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Scientometrics&title=Software%20survey:%20VOSviewer,%20a%20computer%20program%20for%20bibliometric%20mapping&author=N.J.%20Van%20Eck&author=L.%20Waltman&volume=84&issue=2&publication_year=2010&pages=523-538&pmid=20585380&doi=10.1007/s11192-009-0146-3&)\]
- 19.Vieira E., Gomes J. A comparison of Scopus and Web of Science for a typical university. Scientometrics. 2009;81(2):587–600. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Scientometrics&title=A%20comparison%20of%20Scopus%20and%20Web%20of%20Science%20for%20a%20typical%20university&author=E.%20Vieira&author=J.%20Gomes&volume=81&issue=2&publication_year=2009&pages=587-600&)\]
- 20.Wohlin C., Runeson P., Höst M., Ohlsson M.C., Regnell B., Wesslén A. Springer Science & Business Media; 2012. Experimentation in software engineering. a. \[[Google Scholar](https://scholar.google.com/scholar_lookup?Wohlin%20C.,%20Runeson%20P.,%20H%C3%B6st%20M.,%20Ohlsson%20M.C.,%20Regnell%20B.,%20Wessl%C3%A9n%20A.%20Springer%20Science%20&%20Business%20Media;%202012.%20Experimentation%20in%20software%20engineering.%20a.)\]
- 21.Wohlin C., Runeson P., Höst M., Ohlsson M.C., Regnell B., Wesslén A. Experimentation in Software Engineering. Springer; Berlin Heidelberg: 2012. Systematic Literature Reviews; pp. 45–54. \[[DOI](https://doi.org/10.1007/978-3-642-29044-2_4)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?title=Experimentation%20in%20Software%20Engineering&author=C.%20Wohlin&author=P.%20Runeson&author=M.%20H%C3%B6st&author=M.C.%20Ohlsson&author=B.%20Regnell&publication_year=2012&)\]
- 22.Yang L., Zhang H., Shen H., Huang X., Zhou X., Rong G., Shao D. Quality assessment in systematic literature reviews: A software engineering perspective. Inf. Softw. Technol. 2021;130 \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Inf.%20Softw.%20Technol.&title=Quality%20assessment%20in%20systematic%20literature%20reviews:%20A%20software%20engineering%20perspective&author=L.%20Yang&author=H.%20Zhang&author=H.%20Shen&author=X.%20Huang&author=X.%20Zhou&volume=130&publication_year=2021&)\]
- 23.Zahabi M., Razak Abdul, A M. Adaptive virtual reality-based training: A systematic literature review and framework. Augmented Reality, Virtual Reality, Comput. Graphics, Int. Conf., AVR 2020, Proc., 7th. 2020;24(4):725–752. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Augmented%20Reality,%20Virtual%20Reality,%20Comput.%20Graphics,%20Int.%20Conf.,%20AVR%202020,%20Proc.,%207th&title=Adaptive%20virtual%20reality-based%20training:%20A%20systematic%20literature%20review%20and%20framework&author=M.%20Zahabi&author=Abdul%20Razak&author=M%20A&volume=24&issue=4&publication_year=2020&pages=725-752&)\]
- 24.Zheng P., Wang Z., Chen C.-H., Khoo L.P. A survey of smart product-service systems: Key aspects, challenges and future perspectives. Adv. Eng. Inf. 2019;42 \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Adv.%20Eng.%20Inf.&title=A%20survey%20of%20smart%20product-service%20systems:%20Key%20aspects,%20challenges%20and%20future%20perspectives&author=P.%20Zheng&author=Z.%20Wang&author=C.-H.%20Chen&author=L.P.%20Khoo&volume=42&publication_year=2019&)\]
- 25.Zhou Y., Zhang H., Huang X., Yang S., Babar M.A., Tang H. Proceedings of the 19th International Conference on Evaluation and Assessment in Software Engineering. 2015. Quality assessment of systematic reviews in software engineering: A tertiary study; pp. 1–14. \[[Google Scholar](https://scholar.google.com/scholar_lookup?title=Proceedings%20of%20the%2019th%20International%20Conference%20on%20Evaluation%20and%20Assessment%20in%20Software%20Engineering&author=Y.%20Zhou&author=H.%20Zhang&author=X.%20Huang&author=S.%20Yang&author=M.A.%20Babar&publication_year=2015&)\]
- 26.Okoli, C., & Schabram, K. (2010). A guide to conducting a systematic literature review of information systems research.
- 27.Petersen K., Vakkalanka S., Kuzniarz L. Guidelines for conducting systematic mapping studies in software engineering: An update. Information and software technology. 2015;64:1–18. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Information%20and%20software%20technology&title=Guidelines%20for%20conducting%20systematic%20mapping%20studies%20in%20software%20engineering:%20An%20update&author=K.%20Petersen&author=S.%20Vakkalanka&author=L.%20Kuzniarz&volume=64&publication_year=2015&pages=1-18&)\]
- 28.Rowley J., Slack F. Conducting a literature review. Management research news. 2004 \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Management%20research%20news&title=Conducting%20a%20literature%20review&author=J.%20Rowley&author=F.%20Slack&publication_year=2004&)\]

## Associated Data

*This section collects any data citations, data availability statements, or supplementary materials included in this article.*

### Data Availability Statement

- No data was used for the research described in the article.

[^1]: [https://parsif.al/](https://parsif.al/)

[^2]: 1.Carrera-Rivera A., Larrinaga F., Lasa G. Context-Awareness for the design of Smart-Product Service Systems: Literature Review. Comput. Ind. 2022 \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Comput.%20Ind.&title=Context-Awareness%20for%20the%20design%20of%20Smart-Product%20Service%20Systems:%20Literature%20Review&author=A.%20Carrera-Rivera&author=F.%20Larrinaga&author=G.%20Lasa&publication_year=2022&)\]

[^3]: 2.Cong J., Chen C.-H., Zheng P., Li X., Wang Z. A holistic relook at engineering design methodologies for smart product-service systems development. J. Cleaner Prod. 2020;272 doi: 10.1016/j.jclepro.2020.122737. \[[DOI](https://doi.org/10.1016/j.jclepro.2020.122737)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Cleaner%20Prod.&title=A%20holistic%20relook%20at%20engineering%20design%20methodologies%20for%20smart%20product-service%20systems%20development&author=J.%20Cong&author=C.-H.%20Chen&author=P.%20Zheng&author=X.%20Li&author=Z.%20Wang&volume=272&publication_year=2020&doi=10.1016/j.jclepro.2020.122737&)\]

[^4]: 3.Cui Y., Kara S., Chan K.C. Manufacturing big data ecosystem: A systematic literature review. Rob. Comput. Integr. Manuf. 2020;62 \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Rob.%20Comput.%20Integr.%20Manuf.&title=Manufacturing%20big%20data%20ecosystem:%20A%20systematic%20literature%20review&author=Y.%20Cui&author=S.%20Kara&author=K.C.%20Chan&volume=62&publication_year=2020&)\]

[^5]: 4.Donthu N., Kumar S., Mukherjee D., Pandey N., Lim W.M. How to conduct a bibliometric analysis: An overview and guidelines. J. Bus. Res. 2021;133:285–296. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Bus.%20Res.&title=How%20to%20conduct%20a%20bibliometric%20analysis:%20An%20overview%20and%20guidelines&author=N.%20Donthu&author=S.%20Kumar&author=D.%20Mukherjee&author=N.%20Pandey&author=W.M.%20Lim&volume=133&publication_year=2021&pages=285-296&)\]

[^6]: 5.Kitchenham B., Brereton O.P., Budgen D., Turner M., Bailey J., Linkman S. Systematic literature reviews in software engineering–a systematic literature review. Inf. Softw. Technol. 2009;51(1):7–15. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Inf.%20Softw.%20Technol.&title=Systematic%20literature%20reviews%20in%20software%20engineering%E2%80%93a%20systematic%20literature%20review&author=B.%20Kitchenham&author=O.P.%20Brereton&author=D.%20Budgen&author=M.%20Turner&author=J.%20Bailey&volume=51&issue=1&publication_year=2009&pages=7-15&)\]

[^7]: 6.Kitchenham B., Charters S. 2007. Guidelines for performing systematic literature reviews in software engineering.[https://www.cs.auckland.ac.nz/~norsaremah/2007%20Guidelines%20for%20performing%20SLR%20in%20SE%20v2.3.pdf](https://www.cs.auckland.ac.nz/~norsaremah/2007%20Guidelines%20for%20performing%20SLR%20in%20SE%20v2.3.pdf) Technical report, EBSE Technical Report EBSE-2007-01. \[[Google Scholar](https://scholar.google.com/scholar_lookup?Kitchenham%20B.,%20Charters%20S.%202007.%20Guidelines%20for%20performing%20systematic%20literature%20reviews%20in%20software%20engineering.https://www.cs.auckland.ac.nz/~norsaremah/2007%20Guidelines%20for%20performing%20SLR%20in%20SE%20v2.3.pdf%20Technical%20report,%20EBSE%20Technical%20Report%20EBSE-2007-01.)\]

[^8]: 7.Machchhar R.J., Toller C.N.K., Bertoni A., Bertoni M. Data-driven value creation in Smart Product-Service System design: State-of-the-art and research directions. Comput. Ind. 2022;137 doi: 10.1016/j.compind.2022.103606. \[[DOI](https://doi.org/10.1016/j.compind.2022.103606)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Comput.%20Ind.&title=Data-driven%20value%20creation%20in%20Smart%20Product-Service%20System%20design:%20State-of-the-art%20and%20research%20directions&author=R.J.%20Machchhar&author=C.N.K.%20Toller&author=A.%20Bertoni&author=M.%20Bertoni&volume=137&publication_year=2022&doi=10.1016/j.compind.2022.103606&)\]

[^9]: 8.Mahdavi-Hezavehi S., Durelli V.H., Weyns D., Avgeriou P. A systematic literature review on methods that handle multiple quality attributes in architecture-based self-adaptive systems. Inf. Softw. Technol. 2017;90:1–26. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Inf.%20Softw.%20Technol.&title=A%20systematic%20literature%20review%20on%20methods%20that%20handle%20multiple%20quality%20attributes%20in%20architecture-based%20self-adaptive%20systems&author=S.%20Mahdavi-Hezavehi&author=V.H.%20Durelli&author=D.%20Weyns&author=P.%20Avgeriou&volume=90&publication_year=2017&pages=1-26&)\]

[^10]: 9.Marczyk G.R., DeMatteo D., Festinger D. Vol. 2. John Wiley & Sons; 2010. (Essentials of research design and methodology). \[[Google Scholar](https://scholar.google.com/scholar_lookup?Marczyk%20G.R.,%20DeMatteo%20D.,%20Festinger%20D.%20Vol.%202.%20John%20Wiley%20&%20Sons;%202010.%20\(Essentials%20of%20research%20design%20and%20methodology\).)\]

[^11]: 10.Mengist W., Soromessa T., Legese G. Method for conducting systematic literature review and meta-analysis for environmental science research. MethodsX. 2020;7 doi: 10.1016/j.mex.2019.100777. \[[DOI](https://doi.org/10.1016/j.mex.2019.100777)\] \[[PMC free article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6974768/)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/31993339/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=MethodsX&title=Method%20for%20conducting%20systematic%20literature%20review%20and%20meta-analysis%20for%20environmental%20science%20research&author=W.%20Mengist&author=T.%20Soromessa&author=G.%20Legese&volume=7&publication_year=2020&pmid=31993339&doi=10.1016/j.mex.2019.100777&)\]

[^12]: 11.Ngoc H.N., Lasa G., Iriarte I. Human-centred design in industry 4.0: Case study review and opportunities for future research. J. Intell. Manuf. 2021:1–42. doi: 10.1007/s10845-021-01796-x. \[[DOI](https://doi.org/10.1007/s10845-021-01796-x)\] \[[PMC free article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8195456/)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/34149201/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Intell.%20Manuf.&title=Human-centred%20design%20in%20industry%204.0:%20Case%20study%20review%20and%20opportunities%20for%20future%20research&author=H.N.%20Ngoc&author=G.%20Lasa&author=I.%20Iriarte&publication_year=2021&pages=1-42&pmid=34149201&doi=10.1007/s10845-021-01796-x&)\]

[^13]: 12.Pati D., Lorusso L.N. How to write a systematic review of the literature. HERD. 2018;11(1):15–30. doi: 10.1177/1937586717747384. \[[DOI](https://doi.org/10.1177/1937586717747384)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/29283007/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=HERD&title=How%20to%20write%20a%20systematic%20review%20of%20the%20literature&author=D.%20Pati&author=L.N.%20Lorusso&volume=11&issue=1&publication_year=2018&pages=15-30&pmid=29283007&doi=10.1177/1937586717747384&)\]

[^14]: 13.Perera C., Zaslavsky A., Christen P., Georgakopoulos D. Context aware computing for the internet of things: A survey. IEEE Communications Surveys & Tutorials. 2013;16(1):414–454. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=IEEE%20Communications%20Surveys%20&%20Tutorials&title=Context%20aware%20computing%20for%20the%20internet%20of%20things:%20A%20survey&author=C.%20Perera&author=A.%20Zaslavsky&author=P.%20Christen&author=D.%20Georgakopoulos&volume=16&issue=1&publication_year=2013&pages=414-454&)\]

[^15]: 14.Petticrew M., Roberts H. John Wiley & Sons; 2008. Systematic reviews in the social sciences: A practical guide. \[[Google Scholar](https://scholar.google.com/scholar_lookup?Petticrew%20M.,%20Roberts%20H.%20John%20Wiley%20&%20Sons;%202008.%20Systematic%20reviews%20in%20the%20social%20sciences:%20A%20practical%20guide.)\]

[^16]: 15.Ramesh V., Glass R.L., Vessey I. Research in computer science: An empirical study. J. Syst. Softw. 2004;70(1–2):165–176. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=J.%20Syst.%20Softw.&title=Research%20in%20computer%20science:%20An%20empirical%20study&author=V.%20Ramesh&author=R.L.%20Glass&author=I.%20Vessey&volume=70&issue=1%E2%80%932&publication_year=2004&pages=165-176&)\]

[^17]: 16.Taylor K.S., Mahtani K.R., Aronson J.K. Summarising good practice guidelines for data extraction for systematic reviews and meta-analysis. BMJ Evid. Based Med. 2021;26(3):88–90. doi: 10.1136/bmjebm-2020-111651. \[[DOI](https://doi.org/10.1136/bmjebm-2020-111651)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/33632720/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=BMJ%20Evid.%20Based%20Med.&title=Summarising%20good%20practice%20guidelines%20for%20data%20extraction%20for%20systematic%20reviews%20and%20meta-analysis&author=K.S.%20Taylor&author=K.R.%20Mahtani&author=J.K.%20Aronson&volume=26&issue=3&publication_year=2021&pages=88-90&pmid=33632720&doi=10.1136/bmjebm-2020-111651&)\]

[^18]: 17.Vagias W.M. Clemson International Institute for Tourism & Research Development, Department of Parks, Recreation and Tourism Management. Clemson University; 2006. Likert-type scale response anchors. \[[Google Scholar](https://scholar.google.com/scholar_lookup?Vagias%20W.M.%20Clemson%20International%20Institute%20for%20Tourism%20&%20Research%20Development,%20Department%20of%20Parks,%20Recreation%20and%20Tourism%20Management.%20Clemson%20University;%202006.%20Likert-type%20scale%20response%20anchors.)\]

[^19]: 18.Van Eck N.J., Waltman L. Software survey: VOSviewer, a computer program for bibliometric mapping. Scientometrics. 2010;84(2):523–538. doi: 10.1007/s11192-009-0146-3. \[[DOI](https://doi.org/10.1007/s11192-009-0146-3)\] \[[PMC free article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2883932/)\] \[[PubMed](https://pubmed.ncbi.nlm.nih.gov/20585380/)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Scientometrics&title=Software%20survey:%20VOSviewer,%20a%20computer%20program%20for%20bibliometric%20mapping&author=N.J.%20Van%20Eck&author=L.%20Waltman&volume=84&issue=2&publication_year=2010&pages=523-538&pmid=20585380&doi=10.1007/s11192-009-0146-3&)\]

[^20]: 19.Vieira E., Gomes J. A comparison of Scopus and Web of Science for a typical university. Scientometrics. 2009;81(2):587–600. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Scientometrics&title=A%20comparison%20of%20Scopus%20and%20Web%20of%20Science%20for%20a%20typical%20university&author=E.%20Vieira&author=J.%20Gomes&volume=81&issue=2&publication_year=2009&pages=587-600&)\]

[^21]: 20.Wohlin C., Runeson P., Höst M., Ohlsson M.C., Regnell B., Wesslén A. Springer Science & Business Media; 2012. Experimentation in software engineering. a. \[[Google Scholar](https://scholar.google.com/scholar_lookup?Wohlin%20C.,%20Runeson%20P.,%20H%C3%B6st%20M.,%20Ohlsson%20M.C.,%20Regnell%20B.,%20Wessl%C3%A9n%20A.%20Springer%20Science%20&%20Business%20Media;%202012.%20Experimentation%20in%20software%20engineering.%20a.)\]

[^22]: 21.Wohlin C., Runeson P., Höst M., Ohlsson M.C., Regnell B., Wesslén A. Experimentation in Software Engineering. Springer; Berlin Heidelberg: 2012. Systematic Literature Reviews; pp. 45–54. \[[DOI](https://doi.org/10.1007/978-3-642-29044-2_4)\] \[[Google Scholar](https://scholar.google.com/scholar_lookup?title=Experimentation%20in%20Software%20Engineering&author=C.%20Wohlin&author=P.%20Runeson&author=M.%20H%C3%B6st&author=M.C.%20Ohlsson&author=B.%20Regnell&publication_year=2012&)\]

[^23]: 22.Yang L., Zhang H., Shen H., Huang X., Zhou X., Rong G., Shao D. Quality assessment in systematic literature reviews: A software engineering perspective. Inf. Softw. Technol. 2021;130 \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Inf.%20Softw.%20Technol.&title=Quality%20assessment%20in%20systematic%20literature%20reviews:%20A%20software%20engineering%20perspective&author=L.%20Yang&author=H.%20Zhang&author=H.%20Shen&author=X.%20Huang&author=X.%20Zhou&volume=130&publication_year=2021&)\]

[^24]: 23.Zahabi M., Razak Abdul, A M. Adaptive virtual reality-based training: A systematic literature review and framework. Augmented Reality, Virtual Reality, Comput. Graphics, Int. Conf., AVR 2020, Proc., 7th. 2020;24(4):725–752. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Augmented%20Reality,%20Virtual%20Reality,%20Comput.%20Graphics,%20Int.%20Conf.,%20AVR%202020,%20Proc.,%207th&title=Adaptive%20virtual%20reality-based%20training:%20A%20systematic%20literature%20review%20and%20framework&author=M.%20Zahabi&author=Abdul%20Razak&author=M%20A&volume=24&issue=4&publication_year=2020&pages=725-752&)\]

[^25]: 24.Zheng P., Wang Z., Chen C.-H., Khoo L.P. A survey of smart product-service systems: Key aspects, challenges and future perspectives. Adv. Eng. Inf. 2019;42 \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Adv.%20Eng.%20Inf.&title=A%20survey%20of%20smart%20product-service%20systems:%20Key%20aspects,%20challenges%20and%20future%20perspectives&author=P.%20Zheng&author=Z.%20Wang&author=C.-H.%20Chen&author=L.P.%20Khoo&volume=42&publication_year=2019&)\]

[^26]: 25.Zhou Y., Zhang H., Huang X., Yang S., Babar M.A., Tang H. Proceedings of the 19th International Conference on Evaluation and Assessment in Software Engineering. 2015. Quality assessment of systematic reviews in software engineering: A tertiary study; pp. 1–14. \[[Google Scholar](https://scholar.google.com/scholar_lookup?title=Proceedings%20of%20the%2019th%20International%20Conference%20on%20Evaluation%20and%20Assessment%20in%20Software%20Engineering&author=Y.%20Zhou&author=H.%20Zhang&author=X.%20Huang&author=S.%20Yang&author=M.A.%20Babar&publication_year=2015&)\]

[^27]: 26.Okoli, C., & Schabram, K. (2010). A guide to conducting a systematic literature review of information systems research.

[^28]: 27.Petersen K., Vakkalanka S., Kuzniarz L. Guidelines for conducting systematic mapping studies in software engineering: An update. Information and software technology. 2015;64:1–18. \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Information%20and%20software%20technology&title=Guidelines%20for%20conducting%20systematic%20mapping%20studies%20in%20software%20engineering:%20An%20update&author=K.%20Petersen&author=S.%20Vakkalanka&author=L.%20Kuzniarz&volume=64&publication_year=2015&pages=1-18&)\]

[^29]: 28.Rowley J., Slack F. Conducting a literature review. Management research news. 2004 \[[Google Scholar](https://scholar.google.com/scholar_lookup?journal=Management%20research%20news&title=Conducting%20a%20literature%20review&author=J.%20Rowley&author=F.%20Slack&publication_year=2004&)\]