(chap_intro)=
# Git and GitHub Tutorial Introduction

This book is published online at [https://pslmodels.github.io/Git-Tutorial/](https://pslmodels.github.io/Git-Tutorial/) using [Jupyter Book](https://jupyterbook.org/intro.html) as its publishing engine. The source code for this book is publicly available in the GitHub repository [https://github.com/PSLmodels/Git-Tutorial](https://github.com/PSLmodels/Git-Tutorial), and users are encouraged to submit pull requests with contributions and corrections. All content is licensed under the [Creative Commons Attribution Non Commercial Share Alike 3.0 license](https://creativecommons.org/licenses/by-nc-sa/3.0/).

This Git and GitHub tutorial grew out of training needs that constantly recurred and overlapped in our collaborative circles. We repeatedly needed to help new collaborators contribute to [Policy Simulation Library](https://github.com/PSLmodels) repositories using a workflow that was safe, transparent, and scalable. Since 2013, the authors have trained students, faculty, policy makers, and researchers to collaborate on research and code using Git and GitHub. This book collects those lessons in one place.

Two warnings that an experienced Git user should always give a new entrant to version-controlled collaboration are the following.

* The learning curve is steep.
* The workflow initially is not intuitive.

Those obstacles are real, but they are temporary. Once you begin collaborating on open-source projects or on large-group academic and research projects, the purpose of the workflow becomes much clearer. The extra steps create safeguards around shared work: they make changes reviewable, preserve a precise history, and reduce the risk that one person's mistake will disrupt everyone else's work.

{numref}`Figure %s <GitFlowDiag>` below is a diagram of the main pieces and actions in the primary workflow that we advocate in this book. At first glance, it looks busy. That is normal. The main goal of this tutorial is to help the reader connect the commands, the GitHub interface, and the underlying logic of that workflow so that the process becomes manageable and then routine.

```{figure} ../_static/lecture_specific/intro/GitFlowDiag.png
---
scale: 50%
align: center
name: GitFlowDiag
---
Flow diagram of Git and GitHub workflow
```

## Brief definitions

Before we move on, we give a short comparison of Git and GitHub. We spend more time on these topics in {ref}`chap_VCgitHist` and {ref}`chap_GitHubHist`, and a fuller set of definitions appears in the Appendix glossary.

```{admonition} Definition: Repository
:class: note
A {term}`repository` or "repo" is a directory containing files that are tracked by a version control system. A local repository resides on a local machine. A {term}`remote` repository resides in the cloud.
```

```{admonition} Definition: Git
:class: note
{term}`Git` is {term}`open source` version control software that resides on your local computer and tracks changes and the history of changes to all the files in a directory or {term}`repository`. It also provides commands for moving and integrating those changes across related repositories.
```

```{admonition} Definition: GitHub
:class: note
{term}`GitHub` is a {term}`cloud` {term}`source code management service` built around Git repositories. GitHub hosts remote repositories and adds tools for code review, project management, {term}`continuous integration`, pull requests, issue tracking, and documentation hosting.
```

To be clear at the outset, Git is the version control software that lives on your machine, while GitHub is the collaboration platform that helps groups coordinate their Git-based work. The interaction between the two creates a practical environment for large-scale collaboration.

## Wide usage

GitHub has become one of the dominant collaboration platforms for open-source software and many research software projects. That widespread use matters for beginners because it means that the skills learned here transfer to a large number of projects, organizations, and workplaces.

Alternatives to GitHub include [GitLab](https://about.gitlab.com/) and [Bitbucket](https://bitbucket.org/). The details of the interface differ across platforms, but the core Git concepts discussed in this book carry over.

## Other great Git and GitHub resources

Prior to writing this book, the authors pieced together training materials from a number of great resources. We highlight them here both to acknowledge those influences and to recommend companion references.

* *Pro Git* {cite}`ChaconStraub2020` is the free official textbook of the Git software open source project. You can access it online at [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2).
* QuantEcon's "[Git, GitHub, and Version Control](https://julia.quantecon.org/more_julia/version_control.html)" article {cite}`SoodEtAl2020` provides a concise introduction with helpful exercises.
* Kate Hudson's "[Flight Rules for Git](https://github.com/k88hudson/git-flight-rules/)" is an excellent Git troubleshooting reference.
* [Bitbucket Git tutorials](https://www.atlassian.com/git/tutorials) explain many Git concepts clearly, even when their examples use Bitbucket rather than GitHub.
* [Git Koans](https://stevelosh.com/blog/2013/04/git-koans/) by Steve Losh presents Git ideas through short conceptual exercises.

## Open source, Policy Simulation Library, research, and collaboration

This tutorial is shaped by the needs of collaborative open-source research. PSLmodels repositories are not just software products. They are also part of a broader research and policy workflow in which code, documentation, assumptions, and review history all matter.

In that setting, Git and GitHub provide several important benefits.

* They make contributions easier to review before they are accepted.
* They preserve a precise history of who changed what and why.
* They support testing and documentation alongside code.
* They let maintainers protect the main branch while still welcoming outside contributions.
* They lower the cost of onboarding new contributors because the workflow and discussion are visible.

The PSLmodels workflow emphasizes these goals. A contributor is encouraged to work on a branch, open a pull request, discuss the change in public, pass automated checks, and merge only after review. That process may feel slower at first, but it scales much better than informal file sharing or email-based patch exchange.

## Outline of book and exercises

In the online version of this book, the table of contents can be toggled visible or hidden by clicking the arrow at the upper-left corner of the main text column. The book is divided into several parts covering background, hands-on Git and GitHub use, repository management practices, and editor configuration.

```{tableofcontents}
```

The main contribution of this book is to bring together beginner Git usage, GitHub collaboration, and open-source repository management in one place. We especially aim to help the reader make the jump from "I have heard of Git" to "I can contribute safely to a shared repository."

Several chapters include examples and practical exercises. The most important exercises are those that ask the reader to create a branch, make a commit, open a pull request, and resolve a simple conflict, because those tasks mirror the real situations that arise in collaborative work.

## About the authors

[**Richard W. Evans**](https://sites.google.com/site/rickecon/) is Senior Economist at the [Abundance Institute](https://www.abundance.institute/), Director of the [Open Source Economics Laboratory](https://www.oselab.org/), and President of [Open Research Group, Inc.](https://www.openrg.com/). Evans specializes in macroeconomics, public economics, and computational economics. Rick was previously Associate Director and Senior Lecturer in the [M.A. Program in Computational Social Science](https://macss.uchicago.edu/) at the University of Chicago from 2016 to 2020 and a Fellow at the [Becker Friedman Institute](https://bfi.uchicago.edu/) at the University of Chicago from 2016 to 2019. He was the Co-Founder and Co-Director of the BYU Macroeconomics and Computational Laboratory at Brigham Young University from 2012 to 2016. He was Assistant Professor in the BYU Economics Department from 2008 to 2016.

After receiving a B.A. in economics from Brigham Young University in 1998, he began his economic career as a Research Economist at Thredgold Economic Associates in Salt Lake City, Utah, providing state and national economic analysis for Zions Bank and their operations in eight western states. Rick later received an M.A. in Public Policy from Brigham Young University in and Ph.D. in Economics from the University of Texas at Austin. He has also spent time as a researcher at the Joint Economic Committee of the U.S. Congress, the Federal Reserve Bank of Dallas, Utah Economic Council, and as an economic consultant. Rick’s current research focuses on building large-scale, open-source, dynamic general equilibrium macroeconomic models of tax policy and providing web applications and training to allow non-experts to use these models for policy analysis. Rick is a core maintainer of the [OG-USA](https://github.com/PSLmodels/OG-USA) open source large-scale overlapping generations macroeconomic model of U.S. fiscal policy, and has provided macroeconomic modeling consulting services to the European Commission, World Bank, and Indian Ministry of Finance.

[**Jason DeBacker**](https://jasondebacker.com/) is Associate Professor in the Department of Economics at the Darla Moore School of Business at the University of South Carolina and Nonresident Fellow at the [Tax Policy Center](https://www.taxpolicycenter.org/) of the Urban Institute and Brookings Institution. His research interests lie in the areas of public finance and macroeconomics. He has published papers on these topics in the *Journal of Financial Economics*, *Journal of Law and Economics*, the *Journal of Public Economics*, the *Brookings Papers on Economic Activity*, and other outlets. From 2009 to 2012, Jason worked as a financial economist in the Office of Tax Analysis at the U.S. Department of the Treasury. He earned a Ph.D. in economics from the University of Texas at Austin.
