(chap_GitHubHist)=
# History of GitHub

In the [previous chapter](https://pslmodels.github.io/Git-Tutorial/content/background/VCgitHistory.html), we defined and described the three main categories of {term}`version control system`s. We documented the history of {term}`Git` {term}`distributed version control system` (DVCS) and how the current state of Git is really an outgrowth generally of the history of {term}`open source` development and specifically of the development of the open source Linux operating system kernel.

```{admonition} Definition: GitHub
:class: note
{term}`GitHub` or [*GitHub.com*](https://github.com/) is a {term}`cloud` {term}`source code management service` platform designed to enable scalable, efficient, and secure version controlled collaboration by linking {term}`local` {term}`Git` version controlled software development by users. *GitHub*'s main business footprint is hosting a collection of millions of version controlled code repositories. In addition to being a platform for {term}`distributed version control system` (DVCS), *GitHub*'s primary features include code review, project management, {term}`continuous integration` {term}`unit testing`, {term}`GitHub actions`, and associated web page (GitHub pages) and documentation hosting and deployment.
```

As we described in the [last chapter](https://pslmodels.github.io/Git-Tutorial/content/background/VCgitHistory.html) when the development of the {term}`Linux` kernel separated from using the {term}`Bitkeeper` {term}`distributed version control system` (DVCS), Linus Torvalds began work writing his own DVCS software. In the first few years, the Git DVCS software was "self hosting" using a coordinating Linux server. However, it quickly became apparent that a more flexible and scalable central {term}`cloud` service was needed.

The company, GitHub, Inc., was formed in 2007 by Chris Wanstrath, P. J. Hyett, Tom Preston-Werner and Scott Chacon, and the GitHub.com service was rolled out in February 2008 {cite}`GitHubWiki2020`. {numref}`Figure %s <GitHubGrowth>` below shows the growth in GitHub's users and repositories from its inception in 2008 to the most recent [State of the Octoverse](https://octoverse.github.com/) report on the company's progress as well as the Wikipedia entries for "[GitHub](https://en.wikipedia.org/wiki/GitHub)" {cite}`GitHubWiki2020` and "[Timeline of GitHub](https://en.wikipedia.org/wiki/Timeline_of_GitHub)" {cite}`GitHubTimelineWiki2020`. GitHub's users and repositories have grown exponentially since its inception in 2008.

```{figure} ../../_static/lecture_specific/GitHubHistory/GitHubGrowth.png
---
scale: 50%
align: center
name: GitHubGrowth
---
Time series of GitHub growth in users and repositories since 2008. Source: Data come from 2013-2019 [State of the Octoverse](https://octoverse.github.com/) reports as well as Wikipedia articles "GitHub" {cite}`GitHubWiki2020` and "Timeline of GitHub" {cite}`GitHubTimelineWiki2020`.
```

## Acquisition by Microsoft

The vertical line in {numref}`Figure %s <GitHubGrowth>` at June 4, 2018 highlights the data when Microsoft announced its acquisition of GitHub. Some open source users worried that a large for-profit corporation with a long history of antitrust litigation should control the most important platform in open source software development and collaboration. But by 2018, Microsoft had already become one of the heaviest users of GitHub and was maintaining many of the most actively developed repositories on the platform.

In 2014, Steve Ballmer stepped down as CEO of Microsoft and was replaced by Satya Nadella. Nadella quickly began taking Microsoft in a different direction {cite}`MicrosoftOpenWiki2020`. The focus of the expanded beyond the proprietary Windows operating system and into {term}`cloud` services (Azure), embedded, and mobline computing. In an October 2014 media event discussing Microsoft's Azure cloud computing services, Nadella put up a slide that said "Microsoft Loves Linux" and read it to the audience {cite}`McAllister2014`. This statement would have been unthinkable under the previous two Microsoft CEO's, Steve Ballmer and Bill Gates. But from 2014 to its acquisition of GitHub in 2018, Microsoft had shown a strong commitment to the open source community.


## Other GitHub Features

In addition to being a platform for {term}`distributed version control system` (DVCS), GitHub's primary features include code review, project management, {term}`continuous integration` {term}`unit testing`, {term}`GitHub actions`, and associated web page (GitHub pages) and documentation hosting and deployment. In fact, this Jupyter Book employs most of these extra features. GitHub's added features allow it to more easily scale code collaboration and development, both in the open source community and among private enterprise applications.


## Competition

Other {term}`source code management service` platforms exist, but none of them has the size, network, scope, and functionality of GitHub. {term}`Bitbucket` by Atlassian is GitHub's closest competitor and has a slightly different pricing strategy than GitHub. And {term}`GitLab` is also a competitor in this space. But a wide gap separates these other platforms from GitHub.
