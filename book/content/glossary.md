(chap_glossary)=
# Glossary

```{glossary}
application programming interface
  An application programming interface or API is the medium, method, and rules through which a user interacts with software. The API includes a medium which can be a {term}`command line interface` on a specific {term}`local` terminal or a {term}`graphical user interface`. The API also defines the commands through which a user interacts with the software.

benevolent dictator
  In open-source software, a benevolent dictator is an informal term for a person who has broad authority over the direction of a project and final say over which changes are accepted. In many modern projects, decision-making is shared across several maintainers rather than centered on one individual.

Bitbucket
  *Bitbucket* or [*Bitbucket.org*](https://bitbucket.org/) is a {term}`cloud` {term}`source code management service` platform designed to enable scalable, efficient, and secure version controlled collaboration by linking {term}`local` {term}`Git` version controlled software development by developers.

Bitkeeper
  BitKeeper was a proprietary version control system that played an important role in the history of Linux kernel development and influenced the design of {term}`Git`.

Box, Inc.
  Box, Inc. is a cloud file storage and file sharing service used by many universities and businesses. It supports file synchronization and sharing, but it is not a full version control platform like GitHub.

branch
  A branch is a named line of development in a Git repository. Branches allow a user to work on one set of changes independently from another set of changes.

centralized version control system
  A centralized version control system or CVCS is an approach to version control in which all the files in a {term}`repository` as well as the change history (content and timing) are located on a central {term}`remote` server. User's check out versions of files from the repository and check them back in, creating new change history on the central server.

clone
  Clone can be a verb or a noun in the context of {term}`Git` software. A clone is a {term}`local` copy of a {term}`remote` {term}`repository` with its entire Git {term}`distributed version control system` history. To *clone* a repository is to use the `git clone [repo path]` command to copy a remote repository to your local machine with the accompanying Git version control history.

cloud
  Cloud can be a descriptor or a noun. As a descriptor, cloud refers to computational resources, such as servers, that are accessed remotely via the internet. As a noun, remote computational resources and storage can be referred to generically as "the cloud".

command line interface
  A command line interface or CLI is a text-based way of interacting with software by typing commands into a terminal.

commit
  Commit can be a verb or a noun in Git. As a verb, to commit means to record a set of staged changes in the repository history. As a noun, a commit is that recorded snapshot together with its author, timestamp, and message.

continuous integration
  Continuous integration or CI is the practice of automatically running checks, such as tests, builds, or style validation, whenever changes are proposed or merged.

distributed version control system
  A *distributed version control system* or DVCS is {term}`version control system` software on any computer, {term}`local` or {term}`remote`, that tracks the entire history of changes to a {term}`repository` and coordinates and organizes collaboration among multiple users. It is distributed in the sense that multiple {term}`clone`s of a single {term}`remote` repository have the same full history of that repository.

Dropbox
  Dropbox is a cloud file storage and synchronization service. It is useful for sharing files, but it does not provide the same history, branching, and code review features as Git and GitHub.

fork
  A fork is a copy of a remote repository created under a different GitHub account or organization. Forks are central to many open-source workflows because they let contributors propose changes without direct write access to the upstream repository.

Git
  *Git* is {term}`open source` {term}`version control system` software with capability designed to also operate as {term}`distributed version control system` (DVCS) software that resides on your local computer and tracks changes and the history of changes to all the files in a directory or {term}`repository`. See the Git website [https://git-scm.com/](https://git-scm.com/) and the [Git Wikipedia entry](https://en.wikipedia.org/wiki/Git) {cite}`GitWiki2020` for more information.

GitHub
  *GitHub* or [*GitHub.com*](https://github.com/) is a {term}`cloud` {term}`source code management service` platform designed to enable scalable, efficient, and secure version controlled collaboration by linking {term}`local` {term}`Git` version controlled software development by users. *GitHub*'s main business footprint is hosting a collection of millions of version controlled code repositories. In addition to being a platform for {term}`distributed version control system` (DVCS), *GitHub*'s primary features include code review, project management, {term}`continuous integration` {term}`unit testing`, {term}`GitHub actions`, and associated web page (GitHub pages) and documentation hosting and deployment.

GitHub actions
  GitHub Actions is GitHub's automation system for running workflows such as tests, builds, deployments, and repository maintenance tasks.

GitLab
  GitLab is a source code hosting and collaboration platform similar to GitHub. It supports Git repositories, issue tracking, merge requests, CI, and other project management features.

Google Docs
  Google Docs is a cloud-based collaborative word-processing application. It is useful for shared writing, but it is not a substitute for Git-based version control of code repositories.

Google Drive
  Google Drive is a cloud storage and file synchronization platform from Google. It can store and share project files, but it does not provide Git-style branching, merging, and commit history.

graphical user interface
  A graphical user interface or GUI is a visual way of interacting with software through windows, buttons, menus, icons, and other on-screen elements.

integrated development environment
  Integrated development environment or IDE is a software application that consolidates many of the functions of software development under one program. IDEs often include a code editor, object memory and identification, debugger, and build automation tools. (See [IDE Wikipedia entry](https://en.wikipedia.org/wiki/Integrated_development_environment) {cite}`GitIDE2020`.)

Linux
  Linux is a family of open-source operating systems whose development history is closely tied to the history of Git.

local
  *Local* is a descriptor that refers to files that reside or operations that are performed on a user's machine to which he or she has direct access without using the internet.

local version control system
  A *local version control system* or LVCS is the simplest and most common approach to VCS. LVCS stores all the changes to the files in a {term}`repository` locally on the user's machine as a series of changes or deltas in the files. This is the approach taken by Apple's Time Machine backup software as most software that includes an "undo" function.

merge
  Merge can be a verb or a noun. To merge is to combine changes from one branch into another branch. A merge may happen automatically or may require human conflict resolution.

open source
  *Open source* is a descriptor that is usually applied to software or computer code projects, but can also be applied to any project based upon or represented by digital files. An open source project is one in which the source code is freely available to be downloaded and used and in which collaboration, improvements, and changes to the code are encouraged. The free download and use (outward direction) aspect of *open source* is often emphasized. But the collaboration and improvement contribution (inward direction) aspect is at least as important. {term}`Git` and {term}`GitHub` have enabled efficient and scalable collaboration to a degree not seen in other collaborative workflows.

pull request
  A pull request or PR is a GitHub request asking maintainers to review and merge a proposed set of changes from one branch into another branch.

remote
  *Remote* is a descriptor that refers to files that reside or operations that are carried out on a server to which a user has access using the internet.

repository
  A *repository* or "repo" is a directory containing files that are tracked by a version control system. A local repository resides on a local machine. A remote repository resides in the cloud.

source code management service
  A *source code management service* is a {term}`cloud` platform that hosts computer code files and provides either {term}`centralized version control system` (CVCS) or {term}`distributed version control system`. As the central hub of either CVCS or DVCS, the source code management service provides the platform and rules for distributed code collaboration. Leading examples are {term}`GitHub` and {term}`Bitbucket`.

unit testing
  Unit testing is the practice of writing and running tests for small, individual parts of a code base to confirm that each part behaves as expected.

version control system
  *Version control system* or version control software or VCS is software that records changes to a set of files, including the order in which the changes were made and the content of those changes, in such a way that previous versions can be recalled or restored.
```
