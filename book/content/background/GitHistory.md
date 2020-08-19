(chap_GitHist)=
# History of Git

```{admonition} Definition: Git
:class: note
{term}`Git` is an {term}`open source` {term}`distributed version control system` software that resides on your local computer and tracks changes and the history of changes to all the files in a directory or {term}`repository`. See the Git website [https://git-scm.com/](https://git-scm.com/) and the [Git Wikipedia entry](https://en.wikipedia.org/wiki/Git) {cite}`GitWiki2020` for more information.
```

Git is often confused with the term {term}`GitHub` because the two are used together so often. But Git is simply version control software that resides on a user's {term}`local` machine. The back-end of Git tracks the history of changes (timing and content) to all the files you assign to be tracked using a specific method described below. The set of commands available to users through the Git API ({term}`application programming interface`) is small relative to many other interfaces. But understandinng the usage of those commands is often one of the obstacles to learning Git. We have found that a visual approach to what Git is doing is valuable for gaining the intuition behind the standard workflows and API commands.

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

```{figure} ../../_static/lecture_specific/GitHistory/LVCS.png
---
scale: 50%
align: center
name: LVCS
---
Example directory structure of LVCS
```

An LVCS will build the files in each `version` folder by storing only the changes to each file between contiguous versions. The LVCS approach has the benefit of containing the entire history of changes to a repository on your {term}`local` machine. And because LVCS builds a version of the {term}`repository` by storing only the changes or deltas in the files, the memory footprint of LVCS in minimized. However, LVCS has the disadvantage of not providing any good way of communicating and collaborating on the code being locally version controlled.


### Centralized version control system



### Distributed version control system


## How Git Became This

Describe the Linux development history. Show current number of contributors page. Show how many forks of the Linux kernel exist. This is what you need to scale up collaboration.

List alternative version control software, compare and contrast with Git, give some diagrams of what version control does on the local machine.
