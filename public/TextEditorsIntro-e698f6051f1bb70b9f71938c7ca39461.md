(chap_textEdIntro)=
# Text Editors and Git Overview

Your text editor does not need to replace the command line in order to be helpful in a Git workflow. For most contributors, the best editor setup is one that makes the common tasks easier while still leaving Git itself understandable.

## What editor integration can help with

Modern editors can make Git work more approachable by helping you:

* see which files changed
* inspect diffs without leaving the editor
* stage and unstage changes
* write commit messages
* resolve merge conflicts visually
* jump between code and pull-request-related changes more quickly

These features are especially helpful for beginners because they reduce the amount of context-switching between files, terminal commands, and repository state.

## What editor integration should not replace

Even if you use a GUI or editor integration heavily, it is still valuable to understand a few core Git commands directly:

* `git status`
* `git add`
* `git commit`
* `git fetch`
* `git merge`
* `git push`

Editors are interfaces to Git, not replacements for the underlying model. When something goes wrong, being able to read the repository state from the command line is still one of the most useful skills you can have.

## Features worth looking for

If you are choosing or configuring an editor for Git work, the following features are usually worth prioritizing:

* built-in diff viewing
* visible source control panel
* conflict markers or merge assistance
* integrated terminal
* search across the repository
* extensions for Markdown, notebooks, or language-specific tooling used by the project

## Different contributors need different setups

There is no single best editor for all contributors. A project may have users who prefer:

* a full integrated development environment
* a lightweight code editor
* a terminal-first workflow with only minimal editor integration

The important thing is that the workflow be documented and reproducible enough that other contributors can follow it.

## In this part of the book

The next chapter discusses Visual Studio Code because it is widely used, cross-platform, and has strong built-in Git support. Even if you use a different editor, the broader ideas still apply:

* configure an editor you are comfortable using
* understand how it interacts with Git
* treat editor features as support for a workflow you already understand
