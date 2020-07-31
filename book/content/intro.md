(chap_intro)=
# Git and GitHub Tutorial Introduction

This book is published online at [https://pslmodels.github.io/Git-Tutorial/](https://pslmodels.github.io/Git-Tutorial/) using [Jupyter Book](https://jupyterbook.org/intro.html) as its publishing engine. The source code for this book is publicly available in the GitHub repository [https://github.com/PSLmodels/Git-Tutorial](https://github.com/PSLmodels/Git-Tutorial), and users are encouraged to submit pull requests with contributions and corrections. All content is licensed under the [Creative Commons Attribution Non Commercial Share Alike 3.0 license](https://creativecommons.org/licenses/by-nc-sa/3.0/).

This Git and GitHub tutorial grew out of training needs that constantly recurred and overlapped in our collaborative circles. We would need to train any new collaborators on [Policy Simulation Library](https://github.com/PSLmodels) incubated projects on the Git and GitHub workflow we used. Since 2013, the authors have been training students, faculty, policy makers, other researchers to collaborate on research and code using Git and GitHub. Until now, the materials we would use to train our collaborators were pieced together from a number of great sources. This book represents the consolidation of those resources and our experience together in one place.

Two warnings that a seasoned Git and GitHub user should always give a new entrant to this type of version control and code collaboration are the following.
* The learning curve is steep.
* The workflow initially is not intuitive.

These two obstacles seem to work together to make this form of collaboration harder than the sum of their parts initially. However, once you begin collaborating on open source projects or on large-group academic or research projects, you start to see the value of all the different steps, methods, and safeguards invoved with using Git and GitHub. {numref}`Figure %s <GitFlowDiag>` below is a diagram of the main pieces and actions in the primary workflow that we advocate in this book. You will notice that a version of this figure is the main image for the book and is also the `favicon` for the tabs of the web pages of the online book. This figure of a Git and GitHub workflow diagram looks complicated, but these actions will become second nature. And following this workflow will save the collaborators time in the long-run.

```{figure} ../_static/lecture_specific/intro/GitFlowDiag.png
---
scale: 50%
align: center
name: GitFlowDiag
---
Flow diagram of Git and GitHub workflow
```


## Brief definitions

Before we move on with the introduction and the rest of this book, we want to give the reader a quick reference, definition, and comparison of Git and GitHub. We will spend entire chapters on these two topics in {ref}`chap_GitHist` and {ref}`chap_GitHubHist`. But we want to give a brief reference here at the beginning. A full {ref}`chap_glossary` is included in the Appendix of this book.

```{admonition} Definition: Repository
:class: note
A {term}`repository` or "repo" is a directory containing files that are tracked by a version control system. A local repository resides on a local machine. A remote repository resides in the cloud.
```

```{admonition} Definition: Git
:class: note
{term}`Git` is an open source distributed version control software that resides on your local computer and tracks changes and the history of changes to all the files in a directory or {term}`repository`. See the Git website [https://git-scm.com/](https://git-scm.com/) and the [Git Wikipedia entry](https://en.wikipedia.org/wiki/Git) {cite}`GitWiki2020` for more information.
```

```{admonition} Definition: GitHub
:class: note
{term}`GitHub` or GitHub.com is an open source distributed version control software that resides on your local computer and tracks changes and the history of changes to all the files in a directory or {term}`repository`.
```

To be clear at the outset, Git is the version control software that resides on your local computer. It's main functionalities are to track changes in the files in specified directories. But Git also has some functionality to interact with remote repositories. The ineraction between Git and GitHub creates an ideal environment and platform for scaleable collaboration on code among large teams.

## Wide usage
Every year in November, GitHub publishes are report entitled, "The State of the Octoverse", in which they detail the growth and developments in the GitHub community in the most recent year. The most recent [State of the Octoverse](https://github.blog/2019-11-06-the-state-of-the-octoverse-2019/) was published on November 6, 2019 and covered developments from October 1, 2018 to September 30, 2019. Some interesting statistics from that report are the following.

* more than 40 million GitHub user accounts
* more than 100 million code repositories

Alternatives to GitHub include [GitLab](https://about.gitlab.com/), [Bitbucket](https://bitbucket.org/). Other alternatives are documented in [this June 2020 post](https://www.softwaretestinghelp.com/github-alternatives/) by Software Testing Help. But GitHub has the largest user base and largest number of repositories.


## Other great Git and GitHub resources
Prior to writing this book, the authors pieced together training materials from some great resources. We highlight these resources here both to document what many of our ideas are built upon and to recommend resources that should be used concurrently with this book.
* *Pro Git* {cite}`ChaconStraub2020` is the free official textbook of the Git software open source project. You can access this book online at [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2) or you can buy a hard copy from [Amazon.com](https://www.amazon.com/Pro-Git-Scott-Chacon/dp/1484200772?ie=UTF8&camp=1789&creative=9325&creativeASIN=1430218339&linkCode=as2&tag=git-sfconservancy-20). This book focuses on the documentation of the Git software and not as much on its interaction with third party repository hosting services like GitHub. *Pro Git* has translations in 13 languages besides English and has started translations in 16 other languages.
* QuantEcon's "[Git, GitHub, and Version Control](https://julia.quantecon.org/more_julia/version_control.html)" article {cite}`SoodEtAl2020`. This article makes a quick run through Git setup, workflows, and merge conflicts. This article also has some nice exercises to work through at the end.
* Kate Hudson's (the developer, not the actress) "[Flight Rules for Git](https://github.com/k88hudson/git-flight-rules/)" is a how-to guide for actions with Git. Think of this as a Git FAQ. All the links are in the [README.md](https://github.com/k88hudson/git-flight-rules/blob/master/README.md) of this GitHub repository.
* GitHub's [Learning Lab](https://lab.github.com/) site offers tutorials for using Git and GitHub in the form of different learning paths (sequences of tutorials) and individual tutorials.
* [Bitbucket Git tutorials](https://www.atlassian.com/git/tutorials). Bitbucket is the next closest competitor to GitHub, so these tutorials focus on using Git to interact with Bitbucket, which is a little bit different from GitHub. However, the Git tutorials are good.
* Katie Sylor-Miller and Julia Evans [*Oh Shit, Git!*](https://wizardzines.com/zines/oh-shit-git/) is a book in which each chapter is dedicated to key mistakes a Git user will make. This playful e-book costs $10 and can be printed as a PDF. The authors have not used this book, but it looks fantastic. If you prefer or need a cleaner book title, it is also published as [*Dangit, Git!*](https://gumroad.com/l/dangit-git) for the same price.
* Data School's Justin Markham wrote a nice web page entitled, "[Step-by-step guide to contributing on GitHub](https://www.dataschool.io/how-to-contribute-on-github/)" dated June 11, 2020. This is a nice general version of what most contributor guides require. The advantages of this page are that it is highly visual and includes links to other tutorial material.
* The [Git Cheatsheet](https://ndpsoftware.com/git-cheatsheet.html) by NDP Software is an interactive html page that gives the relevant git commands in the five areas of stash, workspace, index, local repository, and upstream repository, as well as how those commands flow into the other areas' commands.
* This [git-pretty flowchart](http://justinhileman.info/article/git-pretty/git-pretty.png) by Justin Hileman is equal parts tongue-and-cheek and realistic heuristic for deciding what to do when you have a particular problem in Git.
* [Git Koans](https://stevelosh.com/blog/2013/04/git-koans/) by Steve Losh, posted April 8, 2013.


## Open source, Policy Simulation Library, research, and collaboration

Finish this preface with a big-picture discussion of where Git and GitHub fit in the broader open source, policy, research, collaboration setting. Discussion of PSLmodels goals, scalable collaboration, precise attribution, open source ethos, heirarchical protection of code, testing, documentation, best practices, harmonization of convention, ease of participation, modularity, crowd sourcing contributions.


## Outline of book and exercises

In the online version of this book, the table of contents can be toggled to be visible or not visible by clicking on the arrow at the upper-left corner of the main text column of each page. The book is divided into six parts, each of which has sub chapters.

Introduction

```{tableofcontents}
```

The contribution of this book to the large body of Git and GitHub references is to bring together in one place the tools and specific instruction for a beginning to move up the Git learning curve as quickly as possible. This is the only resource we know of that combines Git and GitHub functionality and usage with the tools of open source repository management. This is the guide that we wish we had had when we were learning to collaborate with Git and GitHub.

We have also include exercises in some of the chapters. Chapters ? have some of the most important exercises. These are meant to give the user hands on experience with the issues that often come up in collaborating with Git and GitHub.


## About the authors

[**Richard W. Evans**](https://sites.google.com/site/rickecon/) is Advisory Board Visiting Fellow at Rice University's [Baker Institute for Public Policy](https://www.bakerinstitute.org/). He also holds appointments as Director of the [Open Source Economics Laboratory](https://www.oselab.org/), Nonresident Fellow at the [Tax Policy Center](https://www.taxpolicycenter.org/) of the Urban Institute and Brookings Institution, President of [Open Research Group, Inc.](https://www.openrg.com/), and Senior Editor at the [Center for Growth and Opportunity](https://www.thecgo.org/) at Utah State University. Evans specializes in macroeconomics, public economics, and computational economics. Rick was previously Associate Director and Senior Lecturer in the [M.A. Program in Computational Social Science](https://macss.uchicago.edu/) at the University of Chicago from 2016 to 2020 and a Fellow at the [Becker Friedman Institute](https://bfi.uchicago.edu/) at the University of Chicago from 2016 to 2019. He was the Co-Founder and Co-Director of the BYU Macroeconomics and Computational Laboratory at Brigham Young University from 2012 to 2016. He was Assistant Professor in the BYU Economics Department from 2008 to 2016.

After receiving a B.A. in economics from Brigham Young University in 1998, he began his economic career as a Research Economist at Thredgold Economic Associates in Salt Lake City, Utah, providing state and national economic analysis for Zions Bank and their operations in eight western states. Rick later received an M.A. in Public Policy from Brigham Young University in and Ph.D. in Economics from the University of Texas at Austin. He has also spent time as a researcher at the Joint Economic Committee of the U.S. Congress, the Federal Reserve Bank of Dallas, Utah Economic Council, and as an economic consultant. Rick’s current research focuses on building large-scale, open-source, dynamic general equilibrium macroeconomic models of tax policy and providing web applications and training to allow non-experts to use these models for policy analysis. Rick is a core maintainer of the [OG-USA](https://github.com/PSLmodels/OG-USA) open source large-scale overlapping generations macroeconomic model of U.S. fiscal policy, and has provided macroeconomic modeling consulting services to the European Commission, World Bank, and Indian Ministry of Finance.

[**Jason DeBacker**](https://jasondebacker.com/) is Associate Professor in the Department of Economics at the Darla Moore School of Business at the University of South Carolina and Nonresident Fellow at the [Tax Policy Center](https://www.taxpolicycenter.org/) of the Urban Institute and Brookings Institution. His research interests lie in the areas of public finance and macroeconomics. He has published papers on these topics in the *Journal of Financial Economics*, *Journal of
Law and Economics*, the *Journal of Public Economics*, the *Brookings Papers on Economic Activity*, and other outlets. From 2009 to 2012, Jason worked as a financial economist in the Office of Tax Analysis at the U.S. Department of the Treasury. He earned a Ph.D. in economics from the University of Texas at Austin.
