---
title: "Software engineering principles: A systematic mapping study and a quantitative literature review"
source: "https://www.sciencedirect.com/science/article/pii/S221509862034252X?utm_source=chatgpt.com"
author:
  - "[[Software engineering]]"
  - "[[Alain Abran]]"
published:
created: 2026-11-24
description: "Software engineering, a fairly recent engineering discipline, is still evolving without a wide consensus on a body of fundamental principles as in tra…"
tags:
  - "clippings"
---
### Published by

[![Society Logo](https://ars.els-cdn.com/content/image/DHosted.gif)](https://www.sciencedirect.com/journal/engineering-science-and-technology-an-international-journal)

Society Logo

## Review

Author links open overlay panel,,

[View **PDF**](https://www.sciencedirect.com/science/article/pii/S221509862034252X/pdfft?md5=9d09048287ace5699a0845571454e62e&pid=1-s2.0-S221509862034252X-main.pdf)

[10.1016/j.jestch.2020.11.005](https://doi.org/10.1016/j.jestch.2020.11.005)

## Keywords

Software engineering

;

Software engineering principles

;

Principles development process

;

Systematic mapping study – SMS

- [Previous article in this issue](https://www.sciencedirect.com/science/article/pii/S2215098620342385)
- [Next article in this issue](https://www.sciencedirect.com/science/article/pii/S2215098620342609)

## 1\. Introduction

Software engineering (SE) emerged as a discipline in the late 70s and early 80s. The SWEBOK Guide - ISO 19759 defines software engineering (SE) as “the application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software”.

Much of the research in software engineering has focused on developing methods, techniques and tools, and much less research on exploring the foundations of software engineering, including identifying fundamental principles.

In our previous work,, we had discussed some of the similarities and differences between SE and other engineering disciplines: it investigated this issue by comparing the design concept in traditional engineering as described in Vincenti to the design concept for software defined in the SWEBOK Guide. The result of the analysis indicated that the design issue in traditional engineering is not limited to the design issue in software: it goes beyond that, in that it is composed of the whole of the [SE life cycle](https://www.sciencedirect.com/topics/engineering/life-cycle-assessment).

Fundamental principles are used in the establishment of a discipline. Yet, SE still lacks a set of broadly recognized fundamental principles and, in that respect, is not as mature as other engineering fields such as mechanical and electrical engineering.

A fundamental principle is less precise and more permanent than methodologies and techniques. According to the Cambridge University Dictionary, the term “fundamental” means forming the base from which everything else originates; more important than anything else, and “principle” means a basic idea or rule that explains or controls how something happens or works.

Principles are conceptual statements describing the needed properties of products and processes, which can be realized by using methods and techniques, often enforced by tools. Principles should have a strong impact on the [engineering process](https://www.sciencedirect.com/topics/chemical-engineering/process-engineering) and, correspondingly, on the final product.

They should also enable improvement of an engineering product in such a way that it possesses all the needed qualities, like functionality, while permitting non-functional constraints and user needs to be defined better, faster and at lower product cost to improve quality and time to market. So SE was analysed from an engineering perspective,, based on Vincenti’s categories of [engineering knowledge](https://www.sciencedirect.com/topics/computer-science/knowledge-engineering). Bourque et al. noted that the methods, techniques and tools used for developing software undergo rapid change within a short period of time, while Ghezzi et al. observed that the SE discipline cannot rely on methods, techniques and tools, rather it should depend on a stable set of fundamental principles.

This paper reports on a [systematic mapping study](https://www.sciencedirect.com/topics/computer-science/systematic-mapping-study) (SMS) to identify, analyse and characterize the research to date on software engineering principles (SEP).

As presented by Kitchenham et al., a systematic map is a process that focusses on building a classification structure and categorizing the key research studies in a specific field respecting established and well-defined criteria. Consequently, SMS studies provide researchers with up-to date summary knowledge of the research conducted on specific topics. To our knowledge there has been no SMS analyzing the SEP studies published to date.

This SMS aims to assist the SE community to establish a foundation for the discipline through a methodological approach. First it performs a systematic search of the studies on SEP between 1969 and January 2020, then through a set of four mapping questions, it structures and classifies these studies using a set of well-defined criteria.

The SMS findings will assist SE researchers to understand the state of the art on SEP studies and guide them to best practices.

The rest of the paper is structured as follows. presents the research methodology. presents individual summaries of the selected studies and, the details of the data synthesis for the mapping questions. discusses threats to validity. presents the summary results of this SMS study followed by a Discussion and some future work in.

## 2\. Research methodology

The aim of an SMS is to specify the research trends for a specific topic and then categorize research with respect to well-defined criteria. In this paper, the SMS process recommended by Kitchenham et al. and García-Holgado are followed, which includes five steps: 1) define the mapping questions related to specific topic, 2) perform a comprehensive search strategy for candidate studies, 3) select studies using inclusion and exclusion criteria, 4) extract the required data, and 5) synthesize the required data. illustrates the [systematic mapping](https://www.sciencedirect.com/topics/computer-science/systematic-mapping) process for this study.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr1.jpg)

Download: Download high-res image (460KB)

### 2.1. Research mapping questions

Following the first SMS planning step, the following four research mapping questions (MQs), together with their related motivation were established - see.
- MQ1: What are the publication trends in SEP studies?
- MQ2: Who used explicit criteria to identify SEP?
- MQ3: Who built their principles based on a defined methodology process?
- MQ4: Which software engineering principles are applicable throughout the development process?

Table 1. Research mapping questions and motivation.

| MQ no. | Research mapping questions | Motivation |
| --- | --- | --- |
| MQ1 | What are the publication trends in published SEP studies? | To discover the key SEP studies published over the period covered. |
| MQ2 | Who used explicit criteria to identify SEP? | To discover the criteria used to select the SEP. |
| MQ3 | Who built their principles based on a defined methodology? | To discover the SEP studies based only on opinions and those on a defined methodology. |
| MQ4 | Which software engineering principles are applicable throughout the development process (DP)? | To discover which studies documented and illustrated their use throughout the software development lifecycle. |

Classification criteria were then identified to structure and categorize the SEP studies within publication trends, publication channels and publication venues. The corresponding descriptions are presented in.

Table 2. Classification criteria.

<table><thead><tr><th colspan="2">Properties</th><th>Categories</th></tr></thead><tbody><tr><td rowspan="3">Research publication in (SEP)</td><td>Publication trend</td><td>Author (s)<br>Title<br>Publication year<br>Number of proposed SEP within each publication<br>Number of citations within each publication</td></tr><tr><td>Publication channel</td><td>Publication types:<br>Journal namesConference names<br>Book names</td></tr><tr><td>Publication venue</td><td>Research approaches<br>Research contribution</td></tr><tr><td>Research criteria</td><td colspan="2">Published studies that used criteria once SEP context identified.<br>Published studies that did not use criteria once SEP context identified.</td></tr><tr><td>Research methodology</td><td colspan="2">Published studies that list SEP and were built based on a methodology.<br>Published studies that list SEP and were built without using a methodology.</td></tr><tr><td>Development process</td><td colspan="2">SEP applicable for use throughout the development process.<br>SEP not applicable for use throughout the development process.</td></tr></tbody></table>

### 2.2. Perform the search strategy

The purpose of this step was to identify the studies relevant to the mapping questions. To implement the search strategy the following electronic databases Science Direct, IEEE Xplore, ACM Digital Library, Springer, Wiley online library were used as primary public databases, and Google Scholar as a secondary public database. The searches were limited to the studies published between 1969 and January 2020.

The selected major primary public databases were considered due to their high impact factor, while Google Scholar was used because it contains some papers that might not have been published in the primary public databases; in addition, some studies may have been published earlier than 1969–1979.

To perform the search strategy using the six databases, a well-defined search string was built from the key terms used in the mapping questions and alternative words for the key terms. The [Boolean operators](https://www.sciencedirect.com/topics/computer-science/boolean-operator) OR and AND were used to associate the key terms. The final search string was expressed as follows:

(“software engineering principles” OR SEP) AND (“principles process in software engineering”) AND (“ principles criteria in software engineering”) AND (“principles in software development”) AND (“fundamental principle in software engineering”).

1st: The search was executed in the six electronic and digital databases directly with the above search string to find candidate studies.

2nd: Duplicate studies were removed and then titles and abstracts were screened to exclude unrelated papers. If needed, the whole study was examined. In addition, the reference list of each of the relevant studies was scanned to check whether an SEP study meeting the classification criteria had been missed in the first phase.

### 2.3. Study selection using inclusion & exclusion criteria

This section presents the inclusion and exclusion criteria used for selecting the relevant studies through analysis of the candidate studies using the title, abstract and keywords for each study to decide on their relevance to the topic of this SMS - see:

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr2.jpg)

Download: Download high-res image (323KB)

Inclusion criteria: paper or book discussing directly the SEP, applied SEP in practice, criteria used for SEP and processes used within the SEP.

Exclusion criteria: papers or books discussing indirectly the SEP, SEP applied randomly in practice, SEP viewed broadly and process used, and/or criteria, without defining the SEP.

During the selection phase the following activities were carried out to identify the candidate studies:

Meetings of three of the four of authors of this paper for the selection process phase.

The three researchers collectively identified the candidate studies as included or excluded.

The three researchers found that there were some studies categorised as undefined (i.e. they used some of the proposed SEP in their publications from different studies without proposing their own principles).

The three researchers analysed the studies by reading the full text then discussed the MQs until reaching a consensus on acceptance of a candidate study.

### 2.4. Data extraction method

The data extraction method was used and finalized by three researchers for each selected study. illustrates the data extraction method for this SMS. The extracted data was synthesized and summarized to prepare the answers for each MQ. A representation [synthesis method](https://www.sciencedirect.com/topics/engineering/synthesis-method) was used with visualization charts to expand the presentation of the results obtained and simplify their interpretation.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr3.jpg)

Download: Download high-res image (302KB)

### 2.5. Results of the selection of studies

illustrates the data extraction results using the selection criteria as follows:

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr4.jpg)

Download: Download high-res image (596KB)

Using an automatic search string on the six online databases, the number of studies extracted from each online database are as follows: 75, 110, 89, 42, 25, and 124 respectively - (step 1).

The total number of candidate studies without duplicates resulted in 465 primary studies - (step 2).

To identify the relevant studies, the following sub steps were used for inclusion and exclusion criteria - (step 3):

Applying the [inclusion criteria](https://www.sciencedirect.com/topics/computer-science/inclusion-criterion) resulted in 45 relevant primary studies. (For more details see.)

The 45 studies were checked for studies proposing the same principles (SEP), leading to removal of seven studies and ending with 38 studies. (For more details see.)

Applying the exclusion criteria by eliminating duplicate studies and those not related to the SEP topic resulted in 420 studies rejected.

Finally, in step 4: The full text reading led to the exclusion of eight studies for a final set of 30 selected studies. (For more details see.)

From the 30 selected studies, reading led to the identification of 592 SEP.

## 3\. Individual summaries of selected studies

This section presents individual summaries of the 30 studies selected in the previous steps.

P1: Royce 1970: In 1983 Boehm reported that for large software projects the Royce corporation had introduced one of the early discussions on software principles and proposed five rules or steps to follow based on their professional experience in spacecraft [software projects management](https://www.sciencedirect.com/topics/computer-science/project-management-software).

P2: In 1975 seven SEP were introduced by Ross and Irvine related to four fundamental goals (e.g. modifiability, efficiency, reliability, and understandability). The defined principles and goals dealt with various steps of the software development process such as purpose, concepts, mechanism, notation and usage. The authors did not define any criteria for establishing the principles. However, they illustrated the practical use of their framework by applying it to [subroutine call](https://www.sciencedirect.com/topics/computer-science/subroutine-call) notation issues.

P3: Mills defined two principles for design and divided software engineering into three categories: design, development and management. He did not provide any definition of principle, nor did he define any criteria for identifying them.

P4: Lehman introduced five ‘laws’ in 1980 for the evolution of software systems, in particular, for the maintenance of software. Based on his analysis and synthesis of data over seven years of maintenance projects, he suggested that these laws would assist in the development of [management tools](https://www.sciencedirect.com/topics/computer-science/management-tool). In addition, Lehman’s opinion was that the laws defined for software engineering should have less precision than natural laws.

P5: Boehm explicitly referred to the search of basic principles and introduced seven SEP in 1983. He also defined two criteria for identifying them. However, the term ‘principle’ was not explicitly defined. His principles were identified based on his own synthesis of [historical data](https://www.sciencedirect.com/topics/engineering/historical-data) for different software projects.

P6: Brooks defined four basic constraints for software engineering derived from his conclusion that there is no particular methodology or tool that can solve all fundamental problems in software engineering.

P7: Parnas identified five principles he considered important for the software engineering discipline.

P8: Hoare identified seven generic principles for the software engineering discipline.

P9: Booch et al. defined software engineering as follows: “Software engineering is the application of sound engineering principles to the development of systems that are modifiable, efficient, reliable, and understandable.” They proposed seven basic principles linked to the goals mentioned in the above definition. Their principles focused on the ADA programming language issues. No definition was given for the term ‘principle’, neither did they describe a methodology, nor provide criteria for the definition of principles.

P10: Davis identified the 15 most important principles of software engineering but did not provide any criteria for their identification nor a methodology.

P11: In 1995 Davis published the first collection of principles of software development. He defined the term ‘principle’ and organized the collection into eight categories: general principles, [requirements engineering](https://www.sciencedirect.com/topics/computer-science/requirement-engineering) principles, design principles, coding principles, testing principles, management principles, product assurance principles and evolution principles. Furthermore, he stated: “I make no claim that these 201 principles are mutually exclusive… a combination of some of these principles may simplify each other”. (See.)

P12: Wasserman stated that some fundamental concepts appear unchanging despite the rapid change in software development, thus these concepts may form a basic foundation for software engineering. He identified eight fundamental concepts claimed to be a sound foundation for the software engineering discipline. However, he did not provide any definition of fundamental concepts.

P13: Bushmann et al. stated that the construction of software should be founded on “fundamental principles”. They identified eleven important principles for designing and constructing software but did not provide any definition for the term ‘principle’. Neither did they define any criteria, nor describe how the principles were defined.

P14: Wiegers defined 14 principles for software engineering that may affect the software engineering culture of an organization. Wiegers did not define the term ‘principle’ nor the criteria for defining principles. He mentioned that the principles support the development practices which should improve the quality as well as the efficiency of the software [engineering process](https://www.sciencedirect.com/topics/chemical-engineering/process-engineering) and the software products.

P15: Hooker described seven principles for the practice of software engineering.

P16: Jabir and Moore: Jabir is a surname given to a group of experts who participated in a 1996 IEEE workshop where the authors identified eight candidate principles, collectively, through a workshop process.

P17: [Mc](https://www.sciencedirect.com/topics/materials-science/moscovium) Connell,, the IEEE software editor, selected eleven principles for software engineering, as reported in the IEEE software magazine on principles of software engineering.

P18: Maibaum posited that software engineering must have mathematical foundations like the other mature engineering disciplines to be legitimately considered as an engineering discipline. He mentioned that software should be based on a normal design by making use of more readymade components. To deal with the continually increasing complexity of software, he proposed the principle of modularization. However, he did not define the mathematical foundations, nor foundations for the software engineering discipline but did describe categories of [engineering knowledge](https://www.sciencedirect.com/topics/computer-science/knowledge-engineering) inspired by Vincenti’s work to improve the software engineering discipline and implicitly referred to three principles.

P19: Taylor described ten design principles that had been previously defined by Mayall in 1979.

P20: Meyer defined a principle as “a long-lasting concept that underlies the whole discipline.” For Mayer, the term ‘principle’ and concept appear to be identical. Meyer proposed 13 principles that constitute the foundation for software engineering. He mentioned that these principles should constitute part of software engineering curricula and knowledge that students receive.

P21: Bourque et al. and Bourque and Dupuis proposed a documented methodology, application of which led to a set of 15 SEP. Their research methodology incorporated two IEEE sponsored workshops and two Delphi studies with multiple rounds, as well as a web-based survey conducted among members of the Technical Council on Software Engineering of the IEEE Computer Society. Overall, more than 560 people were involved in one or more of the Delphi steps.

P22: Baskerville et al. developed practices and principles for internet speed applications. Their study reported that internet speed application practices were different from traditional engineering practices. The methodology was composed of two phases:

Phase 1: [Case studies](https://www.sciencedirect.com/topics/computer-science/case-study) of internet speed software development were used.

Phase 2: A discovery colloquium on internet speed development.

A comparison between the SEP in Bourque et al. and the internet speed development principles, led them to conclude that internet speed development practices were compatible with agile principles.

P23: Ghezzi et al. identified seven SEP. The authors used their set of SEPs with applications on how to attain the [quality objectives](https://www.sciencedirect.com/topics/engineering/quality-objective) for design, specification and the management of software engineering.

P24: Abran et al.,, and Séguin et al., inventoried from the literature on SEP an initial set of 313 principles proposed in the work of individual authors,,,,,,,,. Then, to verify whether any of the 313 proposed principles were indeed a candidate fundamental principle, a two-step [verification process](https://www.sciencedirect.com/topics/computer-science/verification-process) was used by Séguin, followed by Séguin, Abran and Dupuis. This synthesis led to a final set of 24 candidate SEP.

P25: Wang inventoried 55 SEP from a number of studies and proposed a framework of 31 SEP through a mapping between these 31 proposed SEP and 14 basic software engineering constraints classified into three categories: cognitive constraints, organizational constraints and [resource constraints](https://www.sciencedirect.com/topics/computer-science/resource-constraint).

P26: Meyer described seven principles for software testing but did not define the term ‘principle’, nor did they provide criteria or documented methodology.

P27: Meridji and Abran, analyzed the 34 candidate SEP from Seguin et al. from an engineering perspective. A four-phase methodology was designed to analyse and consolidate these 34 candidate fundamental principles using both engineering criteria derived from the engineering categories of knowledge defined by Vincenti and the engineering criteria defined by the [joint](https://www.sciencedirect.com/topics/engineering/joints-structural-components) IEEE and ACM software engineering curriculum. The result was the definition of nine SEP conforming to engineering criteria. In addition, a tree structure hierarchy was proposed composed of specific [instantiations](https://www.sciencedirect.com/topics/engineering/instantiation) of the candidate fundamental principles.

P28: Pressman proposed a number of principles for software engineers to be applied throughout the development process such as problem analysis, designing, constructing and testing a solution. (See.)

P29: Al-Sarayreh and Meridji used the nine SEP in P28. Using a case study, they applied them to the development of an operational process for software requirements for renewable energy software.

P30: Martin proposed 12 SEP according to the properties that distinguish agile regular practices from a non-agile process.

## 4\. Data synthesis for the mapping questions

This section presents a synthesis of the data extraction from the 30 selected studies using the four mapping questions and their classification criteria.

### 4.1. Data synthesis for MQ1 on SEP

This section presents the answers to the first mapping question (MQ1) using the classification criteria in: publication trends, channels and venues.

#### 4.1.1. Publication trends MQ1

The publication trend of SEP studies is presented in with the number of SEP studies published per decade from 1969 to January 2020. In summary, the majority of the studies (20 out of 30, or 65%) were published over two decades from 1989 to 2009. The publication rate then slowed in the following decade.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr5.jpg)

Download: Download high-res image (97KB)

shows the number of proposed SEP per study per year, for a total of 592 SEP proposed over the five decades, distributed as follows by decade:
- 1969–1979: 12
- 1979–1989: 25
- 1989–1999: 287
- 1999–2009: 138
- 2009–2020: 130.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr6.jpg)

Download: Download high-res image (442KB)

shows the authors of the SEP studies. The author who proposed the largest number of SEP, by far, was Davis who first introduced 15 principles in study P10 and then 201 in study P11. Next Pressman proposed 107 SEP in study P28.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr7.jpg)

Download: Download high-res image (586KB)

In contrast, in study P24 Séguin and Abran, introduced 34 principles, then reduced this list through more in-depth analysis and criteria to 24 principles, and to nine principles in P27.

All other authors in account for only 33% of the total number of SEP.

### 4.2. Data synthesis for MQ2: SEP identified based on criteria

This section presents the answer to MQ2 through an analysis on whether or not explicit criteria had been identified and used to identify selected SEP in the 30 studies for more details see:

Only the following six studies used explicit criteria to identify their proposed SEP (for more details see.):
- Boehm - seven candidate principles;
- Jabir and Moore - eight candidate principles;
- Bourque et al. − 15 candidate principles.
- Abran and Séguin,, respectively − 34 out of a literature inventory of 308, subsequently reduced to 24 candidate principles through additional criteria.
- Meridji and Abran - nine candidate principles using the two sets of criteria's in,.

None of the other 25 studies used explicit criteria to identify their SEP.

### 4.3. Data synthesis for MQ3: authors of SEP that used a methodology process

This section presents the answers to MQ3. The following six studies used a research methodology to identify their proposed SEP for more details see:

Bushman et al., proposed 11 candidate principles using an SMS research methodology.

Wiegers, proposed 11 candidate principles using an SMS research methodology.

Jabir and Moore, proposed eight candidate principles on the basis of a specific workshop on this SEP topic.

Bourque et al., proposed 15 candidate principles using a multi-rounds Delphi research methodology.

Abran and Séguin,, proposed 34 out of an inventory of 308 SEP, subsequently reducing them to a set of 24 candidate SEPs using an SMS research methodology.

Meridji and Abran proposed nine candidate principles using a research methodology based on Vincenti’s categorization of engineering knowledge.

The other studies did not report a methodology process to identify their principles.

### 4.4. Data synthesis for MQ4: SEP applied through the development process

This section presents the answer to MQ4. The following studies proposed an SEP applicable within the development process when they identified SEP within their studies for more details see:

Ghezzi et al. proposed seven candidate principles implemented on quality design specifications in the software engineering domain.

Al-Sarayreh and Meridji used the nine principles in Meridji and Abran, and illustrated their implementation in the software requirements phase.

## 5\. Threats to validity

[Construct validity](https://www.sciencedirect.com/topics/computer-science/construct-validity): the selection of studies used to address the mapping questions (MQs). This selection is dependent on the search strategy including the search string, electronic databases, and the search process used. To mitigate threats to construct validity, a detailed search strategy was used based on the defined four MQs. To select the relevant studies, it was then applied to the predefined six electronic databases using a normal and advanced search found on each electronic database site.

Nevertheless, some studies may not have used the same expressions related to the mapping questions in their titles, abstracts, or keywords. Consequently, a risk of missing some such studies in the normal and advanced search was considered. So, an inclusion and exclusion process was carried out to check by inspection the references of the included studies to find any additional relevant missing studies. This procedure was implemented by three researchers and the variances between them were discussed until a consensus was reached. This, to a significant degree, confirms the validity of the entire search process.

[Internal validity](https://www.sciencedirect.com/topics/computer-science/internal-validity): there is some risk the data extraction process used may be missing some data. To mitigate this threat, the data extraction method used on the selection of studies, as well as answers to the mapping questions, was made independently by the three researchers, and the variances between them discussed until a consensus was reached.

External validity: the findings in this SMS are the conclusions drawn from the data extracted from the selected studies. To mitigate this threat, each study was inspected and/or removed. The findings of this SMS are based on the data extraction method on the selected SEP studies and are considered fair and mirror the recent state of the art.

## 6\. Summary results

Software engineering is a discipline whose aim is the creation of high-quality software. Nevertheless, this engineering field is much less mature than classical engineering disciplines and still lacks its own set of widely recognized fundamental principles.

This study concentrated on the analysis of the SEP studies published between 1969 and January 2020. Four mapping questions were investigated, analysed and interpreted based on the SMS research methodology.

This SMS identified 30 relevant SEP studies. Data were extracted from these studies and combined with respect to the MQs.

In this SMS 592 candidate principles were identified within 30 relevant studies from individual authors and/or [collaborative works](https://www.sciencedirect.com/topics/engineering/collaborative-work) in the field.

The research findings answered the following four mapping questions:

MQ1: What are the publication trends in SEP studies?

In the 30 selected studies, the following trends were identified:

The majority of the studies (20 out of 30, or 65%) were published over two decades from 1989 to 2009, and then the publication rate slowed in the following decade.

A total of 592 SEP was proposed over the five decades.

The largest number of SEP by far was proposed by Davis who first introduced 15 principles in study P10 and then 201 others in study P11. Next was Pressman with 107 SEP in study P28.

In contrast, in study P24 Séguin and Abran introduced 34 principles, which they reduced, through more in-depth analysis and criteria, to 24 principles. This list was then reduced to nine principles in P27 (Meridji and Abran).

Publication channels: 14 of the selected studies were published in refereed journals (45%), nine in books (29%), five in international conferences (16%) and two by other means (10%).

The number of studies per publication venue: journals 14, conferences five, books nine and two in other sources.

In addition, of the 592 SEP identified, many were worded differently but had similar meanings, while a number had conflicting meanings.

MQ2: Who used explicit criteria to identify SEP?

Only five of the 30 studies used explicit criteria to identify their set of SEP: Boehm; Jabir and Moore; Bourque et al.; Abran et al.; Séguin et al.,; Meridji and Abran.

The key SMS findings are: no criteria were given by most authors on how they selected these principles, neither did they identify which principles to use in specific contexts of the software engineering domain.

MQ3: Who built their principles based on a defined methodology process?

Only six studies used a methodology to derive their SEP:

Bushman et al., Wiegers, Abran et al., and Séguin et al., used an SMS research methodology.

Jabir and Moore proposed eight candidate principles at a specific IEEE workshop on SEP.

Bourque et al. proposed 15 candidate principles using a multi-rounds Delphi research methodology.

Meridji and Abran \[\] proposed nine candidate principles using a research methodology based on Vincenti’s categorization of engineering knowledge.

All of the other 24 studies identified their principles based on their own analysis without traceability to a methodology or selection criteria.

MQ4: Which software engineering principles are applicable throughout the development process?

Only Ghezzi et al. proposed seven candidate principles implemented on quality design specifications in the software engineering domain. Al-Sarayreh and Meridji used the nine principles in Meridji and Abran and implemented them in the software requirements phase.

Only two studies in our SMS used some of the proposed SEP within the software development process: one study implemented seven SEP on quality design specifications and the second study implemented its set of nine SEP in the software requirements phase.

## 7\. Discussion

Software engineering principles (SEP) are conceptual statements meant to have a strong impact on the engineering process and, correspondingly, on the final product. SEP should therefore describe the required properties of products and processes. SEP can be realized by using methods and techniques, regularly enforced by different types of [software tools](https://www.sciencedirect.com/topics/computer-science/software-development-tool).

Within these studies a total of 592 SEP were proposed, many expressed differently with similar meanings, and others with conflicting meanings. These studies were reviewed and classified on the basis of four mapping questions examining publication trends, use of explicit criteria for the proposed SEP, whether authors clearly described a methodology to come up with the proposed SEP.

Based on our analysis and observations while conducting this SMS the following insights can be shared:

Most of the proposed SEP are out of context statements, often without detailed definitions. Therefore, their applicability to specific contexts may depend on ideas and opinions of what a specific SEP stands for. Further work is necessary to develop more objective criteria by linking them to [operational software](https://www.sciencedirect.com/topics/computer-science/operational-software) development environments.

Most of the studies on SEP propose principles without attention to definitions and laws linking them to principles as defined in traditional engineering. Further work is needed to investigate how traditional engineering principles can be applied or adapted to SEP principles.

SE researchers have proposed a large number of SEP to practitioners for replicating success of software projects. The SEP in this SMS may eventually have considerable impact on the industry for the improvement of SE processes by enhancing planning, management and development of software at different phases of the [software development life cycle](https://www.sciencedirect.com/topics/computer-science/software-development-lifecycle).

Much additional work is required to reduce the large number of candidate SEP into a smaller comprehensive set using well-defined criteria and processes.

Further work is also needed to describe how proposed SEP can be applied consistently and properly within the development process and how can they can efficiently deliver high-quality applications.

Further research would be useful to improve both the identification and more detailed descriptions of SEP, for example:
- •

	Integrate SEP and practices.
- •

	Have SEP address the system [engineering life cycle](https://www.sciencedirect.com/topics/computer-science/life-cycle-assessment) to requirements, design, architecture, maintenance, programming, testing and transitions.
- •

	Make SEP relevant across application domains and other disciplines such as computer science, economics, people and management skills.
- •

	Define SEP in an objective way and link to real software development environments.
- •

	Ensure each SEP has its own set of definitions and is linked with other SEP as in traditional engineering.

Further [research work](https://www.sciencedirect.com/topics/engineering/research-work) could also be initiated for building an ontology for the SE principles using an artificial intelligent tool. As well as, investigating the similarities between principles such as ones that are similar but are just named differently. In addition to the principles that are conflicting each other.

Furthermore, an examination of which principles work on which problems and their specific application is required.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Appendix A. Supplementary data

The following are the Supplementary data to this article:[Download: Download Word document (22KB)](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-mmc1.docx "Download Word document (22KB)")

Supplementary Data 1.

## References

[^1]: ## 1\. Introduction

Software engineering (SE) emerged as a discipline in the late 70s and early 80s. The SWEBOK Guide - ISO 19759 defines software engineering (SE) as “the application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software”.

Much of the research in software engineering has focused on developing methods, techniques and tools, and much less research on exploring the foundations of software engineering, including identifying fundamental principles.

In our previous work,, we had discussed some of the similarities and differences between SE and other engineering disciplines: it investigated this issue by comparing the design concept in traditional engineering as described in Vincenti to the design concept for software defined in the SWEBOK Guide. The result of the analysis indicated that the design issue in traditional engineering is not limited to the design issue in software: it goes beyond that, in that it is composed of the whole of the [SE life cycle](https://www.sciencedirect.com/topics/engineering/life-cycle-assessment).

Fundamental principles are used in the establishment of a discipline. Yet, SE still lacks a set of broadly recognized fundamental principles and, in that respect, is not as mature as other engineering fields such as mechanical and electrical engineering.

A fundamental principle is less precise and more permanent than methodologies and techniques. According to the Cambridge University Dictionary, the term “fundamental” means forming the base from which everything else originates; more important than anything else, and “principle” means a basic idea or rule that explains or controls how something happens or works.

Principles are conceptual statements describing the needed properties of products and processes, which can be realized by using methods and techniques, often enforced by tools. Principles should have a strong impact on the [engineering process](https://www.sciencedirect.com/topics/chemical-engineering/process-engineering) and, correspondingly, on the final product.

They should also enable improvement of an engineering product in such a way that it possesses all the needed qualities, like functionality, while permitting non-functional constraints and user needs to be defined better, faster and at lower product cost to improve quality and time to market. So SE was analysed from an engineering perspective,, based on Vincenti’s categories of [engineering knowledge](https://www.sciencedirect.com/topics/computer-science/knowledge-engineering). Bourque et al. noted that the methods, techniques and tools used for developing software undergo rapid change within a short period of time, while Ghezzi et al. observed that the SE discipline cannot rely on methods, techniques and tools, rather it should depend on a stable set of fundamental principles.

This paper reports on a [systematic mapping study](https://www.sciencedirect.com/topics/computer-science/systematic-mapping-study) (SMS) to identify, analyse and characterize the research to date on software engineering principles (SEP).

As presented by Kitchenham et al., a systematic map is a process that focusses on building a classification structure and categorizing the key research studies in a specific field respecting established and well-defined criteria. Consequently, SMS studies provide researchers with up-to date summary knowledge of the research conducted on specific topics. To our knowledge there has been no SMS analyzing the SEP studies published to date.

This SMS aims to assist the SE community to establish a foundation for the discipline through a methodological approach. First it performs a systematic search of the studies on SEP between 1969 and January 2020, then through a set of four mapping questions, it structures and classifies these studies using a set of well-defined criteria.

The SMS findings will assist SE researchers to understand the state of the art on SEP studies and guide them to best practices.

The rest of the paper is structured as follows. presents the research methodology. presents individual summaries of the selected studies and, the details of the data synthesis for the mapping questions. discusses threats to validity. presents the summary results of this SMS study followed by a Discussion and some future work in.

## 2\. Research methodology

The aim of an SMS is to specify the research trends for a specific topic and then categorize research with respect to well-defined criteria. In this paper, the SMS process recommended by Kitchenham et al. and García-Holgado are followed, which includes five steps: 1) define the mapping questions related to specific topic, 2) perform a comprehensive search strategy for candidate studies, 3) select studies using inclusion and exclusion criteria, 4) extract the required data, and 5) synthesize the required data. illustrates the [systematic mapping](https://www.sciencedirect.com/topics/computer-science/systematic-mapping) process for this study.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr1.jpg)

Download: Download high-res image (460KB)

### 2.1. Research mapping questions

Following the first SMS planning step, the following four research mapping questions (MQs), together with their related motivation were established - see.
- MQ1: What are the publication trends in SEP studies?
- MQ2: Who used explicit criteria to identify SEP?
- MQ3: Who built their principles based on a defined methodology process?
- MQ4: Which software engineering principles are applicable throughout the development process?

Table 1. Research mapping questions and motivation.

| MQ no. | Research mapping questions | Motivation |
| --- | --- | --- |
| MQ1 | What are the publication trends in published SEP studies? | To discover the key SEP studies published over the period covered. |
| MQ2 | Who used explicit criteria to identify SEP? | To discover the criteria used to select the SEP. |
| MQ3 | Who built their principles based on a defined methodology? | To discover the SEP studies based only on opinions and those on a defined methodology. |
| MQ4 | Which software engineering principles are applicable throughout the development process (DP)? | To discover which studies documented and illustrated their use throughout the software development lifecycle. |

Classification criteria were then identified to structure and categorize the SEP studies within publication trends, publication channels and publication venues. The corresponding descriptions are presented in.

Table 2. Classification criteria.

<table><thead><tr><th colspan="2">Properties</th><th>Categories</th></tr></thead><tbody><tr><td rowspan="3">Research publication in (SEP)</td><td>Publication trend</td><td>Author (s)<br>Title<br>Publication year<br>Number of proposed SEP within each publication<br>Number of citations within each publication</td></tr><tr><td>Publication channel</td><td>Publication types:<br>Journal namesConference names<br>Book names</td></tr><tr><td>Publication venue</td><td>Research approaches<br>Research contribution</td></tr><tr><td>Research criteria</td><td colspan="2">Published studies that used criteria once SEP context identified.<br>Published studies that did not use criteria once SEP context identified.</td></tr><tr><td>Research methodology</td><td colspan="2">Published studies that list SEP and were built based on a methodology.<br>Published studies that list SEP and were built without using a methodology.</td></tr><tr><td>Development process</td><td colspan="2">SEP applicable for use throughout the development process.<br>SEP not applicable for use throughout the development process.</td></tr></tbody></table>

### 2.2. Perform the search strategy

The purpose of this step was to identify the studies relevant to the mapping questions. To implement the search strategy the following electronic databases Science Direct, IEEE Xplore, ACM Digital Library, Springer, Wiley online library were used as primary public databases, and Google Scholar as a secondary public database. The searches were limited to the studies published between 1969 and January 2020.

The selected major primary public databases were considered due to their high impact factor, while Google Scholar was used because it contains some papers that might not have been published in the primary public databases; in addition, some studies may have been published earlier than 1969–1979.

To perform the search strategy using the six databases, a well-defined search string was built from the key terms used in the mapping questions and alternative words for the key terms. The [Boolean operators](https://www.sciencedirect.com/topics/computer-science/boolean-operator) OR and AND were used to associate the key terms. The final search string was expressed as follows:

(“software engineering principles” OR SEP) AND (“principles process in software engineering”) AND (“ principles criteria in software engineering”) AND (“principles in software development”) AND (“fundamental principle in software engineering”).

To confirm that no related works were neglected, the search strategy process was carried out in two phases:

1st: The search was executed in the six electronic and digital databases directly with the above search string to find candidate studies.

2nd: Duplicate studies were removed and then titles and abstracts were screened to exclude unrelated papers. If needed, the whole study was examined. In addition, the reference list of each of the relevant studies was scanned to check whether an SEP study meeting the classification criteria had been missed in the first phase.

### 2.3. Study selection using inclusion & exclusion criteria

This section presents the inclusion and exclusion criteria used for selecting the relevant studies through analysis of the candidate studies using the title, abstract and keywords for each study to decide on their relevance to the topic of this SMS - see:

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr2.jpg)

Download: Download high-res image (323KB)

Inclusion criteria: paper or book discussing directly the SEP, applied SEP in practice, criteria used for SEP and processes used within the SEP.

Exclusion criteria: papers or books discussing indirectly the SEP, SEP applied randomly in practice, SEP viewed broadly and process used, and/or criteria, without defining the SEP.

During the selection phase the following activities were carried out to identify the candidate studies:

Meetings of three of the four of authors of this paper for the selection process phase.

The three researchers collectively identified the candidate studies as included or excluded.

The three researchers found that there were some studies categorised as undefined (i.e. they used some of the proposed SEP in their publications from different studies without proposing their own principles).

The three researchers analysed the studies by reading the full text then discussed the MQs until reaching a consensus on acceptance of a candidate study.

### 2.4. Data extraction method

The data extraction method was used and finalized by three researchers for each selected study. illustrates the data extraction method for this SMS. The extracted data was synthesized and summarized to prepare the answers for each MQ. A representation [synthesis method](https://www.sciencedirect.com/topics/engineering/synthesis-method) was used with visualization charts to expand the presentation of the results obtained and simplify their interpretation.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr3.jpg)

Download: Download high-res image (302KB)

### 2.5. Results of the selection of studies

illustrates the data extraction results using the selection criteria as follows:

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr4.jpg)

Download: Download high-res image (596KB)

Using an automatic search string on the six online databases, the number of studies extracted from each online database are as follows: 75, 110, 89, 42, 25, and 124 respectively - (step 1).

The total number of candidate studies without duplicates resulted in 465 primary studies - (step 2).

To identify the relevant studies, the following sub steps were used for inclusion and exclusion criteria - (step 3):

Applying the [inclusion criteria](https://www.sciencedirect.com/topics/computer-science/inclusion-criterion) resulted in 45 relevant primary studies. (For more details see.)

The 45 studies were checked for studies proposing the same principles (SEP), leading to removal of seven studies and ending with 38 studies. (For more details see.)

Applying the exclusion criteria by eliminating duplicate studies and those not related to the SEP topic resulted in 420 studies rejected.

Finally, in step 4: The full text reading led to the exclusion of eight studies for a final set of 30 selected studies. (For more details see.)

From the 30 selected studies, reading led to the identification of 592 SEP.

## 3\. Individual summaries of selected studies

This section presents individual summaries of the 30 studies selected in the previous steps.

P1: Royce 1970: In 1983 Boehm reported that for large software projects the Royce corporation had introduced one of the early discussions on software principles and proposed five rules or steps to follow based on their professional experience in spacecraft [software projects management](https://www.sciencedirect.com/topics/computer-science/project-management-software).

P2: In 1975 seven SEP were introduced by Ross and Irvine related to four fundamental goals (e.g. modifiability, efficiency, reliability, and understandability). The defined principles and goals dealt with various steps of the software development process such as purpose, concepts, mechanism, notation and usage. The authors did not define any criteria for establishing the principles. However, they illustrated the practical use of their framework by applying it to [subroutine call](https://www.sciencedirect.com/topics/computer-science/subroutine-call) notation issues.

P3: Mills defined two principles for design and divided software engineering into three categories: design, development and management. He did not provide any definition of principle, nor did he define any criteria for identifying them.

P4: Lehman introduced five ‘laws’ in 1980 for the evolution of software systems, in particular, for the maintenance of software. Based on his analysis and synthesis of data over seven years of maintenance projects, he suggested that these laws would assist in the development of [management tools](https://www.sciencedirect.com/topics/computer-science/management-tool). In addition, Lehman’s opinion was that the laws defined for software engineering should have less precision than natural laws.

P5: Boehm explicitly referred to the search of basic principles and introduced seven SEP in 1983. He also defined two criteria for identifying them. However, the term ‘principle’ was not explicitly defined. His principles were identified based on his own synthesis of [historical data](https://www.sciencedirect.com/topics/engineering/historical-data) for different software projects.

P6: Brooks defined four basic constraints for software engineering derived from his conclusion that there is no particular methodology or tool that can solve all fundamental problems in software engineering.

P7: Parnas identified five principles he considered important for the software engineering discipline.

P8: Hoare identified seven generic principles for the software engineering discipline.

P9: Booch et al. defined software engineering as follows: “Software engineering is the application of sound engineering principles to the development of systems that are modifiable, efficient, reliable, and understandable.” They proposed seven basic principles linked to the goals mentioned in the above definition. Their principles focused on the ADA programming language issues. No definition was given for the term ‘principle’, neither did they describe a methodology, nor provide criteria for the definition of principles.

P10: Davis identified the 15 most important principles of software engineering but did not provide any criteria for their identification nor a methodology.

P11: In 1995 Davis published the first collection of principles of software development. He defined the term ‘principle’ and organized the collection into eight categories: general principles, [requirements engineering](https://www.sciencedirect.com/topics/computer-science/requirement-engineering) principles, design principles, coding principles, testing principles, management principles, product assurance principles and evolution principles. Furthermore, he stated: “I make no claim that these 201 principles are mutually exclusive… a combination of some of these principles may simplify each other”. (See.)

P12: Wasserman stated that some fundamental concepts appear unchanging despite the rapid change in software development, thus these concepts may form a basic foundation for software engineering. He identified eight fundamental concepts claimed to be a sound foundation for the software engineering discipline. However, he did not provide any definition of fundamental concepts.

P13: Bushmann et al. stated that the construction of software should be founded on “fundamental principles”. They identified eleven important principles for designing and constructing software but did not provide any definition for the term ‘principle’. Neither did they define any criteria, nor describe how the principles were defined.

P14: Wiegers defined 14 principles for software engineering that may affect the software engineering culture of an organization. Wiegers did not define the term ‘principle’ nor the criteria for defining principles. He mentioned that the principles support the development practices which should improve the quality as well as the efficiency of the software [engineering process](https://www.sciencedirect.com/topics/chemical-engineering/process-engineering) and the software products.

P15: Hooker described seven principles for the practice of software engineering.

P16: Jabir and Moore: Jabir is a surname given to a group of experts who participated in a 1996 IEEE workshop where the authors identified eight candidate principles, collectively, through a workshop process.

P17: [Mc](https://www.sciencedirect.com/topics/materials-science/moscovium) Connell,, the IEEE software editor, selected eleven principles for software engineering, as reported in the IEEE software magazine on principles of software engineering.

P18: Maibaum posited that software engineering must have mathematical foundations like the other mature engineering disciplines to be legitimately considered as an engineering discipline. He mentioned that software should be based on a normal design by making use of more readymade components. To deal with the continually increasing complexity of software, he proposed the principle of modularization. However, he did not define the mathematical foundations, nor foundations for the software engineering discipline but did describe categories of [engineering knowledge](https://www.sciencedirect.com/topics/computer-science/knowledge-engineering) inspired by Vincenti’s work to improve the software engineering discipline and implicitly referred to three principles.

P19: Taylor described ten design principles that had been previously defined by Mayall in 1979.

P20: Meyer defined a principle as “a long-lasting concept that underlies the whole discipline.” For Mayer, the term ‘principle’ and concept appear to be identical. Meyer proposed 13 principles that constitute the foundation for software engineering. He mentioned that these principles should constitute part of software engineering curricula and knowledge that students receive.

P21: Bourque et al. and Bourque and Dupuis proposed a documented methodology, application of which led to a set of 15 SEP. Their research methodology incorporated two IEEE sponsored workshops and two Delphi studies with multiple rounds, as well as a web-based survey conducted among members of the Technical Council on Software Engineering of the IEEE Computer Society. Overall, more than 560 people were involved in one or more of the Delphi steps.

P22: Baskerville et al. developed practices and principles for internet speed applications. Their study reported that internet speed application practices were different from traditional engineering practices. The methodology was composed of two phases:

Phase 1: [Case studies](https://www.sciencedirect.com/topics/computer-science/case-study) of internet speed software development were used.

Phase 2: A discovery colloquium on internet speed development.

A comparison between the SEP in Bourque et al. and the internet speed development principles, led them to conclude that internet speed development practices were compatible with agile principles.

P23: Ghezzi et al. identified seven SEP. The authors used their set of SEPs with applications on how to attain the [quality objectives](https://www.sciencedirect.com/topics/engineering/quality-objective) for design, specification and the management of software engineering.

P24: Abran et al.,, and Séguin et al., inventoried from the literature on SEP an initial set of 313 principles proposed in the work of individual authors,,,,,,,,. Then, to verify whether any of the 313 proposed principles were indeed a candidate fundamental principle, a two-step [verification process](https://www.sciencedirect.com/topics/computer-science/verification-process) was used by Séguin, followed by Séguin, Abran and Dupuis. This synthesis led to a final set of 24 candidate SEP.

P25: Wang inventoried 55 SEP from a number of studies and proposed a framework of 31 SEP through a mapping between these 31 proposed SEP and 14 basic software engineering constraints classified into three categories: cognitive constraints, organizational constraints and [resource constraints](https://www.sciencedirect.com/topics/computer-science/resource-constraint).

P26: Meyer described seven principles for software testing but did not define the term ‘principle’, nor did they provide criteria or documented methodology.

P27: Meridji and Abran, analyzed the 34 candidate SEP from Seguin et al. from an engineering perspective. A four-phase methodology was designed to analyse and consolidate these 34 candidate fundamental principles using both engineering criteria derived from the engineering categories of knowledge defined by Vincenti and the engineering criteria defined by the [joint](https://www.sciencedirect.com/topics/engineering/joints-structural-components) IEEE and ACM software engineering curriculum. The result was the definition of nine SEP conforming to engineering criteria. In addition, a tree structure hierarchy was proposed composed of specific [instantiations](https://www.sciencedirect.com/topics/engineering/instantiation) of the candidate fundamental principles.

P28: Pressman proposed a number of principles for software engineers to be applied throughout the development process such as problem analysis, designing, constructing and testing a solution. (See.)

P29: Al-Sarayreh and Meridji used the nine SEP in P28. Using a case study, they applied them to the development of an operational process for software requirements for renewable energy software.

P30: Martin proposed 12 SEP according to the properties that distinguish agile regular practices from a non-agile process.

## 4\. Data synthesis for the mapping questions

This section presents a synthesis of the data extraction from the 30 selected studies using the four mapping questions and their classification criteria.

### 4.1. Data synthesis for MQ1 on SEP

This section presents the answers to the first mapping question (MQ1) using the classification criteria in: publication trends, channels and venues.

#### 4.1.1. Publication trends MQ1

The publication trend of SEP studies is presented in with the number of SEP studies published per decade from 1969 to January 2020. In summary, the majority of the studies (20 out of 30, or 65%) were published over two decades from 1989 to 2009. The publication rate then slowed in the following decade.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr5.jpg)

Download: Download high-res image (97KB)

shows the number of proposed SEP per study per year, for a total of 592 SEP proposed over the five decades, distributed as follows by decade:
- 1969–1979: 12
- 1979–1989: 25
- 1989–1999: 287
- 1999–2009: 138
- 2009–2020: 130.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr6.jpg)

Download: Download high-res image (442KB)

shows the authors of the SEP studies. The author who proposed the largest number of SEP, by far, was Davis who first introduced 15 principles in study P10 and then 201 in study P11. Next Pressman proposed 107 SEP in study P28.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr7.jpg)

Download: Download high-res image (586KB)

In contrast, in study P24 Séguin and Abran, introduced 34 principles, then reduced this list through more in-depth analysis and criteria to 24 principles, and to nine principles in P27.

All other authors in account for only 33% of the total number of SEP.

#### 4.1.2. Publication channel MQ1

presents the publication channels (MQ1) of the SEP studies: 14 of the selected studies were published in refereed journals (45%), nine in books (29%), five in international conferences (16%) and two by other means (10%).

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr8.jpg)

Download: Download high-res image (107KB)

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr9.jpg)

Download: Download high-res image (266KB)

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr10.jpg)

Download: Download high-res image (239KB)

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr11.jpg)

Download: Download high-res image (249KB)

#### 4.1.3. Publication venue MQ1

,,, show the publication venues of the papers identified in journals, conferences, books and other sources respectively. The number of studies per publication venue is given in the second column of each table.

Table 3. Publication sources of journal papers.

| Publication venue | Number of studies |
| --- | --- |
| IEEE Software | 4 |
| Journal of Systems and Software | 3 |
| IBM Systems Journal | 1 |
| Communications of the ACM | 1 |
| Journal Computer Standards and Interfaces | 1 |
| Software Technologies IEEE | 1 |
| IEEE Computer | 1 |
| International Journal of Software Applications | 1 |
| Journal of Software Engineering and Applications | 1 |

Table 4. Publication sources of [conference papers](https://www.sciencedirect.com/topics/computer-science/conference-paper).

| Publication venue | Number of studies |
| --- | --- |
| Conference on Principles of Software Engineering - PRISE | 1 |
| Conference on Software Engineering, IEEE Computer Society Press | 1 |
| Conference on the Future of Software Engineering. ACM | 1 |
| Conference on Computer Science and Software Engineering, ACM New York, NY, USA | 1 |
| Third International Symposium and Forum on Software Engineering Standards, Walnut Creek, CA | 1 |

Table 5. Publication sources of books.

| Book name | Year | Publisher | Number of studies |
| --- | --- | --- | --- |
| What Engineers Know and How They Know it | 1990 | Johns Hopkins University Press | 1 |
| Fundamentals of Software Engineering | 2003 | New-Jersey: Prentice-Hall. (2nd ed.) | 1 |
| Software Engineering: Process, Principles, and Goals | 1980 | Computer Softech Inc. | 1 |
| Software Engineering with Ada | 1994 | (3rd ed.) California: Benjamin/Cummings Publishing | 1 |
| 201 Principles of Software Development | 1995 | New-York: McGraw-Hill. | 1 |
| Pattern-Oriented Software Architecture | 1996 | Wiley and Sons | 1 |
| Creating a Software Engineering Culture | 1996 | New York: Dorset House Publishing. | 1 |
| Software Engineering: A Practitioners Approach, | 2018 | 9 ed. (McGraw-Hill). | 1 |
| Agile Software Development: Principles, Patterns, and Practices | 2002 | Pearson; International edition | 1 |

Table 6. Publication sources of others.

| Publication venue | Source | Number of studies |
| --- | --- | --- |
| Analysis of Software Engineering from an Engineering Perspective | PhD thesis – École de Technologie Supérieure - University of Québec, Canada, 2009 | 1 |
| Hints on Programming Language Design | Reprinted in Essays in Computing Science, ed. C.B Jones, Prentice Hall International, 1989 | 1 |
| Seven principles of software development | [https://lingualeo.com/pt/jungle/seven-principles-of-software-development-by-david-hooker-48432](https://lingualeo.com/pt/jungle/seven-principles-of-software-development-by-david-hooker-48432)., 1996 | 1 |

### 4.2. Data synthesis for MQ2: SEP identified based on criteria

This section presents the answer to MQ2 through an analysis on whether or not explicit criteria had been identified and used to identify selected SEP in the 30 studies for more details see:

Only the following six studies used explicit criteria to identify their proposed SEP (for more details see.):
- Boehm - seven candidate principles;
- Jabir and Moore - eight candidate principles;
- Bourque et al. − 15 candidate principles.
- Abran and Séguin,, respectively − 34 out of a literature inventory of 308, subsequently reduced to 24 candidate principles through additional criteria.
- Meridji and Abran - nine candidate principles using the two sets of criteria's in,.

None of the other 25 studies used explicit criteria to identify their SEP.

### 4.3. Data synthesis for MQ3: authors of SEP that used a methodology process

This section presents the answers to MQ3. The following six studies used a research methodology to identify their proposed SEP for more details see:

Bushman et al., proposed 11 candidate principles using an SMS research methodology.

Wiegers, proposed 11 candidate principles using an SMS research methodology.

Jabir and Moore, proposed eight candidate principles on the basis of a specific workshop on this SEP topic.

Bourque et al., proposed 15 candidate principles using a multi-rounds Delphi research methodology.

Abran and Séguin,, proposed 34 out of an inventory of 308 SEP, subsequently reducing them to a set of 24 candidate SEPs using an SMS research methodology.

Meridji and Abran proposed nine candidate principles using a research methodology based on Vincenti’s categorization of engineering knowledge.

The other studies did not report a methodology process to identify their principles.

### 4.4. Data synthesis for MQ4: SEP applied through the development process

This section presents the answer to MQ4. The following studies proposed an SEP applicable within the development process when they identified SEP within their studies for more details see:

Ghezzi et al. proposed seven candidate principles implemented on quality design specifications in the software engineering domain.

Al-Sarayreh and Meridji used the nine principles in Meridji and Abran, and illustrated their implementation in the software requirements phase.

## 5\. Threats to validity

[Construct validity](https://www.sciencedirect.com/topics/computer-science/construct-validity): the selection of studies used to address the mapping questions (MQs). This selection is dependent on the search strategy including the search string, electronic databases, and the search process used. To mitigate threats to construct validity, a detailed search strategy was used based on the defined four MQs. To select the relevant studies, it was then applied to the predefined six electronic databases using a normal and advanced search found on each electronic database site.

Nevertheless, some studies may not have used the same expressions related to the mapping questions in their titles, abstracts, or keywords. Consequently, a risk of missing some such studies in the normal and advanced search was considered. So, an inclusion and exclusion process was carried out to check by inspection the references of the included studies to find any additional relevant missing studies. This procedure was implemented by three researchers and the variances between them were discussed until a consensus was reached. This, to a significant degree, confirms the validity of the entire search process.

[Internal validity](https://www.sciencedirect.com/topics/computer-science/internal-validity): there is some risk the data extraction process used may be missing some data. To mitigate this threat, the data extraction method used on the selection of studies, as well as answers to the mapping questions, was made independently by the three researchers, and the variances between them discussed until a consensus was reached.

External validity: the findings in this SMS are the conclusions drawn from the data extracted from the selected studies. To mitigate this threat, each study was inspected and/or removed. The findings of this SMS are based on the data extraction method on the selected SEP studies and are considered fair and mirror the recent state of the art.

## 6\. Summary results

Software engineering is a discipline whose aim is the creation of high-quality software. Nevertheless, this engineering field is much less mature than classical engineering disciplines and still lacks its own set of widely recognized fundamental principles.

This study concentrated on the analysis of the SEP studies published between 1969 and January 2020. Four mapping questions were investigated, analysed and interpreted based on the SMS research methodology.

This SMS identified 30 relevant SEP studies. Data were extracted from these studies and combined with respect to the MQs.

In this SMS 592 candidate principles were identified within 30 relevant studies from individual authors and/or [collaborative works](https://www.sciencedirect.com/topics/engineering/collaborative-work) in the field.

The research findings answered the following four mapping questions:

MQ1: What are the publication trends in SEP studies?

In the 30 selected studies, the following trends were identified:

The majority of the studies (20 out of 30, or 65%) were published over two decades from 1989 to 2009, and then the publication rate slowed in the following decade.

A total of 592 SEP was proposed over the five decades.

The largest number of SEP by far was proposed by Davis who first introduced 15 principles in study P10 and then 201 others in study P11. Next was Pressman with 107 SEP in study P28.

In contrast, in study P24 Séguin and Abran introduced 34 principles, which they reduced, through more in-depth analysis and criteria, to 24 principles. This list was then reduced to nine principles in P27 (Meridji and Abran).

Publication channels: 14 of the selected studies were published in refereed journals (45%), nine in books (29%), five in international conferences (16%) and two by other means (10%).

The number of studies per publication venue: journals 14, conferences five, books nine and two in other sources.

In addition, of the 592 SEP identified, many were worded differently but had similar meanings, while a number had conflicting meanings.

MQ2: Who used explicit criteria to identify SEP?

Only five of the 30 studies used explicit criteria to identify their set of SEP: Boehm; Jabir and Moore; Bourque et al.; Abran et al.; Séguin et al.,; Meridji and Abran.

The key SMS findings are: no criteria were given by most authors on how they selected these principles, neither did they identify which principles to use in specific contexts of the software engineering domain.

MQ3: Who built their principles based on a defined methodology process?

Only six studies used a methodology to derive their SEP:

Bushman et al., Wiegers, Abran et al., and Séguin et al., used an SMS research methodology.

Jabir and Moore proposed eight candidate principles at a specific IEEE workshop on SEP.

Bourque et al. proposed 15 candidate principles using a multi-rounds Delphi research methodology.

Meridji and Abran \[\] proposed nine candidate principles using a research methodology based on Vincenti’s categorization of engineering knowledge.

All of the other 24 studies identified their principles based on their own analysis without traceability to a methodology or selection criteria.

MQ4: Which software engineering principles are applicable throughout the development process?

Only Ghezzi et al. proposed seven candidate principles implemented on quality design specifications in the software engineering domain. Al-Sarayreh and Meridji used the nine principles in Meridji and Abran and implemented them in the software requirements phase.

Only two studies in our SMS used some of the proposed SEP within the software development process: one study implemented seven SEP on quality design specifications and the second study implemented its set of nine SEP in the software requirements phase.

## 7\. Discussion

Software engineering principles (SEP) are conceptual statements meant to have a strong impact on the engineering process and, correspondingly, on the final product. SEP should therefore describe the required properties of products and processes. SEP can be realized by using methods and techniques, regularly enforced by different types of [software tools](https://www.sciencedirect.com/topics/computer-science/software-development-tool).

Within these studies a total of 592 SEP were proposed, many expressed differently with similar meanings, and others with conflicting meanings. These studies were reviewed and classified on the basis of four mapping questions examining publication trends, use of explicit criteria for the proposed SEP, whether authors clearly described a methodology to come up with the proposed SEP.

Based on our analysis and observations while conducting this SMS the following insights can be shared:

Most of the proposed SEP are out of context statements, often without detailed definitions. Therefore, their applicability to specific contexts may depend on ideas and opinions of what a specific SEP stands for. Further work is necessary to develop more objective criteria by linking them to [operational software](https://www.sciencedirect.com/topics/computer-science/operational-software) development environments.

Most of the studies on SEP propose principles without attention to definitions and laws linking them to principles as defined in traditional engineering. Further work is needed to investigate how traditional engineering principles can be applied or adapted to SEP principles.

SE researchers have proposed a large number of SEP to practitioners for replicating success of software projects. The SEP in this SMS may eventually have considerable impact on the industry for the improvement of SE processes by enhancing planning, management and development of software at different phases of the [software development life cycle](https://www.sciencedirect.com/topics/computer-science/software-development-lifecycle).

Much additional work is required to reduce the large number of candidate SEP into a smaller comprehensive set using well-defined criteria and processes.

Further work is also needed to describe how proposed SEP can be applied consistently and properly within the development process and how can they can efficiently deliver high-quality applications.

Further research would be useful to improve both the identification and more detailed descriptions of SEP, for example:
- •

	Integrate SEP and practices.
- •

	Have SEP address the system [engineering life cycle](https://www.sciencedirect.com/topics/computer-science/life-cycle-assessment) to requirements, design, architecture, maintenance, programming, testing and transitions.
- •

	Make SEP relevant across application domains and other disciplines such as computer science, economics, people and management skills.
- •

	Define SEP in an objective way and link to real software development environments.
- •

	Ensure each SEP has its own set of definitions and is linked with other SEP as in traditional engineering.

Further [research work](https://www.sciencedirect.com/topics/engineering/research-work) could also be initiated for building an ontology for the SE principles using an artificial intelligent tool. As well as, investigating the similarities between principles such as ones that are similar but are just named differently. In addition to the principles that are conflicting each other.

Furthermore, an examination of which principles work on which problems and their specific application is required.

[^2]: The aim of an SMS is to specify the research trends for a specific topic and then categorize research with respect to well-defined criteria. In this paper, the SMS process recommended by Kitchenham et al. and García-Holgado are followed, which includes five steps: 1) define the mapping questions related to specific topic, 2) perform a comprehensive search strategy for candidate studies, 3) select studies using inclusion and exclusion criteria, 4) extract the required data, and 5) synthesize the required data. illustrates the [systematic mapping](https://www.sciencedirect.com/topics/computer-science/systematic-mapping) process for this study.

![](https://ars.els-cdn.com/content/image/1-s2.0-S221509862034252X-gr1.jpg)

Download: Download high-res image (460KB)

[^3]: Boehm - seven candidate principles;

[^4]: Jabir and Moore - eight candidate principles;

[^5]: Bourque et al. − 15 candidate principles.

[^6]: Abran and Séguin,, respectively − 34 out of a literature inventory of 308, subsequently reduced to 24 candidate principles through additional criteria.

[^7]: Meridji and Abran - nine candidate principles using the two sets of criteria's in,.