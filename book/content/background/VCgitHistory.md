(chap_VCgitHist)=
# Version Control and Git History

```{admonition} Definition: Git
:class: note
{term}`Git` is an {term}`open source` {term}`distributed version control system` (DVCS) software that resides on your local computer and tracks changes and the history of changes to all the files in a directory or {term}`repository`. See the Git website [https://git-scm.com/](https://git-scm.com/) and the [Git Wikipedia entry](https://en.wikipedia.org/wiki/Git) {cite}`GitWiki2020` for more information.
```

Git is often confused with the term {term}`GitHub` because the two are used together so often. But Git is simply a {term}`version control system` (VCS) software that resides on a user's {term}`local` machine. The back-end of Git tracks the history of changes (timing and content) to all the files you assign to be tracked using a specific method described below. The set of commands available to users through the Git API ({term}`application programming interface`) is small relative to many other interfaces. But understandinng the usage of those commands is often one of the obstacles to learning Git. We have found that a visual approach to what Git is doing is valuable for gaining the intuition behind the standard workflows and API commands.

In the rest of this chapter, we will describe the three main types of {term}`version control system`s and compare and contrast Git's approach to the other two approaches. We will then provide a short summary of how Git evolved over its history into the form it currently takes. Some other good references for what Git is and its history are *Pro Git* {cite}`ChaconStraub2020`, sections [1.1](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control), [1.2](https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git), and [1.3](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).


## Version Control

```{admonition} Definition: Version control system
:class: note
A *version control system* or version control software or VCS is software that records changes to a set of files, including the order in which the changes were made and the content of those changes, in such a way that previous versions can be recalled or restored.
```

Version control systems take three main forms: (i) local version control systems (LCVS), (ii) centralized version control systems (CVCS), and (iii) distributed version control systems. {cite}`WikiVCSlist2020` maintains an updated page, "[List of version-control software](https://en.wikipedia.org/wiki/List_of_version-control_software)," that provides an exhaustive list of {term}`open source` and proprietary version-control software packages categorized in each of these three types of approaches.


### Local version control system
```{admonition} Definition: Local version control system (LVCS)
:class: note
A {term}`local version control system` or LVCS is the simplest and most common approach to VCS. LVCS stores all the changes to the files in a {term}`repository` locally on the user's machine as a series of changes or deltas in the files. This is the approach taken by Apple's Time Machine backup software as most software that includes an "undo" function.
```
LVCS is one step more sophisticated than do-it-yourself approach. Conceptually, LVCS is saving the set of changes to the appropriate files in separate directories of the local machine. Using these changes or deltas, LVCS can recreate the state of the repository at the point of a given snapshot by sequentially executing those deltas to the initial state of the repository or undoing those deltas from the current state of the repository.

{numref}`Figure %s <LVCS>` below shows an example of what an LVCS directory structure might look like. The {term}`repository` being tracked is named "directory". The figure shows five versions of the repository as files in five corresponding version folders. The files in the `version1` folder represent the original or inital state of the repository. In the `version2` folder, you can see that both `file_A` has changed to `file_A1` and `file_C` has changed to `file_C1`. In folders `version3`, `version4`, and `version5`, more changes to the files are recorded.

```{figure} ../../_static/lecture_specific/VCgitHistory/LVCS.png
---
scale: 50%
align: center
name: LVCS
---
Example directory structure of local version control system (LVCS)
```

An LVCS will build the files in each `version` folder by storing only the changes to each file between contiguous versions. The LVCS approach has the benefit of containing the entire history of changes to a repository on your {term}`local` machine. And because LVCS builds a version of the {term}`repository` by storing only the changes or deltas in the files, the memory footprint of LVCS in minimized. However, LVCS has the disadvantage of not providing any good way of communicating and collaborating on the code being locally version controlled.


### Centralized version control system
```{admonition} Definition: Centralized version control system (CVCS)
:class: note
A *centralized version control system* or CVCS is an approach to version control in which all the files in a {term}`repository` as well as the change history (content and timing) are located on a central {term}`remote` server. User's check out versions of files from the repository and check them back in, creating new change history on the central server.
```

