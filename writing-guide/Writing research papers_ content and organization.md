---
title: "Writing research papers: content and organization"
source: "https://homepages.inf.ed.ac.uk/sgwater/writing/content.html?utm_source=chatgpt.com"
author:
published:
created: 2026-11-24
description:
tags:
  - "clippings"
---
## Goals of this page

This page is a constant work in progress containing advice that I find myself giving repeatedly to students. I intend to add to it as I find more examples of common mistakes, but it isn't currently organized in any particular way, or complete. The advice is mainly oriented towards conference/journal papers, but where noted some of it relates to longer documents (e.g., theses).

For more complete advice on **research papers** you may wish to look at [Simon Peyton Jones' excellent slides](https://www.microsoft.com/en-us/research/academic-program/write-great-research-paper/). I agree with almost everything he says; a few exceptions are noted below.

If you are actually looking for advice on writing a **PhD thesis**, please see [Stefan Rueger's guide](http://people.kmi.open.ac.uk/stefan/thesis-writing.pdf). I haven't read the whole thing carefully, but the parts I have read are very sensible.

Parts of this page also draw on material from [*The Craft of Research*](http://www.amazon.co.uk/Research-Chicago-Writing-Editing-Publishing/dp/0226065669/ref=sr_1_1?s=books&ie=UTF8&qid=1400685408&sr=1-1&keywords=craft+of+research) by Wayne C. Booth, Gregory G. Colomb, and Joseph M. Williams, which is a comprehensive guide to research writing, from formulating a question to writing up your results.

## The abstract

I find [Philip Koopman's advice](http://www.ece.cmu.edu/~koopman/essays/abstract.html) to be very good. The abstract is one area where I think the Peyton Jones slides (above) are not great; his description of what goes in the abstract is both too rigid and too vague; Koopman's advice seems much more helpful.

## The introduction

Very informally, your introduction should answer the reader's questions

*What did you do and why should I care?*

More formally, you should answer the following two questions in this order:

1. What is the problem?
2. What are your contributions?

Point 1 could be addressed by identifying a scientific question and why it is interesting, or an engineering problem and why solving it would be important. In both cases you should also say at least something about why previous approaches (if any) have not solved the problem satisfactorily.

For point 2, you will likely have some high-level contributions (e.g. the approach you are taking) as well as lower-level contributions (e.g. the results you achieve). Be specific and explicit about your contributions; "our main contributions are" is not a phrase to shy away from! Also note that contributions are normally *claims* that will be supported by *evidence* in the remainder of the document, not simply *descriptions* of what you have done (although you can include some description to make clearer what the claims are). For example "our method improves upon Y (because Z)" is a claim; "we implement X using Y" is a description.

## Using examples

Examples often can be worth 1000 words. They are especially useful in introductions to make your problem or approach concrete. You can always come back later to fill in details that the example skims over. But really, any time you introduce some abstract material (definition, algorithm, formula, etc.), you should ask yourself: would this be easier to understand if I added an example? Also watch out for sentences like "in some cases X could happen": can you give an example of *when* it would happen? Ideally you should try to come up with one or two running examples that can illustrate many of the different ideas you are talking about.

## The "related work" section

Like all other sections of the paper, every background/literature review section must have a *main point* (or a couple of closely related points) and everything you say in it should support that point. "Describing work in related areas" is not a main point. Main points of background sections could include

a) convincing the reader that your approach is novel (by, e.g., pointing out how it differs from previous approaches).

b) convincing the reader that your approach is sensible (by, e.g., giving examples of successful previous work taking a similar approach; or previous results that suggest the current approach).

c) describing a previous approach that your work builds off of.

d) convincing the reader that you are sufficiently familiar with the problems and approaches in the area to write a paper.

Other than case (c) where you need to describe something in detail because your work is directly based on it, all of these points are about convincing, not describing. Also, case (d) is almost always satisfied by addressing (a) and/or (b). So if you have written anything that is merely a description, either get rid of it or change it so that it addresses one or both of these points (possibly in a supporting fashion: you may need to briefly describe an approach to show how it inspires yours or is different from yours, but the point should be the inspiration/difference, not the description.) When discussing others' work, do not simply say it is "similar" or "different" to yours; be explicit about what the similarities and differences are. And, make sure the reader will understand why these similiarites/differences are important.

For an example Related Work section that follows these principles, see Sec. 2 of [this paper](http://homepages.inf.ed.ac.uk/sgwater/papers/acl12-bootstrapping.pdf).

However, before even writing your related work section, consider: do you need a separate section for this material? In many cases it is possible to provide sufficient evidence for points (a) and (b) in the introduction itself that you do not need a further "related work" section. Where possible, this organization is often desirable, since it will force you to be brief and pointed in your references to previous work, without unnecessary description.

For examples of this type of introduction, see [this paper](http://homepages.inf.ed.ac.uk/sgwater/papers/cogsci11_predictability.pdf) or [this paper](http://homepages.inf.ed.ac.uk/sgwater/papers/emnlp11-bmmm.pdf).

## Sectioning, transitions, and main points

\[These notes are especially applicable to longer documents, e.g., journal articles and theses, which less experienced writers may have more trouble organizing than short papers, but they are potentially useful for documents of any length.\]

Be wary of using very large numbers of very short sections, and/or using section headings as a crutch to indicate the structure of the document. The section headings may make sense to you, but by themselves they are often insufficient to make the document structure clear to the reader; instead you should make sure the text itself includes transitions, introductions, and/or conclusions that clarify its structure, giving the reader a sense of direction. Consider what would happen if you removed the section headings. Would the document make any sense? A clearly structured document ought to. Crucially, you need to make sure that the *main point* of each section is clearly stated (i.e., why have you included that section in the document? What is it supposed to tell us?), and that this point is *clearly related* to what came before (and often, what will follow).

Normally, the main point of each section and the transitioning/context information should come as an introduction to the section, which could be just a sentence or two for short (sub)sections or could be much longer. Introductions may or may not have explicit section headings--usually you would only put a section/chapter heading on an introduction at the beginning of a full paper, or (for a multi-chapter document) at the beginning of the whole document and each chapter. Otherwise it should be:

```
\section{A}
text introducing main point and how the subsections relate to this point
\subsection{B}
stuff 1
\subsection{C}
(relationship of C to B and/or to the main point of A)
stuff 2
...
```

In addition, for any medium or large section of a long document (including sections shorter than a full chapter), consider: would it help the reader to include a conclusion that reminds them what the main point of the section was and again fits things into the context of the larger chapter/document (often including what are the missing pieces that the following sections will fill in?). The conclusion doesn't have to be a separate section, it could just be a couple of sentences at the end.

## Coherence and cohesion

Getting sections and transitions right at the highest level isn't enough if your individual paragraphs don't hang together and follow a natural flow. Two places to look for help with this are:
- UNC Chapel Hill's [handout on Paragraph Development](http://writingcenter.unc.edu/handouts/paragraphs/)
- Stephan Flores' [brief style advice](http://www.webpages.uidaho.edu/~sflores/styleadvice.pdf). It is actually a very short summary based on [*Style: Toward clarity and grace*](http://www.amazon.co.uk/Style-Clarity-Chicago-Writing-Publishing/dp/0226899152/ref=sr_1_2?ie=UTF8&qid=1313569326&sr=8-2) by Joseph M. Williams, which I highly recommend for more detailed information.
	---

	Last modified: Wed, May 21, 2014 3:53:24 PM