{numref}`Figure %s <CVCS>` below shows the workflow of a centralized version control system (CVCS). Developers A and B check files out from the remote centralized server onto their respective local machines and make changes on their local machines. The central server version updates when changes from remote users are checked back in.

```{figure} ../../_static/lecture_specific/VCgitHistory/CVCS.png
---
scale: 50%
align: center
name: CVCS
---
Example structure of centralized version control system (CVCS) workflow
```

The centralized version control system (CVCS) approach to version control allows for collaboration among a large number of developers and does not require a large memory footprint on each developer's {term}`local` machine. However, remote checking out and checking in is more time consuming, and the entire history of the repository is not on each developer's local machine.

Chacon and Straub (2020, Section 1.1){cite}`ChaconStraub2020` highlights a potential drawback with CVCS that the central server exposes only one point of failure. However, with current standards for {term}`cloud` services backup and security, this potential weakness is largely mitigated in most cases.

### Distributed version control system

{term}`Git` software is an {term}`open source` {term}`version control system` software with capability designed to also operate as {term}`distributed version control system` (DVCS) software.

```{admonition} Definition: Distributed version control system (DVCS)
:class: note
A *distributed version control system* or DVCS is {term}`version control system` software on any computer, {term}`local` or {term}`remote`, that tracks the entire history of changes to a {term}`repository` and coordinates and organizes collaboration among multiple users through a {term}`source code management service`. It is distributed in the sense that multiple {term}`clone`s of a single {term}`remote` repository have the same full history of that repository.
```

A distributed version control system (DVCS) puts the entire history on each user's {term}`local` machine upon some form of check out. The DVCS requires two components. The first component is software on all collaborating machines that tracks changes and communicates between the users' machines. The second component is a {term}`cloud` {term}`source code management service` platform that coordinates collaboration among the participating users. In the case of this tutorial, the software is {term}`Git` and the coordinating cloud platform is {term}`GitHub`.

{numref}`Figure %s <DVCS>` below shows how each of three collaborating entities in the DVCS collaboration has the full set of files and the full Git history residing on their local machine. Much of the difficulty in learning {term}`Git` comes from the commands that allow these three (or many more) independent entities to effectively transfer, track, and communicate changes among each other. A definite downside to using a DVCS like Git is the complexity involved with updating, submitting changes, merging differences, and hierarchical permissions.

```{figure} ../../_static/lecture_specific/VCgitHistory/DVCS.png
---
scale: 50%
align: center
name: DVCS
---
Example structure of distributed version control system (DVCS) workflow
```

On the positive side, the DVCS configuration is the most flexible and allows for many different workflows. It allows for a workflow that looks and behaves similarly to the CVCS workflow shown in {numref}`Figure %s <CVCS>`. But it also allows for collaborative workflows directly between users that is facilitated by the central server run by the {term}`source code management service` platform.

Because the entire Git history and file structure resides on each user's {term}`local` drive independently, the project's files naturally have many backups. And a user can work with the project files without being connected to the internet and at the speeds of their local machine. A related drawback to DVCS systems is that the memory footprint of the project is large.

Because the DVCS approach to version control is the most flexible and allows the most autonomy, it has become the most common version control method for {term}`open source` projects, with {term}`Git` version control software as the most widely used implementation.

```{admonition} Note: Open source irony of Git source code
:class: warning
{term}`Git`'s source code was once on a {term}`GitHub` repository that was actively developed by many outside users posting issues, asking questions, and submitting code software patches through {term}`pull request`s. However, if you go to the current GitHub repository for Git's source code ([https://github.com/git/git](https://github.com/git/git)), you will find in the description of the repository that the GitHub repository is a read-only mirror of the:
> Git Source Code Mirror - This is a publish-only repository and all pull requests are ignored. Please follow Documentation/SubmittingPatches procedure for any of your improvements.

So the Git source code is openly published, but the method of outside collaboration is limited. If you read the documentation for [submitting patches to Git](https://github.com/git/git/blob/master/Documentation/SubmittingPatches), you find that all changes by outside users are sent to the Git maintainers through the listserve. This makes the Git development DVCS workflow necessarily less distributed.
```


## History of Git: Why Git Became This

The standard *Pro Git* book {cite}`ChaconStraub2020` has a chapter entitled, "[A Short History of Git](https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git)". But a more recent article by Favell (2020) {cite}`Favell2020` entitled, "[The History of Git: The Road to Domination in Software Version Control](https://www.welcometothejungle.com/en/articles/btc-history-git)," goes into more detail about Git's rise from the early 2000's to the present. But one also needs to know a little bit about the [history of the Linux](https://en.wikipedia.org/wiki/History_of_Linux) {term}`open source` operating system {cite}`LinuxWiki2020` to appreciate its important role in the history of Git. The short history we present here is a synopsis that highlights why Git has the features and following that it does. We are tryin to give you evidence that you should make the investment to become a Git master.

Early in the Favell (2020) article {cite}`Favell2020`, he gives the following strong evidence of Git's current dominance in the VCS ({term}`version control system`) field.

> The best indication of Git’s market dominance is a survey of developers by Stack Overflow. This found that 88.4% of 74,298 respondents in 2018 used Git (up from 69.3% in 2015). The nearest competitors were Subversion, with 16.6% penetration (down from 36.9%); Team Foundation Version Control, with 11.3% (down from 12.2%); and Mercurial, with 3.7% (down from 7.9%). In fact, so dominant has Git become that the data scientists at Stack Overflow didn’t bother to ask the question in their 2019 survey. {cite}`Favell2020`

### Early Linux development: 1991 to 2002

In 1991, Linus Torvalds posted an initial version of a free operating system on an internet message board used by developers. The developer community began to take interest in this operating system, and submitted patches and changes to the source code via internet until 2002. During this time period, the version control approach of the Linux kernel could be best described as a network of {term}`local version control system`s (LVCS) early on, then transitioning to a {term}`centralized version control system` (CVCS).

By the late 1990s, development of the Linux kernel as a viable operating system for broad use had greatly matured, and the number of developers and contributors had multiplied. The community of Linux developers were committed to keeping the kernel's source code {term}`open source`, but the scaling of the number of collaborators was being limited by the {term}`version control system`s being used at the time, such as CVS and Subversion.

By 2000, some of the Linux developers were using a new {term}`source code management service` and accompanying version constrol system, BitKeeper {cite}`BitKeeperWiki2020`, because they offered free code hosting. But the software for the BitKeeper VCS tools was proprietary, which made some of the core Linux developers uncomfortable given the Linux open source license and ethic. But in 2020, Torvalds prevailed on much of the community to host the main {term}`repository` of the Linux source code with BitKeeper, which was a DVCS. The rationale was that the efficiencies from a mature DVCS platform would outweigh any conflict with proprietary versus open source licenses.


### Linux development with BitKeeper: 2002 to 2005

Between 2002 and 2005 the main repository of the Linux kernel and many of its core developers were enjoying free hosting of DVCS ({term}`distributed version control system`) collaboration and development through BitKeeper's services. However, in 2005, a dispute between one of Linux's developers and the CEO of BitKeeper's parent company (who was also a Linux developer) resulted in BitKeeper revoking the Linux repository's free status. Torvalds was torn between lack of alternative quality DVCS {term}`source code management service`s and the importance of not paying for the DVCS service and having the licenses associated with those services be consistent with and not restrictive of the Linux open source license.

It is worth noting the BitKeeper pioneered the {term}`distributed version control system` approach. And it was not clear that any suitable alternatives could be found. A new DVCS system for Linux development had to be found. The *Pro Git* book cites five properties and a DVCS system had to have to satisfy the needs of the large and growing Linux development community.{cite}`ChaconStraub2020`{cite}`GitWiki2020`

* Speed
* Simple design
* Strong support for non-linear development (thousands of parallel {term}`branch`es)
* Fully distributed
* Able to handle large projects like the Linux kernel efficiently (spped and data size)
* Include very strong safeguards against corruption, either accidental or malicious


### Birth and progress of Git: 2005 to present

It became clear that no suitable alternative to BitKeeper existed, so Torvalds began development of his own DVCS called "Git" on April 3, 2005.
> The development of {term}`Git` began on 3 April 2005. Torvalds announced the project on 6 April and became self-hosting the next day. The first merge of multiple branches took place on 18 April. Torvalds achieved his performance goals; on 29 April, the nascent Git was benchmarked recording patches to the Linux kernel tree at the rate of 6.7 patches per second. On 16 June, Git managed the kernel 2.6.12 release.{cite}`GitWiki2020`

We could not find any definitive source of an instance in which Torvalds explicitly states where the name "Git" came from and what it means. But most sources point to the Git wiki FAQ thread, "[Why the 'Git' name](https://git.wiki.kernel.org/index.php/GitFaq#Why_the_.27Git.27_name.3F)?"{cite}`GitFAQwiki2020` The most plausible origin of the name comes from a sarcastic quip by Torvalds that "Git" was named after the British slang for "pig headed or argumentative". Torvalds is quoted as saying:
> I'm an egotistical bastard, and I name all my projects after myself. First "Linux", now "Git". --Linus Torvalds {cite}`GitFAQwiki2020`

{numref}`Figure %s <GitContributors>` and {numref}`Figure %s <LinuxContributors>` below show the list of contributors, what they contributed, and when they contributed on the {term}`GitHub` {term}`source code management service`. Note that the Git source code has had 1,388 contributors over its history, and the Linux kernel has had 10,933 contributors--all using Git and GitHub to collaboratively create and improve their respective source codes. No other software and platform allow code collaboration to scale as effectively and efficiently.

```{figure} ../../_static/lecture_specific/VCgitHistory/GitContributors.png
---
scale: 100%
align: center
name: GitContributors
---
Screenshot of GitHub Git source code mirror contributors ([https://github.com/git/git/graphs/contributors](https://github.com/git/git/graphs/contributors)) as of August 20, 2020
```

```{figure} ../../_static/lecture_specific/VCgitHistory/LinuxContributors.png
---
scale: 100%
align: center
name: LinuxContributors
---
Screenshot of main Linux kernel contributors ([https://github.com/torvalds/linux/graphs/contributors](https://github.com/torvalds/linux/graphs/contributors)) as of August 20, 2020
```

### Git: Open to copy, selective to receive

We highlight two final characteristics of the Git {term}`version control system` that are fundamental to its underlying philosophy and ethos--(i) ownership of code is completely decentralized and (ii) ownership of {term}`repository`. First, Git is explicitly decentralized. We will define a {term}`fork` more carefully in the chapter {ref}`chap_basics` and in the {ref}`chap_glossary`, but for now it is sufficient to say that a fork is a {term}`remote` copy of a {term}`remote` code {term}`repository` (both of which reside in the {term}`cloud`). Because Git is a {term}`distributed version control system` (DVCS) each fork is a complete copy of the code repository along with its {term}`commit` (or change) history. Anyone can fork a public repository and change the code however they like. {numref}`Figure %s <GitForks>` below shows that the Git source code repository mirror on GitHub has more than 19,700 forks. This means that 19,700 GitHub account users have made a complete fully functional copy of the Git source code and can make any changes they like to their personal forks.

```{figure} ../../_static/lecture_specific/VCgitHistory/GitForks.png
---
scale: 100%
align: center
name: GitForks
---
Screenshot of GitHub Git source code mirror main page ([https://github.com/git/git](https://github.com/git/git)) as of August 20, 2020 highlighting the number of {term}`fork`s
```

The second characteristic seems to go in the opposite direction of the first point in that every code {term}`repository` has a rigid hierarchical structure of who has permission to accept changes to the code to provide maximum code security and order while allowing the potential of contributions from anyone. In the {term}`open source` community, the term {term}`benevolent dictator`(s) is often attached to the individuals who have {term}`merge` permission for a code repository or permission to accept changes into that repository. With the Git DVCS, anyone can make and take a copy of the public repository code and they can submit changes to anyone else's repository. But only the individuals with merge permission for a given repository can accept and incorporate changes into the repository. We will discuss this more in Chapters {ref}`chap_basics` and {ref}`chap_workflow`.

These two characteristics together--open access to copy code repositories but restricted access to submit changes--has found the sweet spot for DVCS collaboration. This is why Git has gained such a large share of the {term}`version control system` and {term}`source code management service` market. Git, in combination with the GitHub source code management service platform, has proven to be the best way to efficiently scale collaboration on code development.
