(chap_docum)=
# Documentation

Good documentation lowers the cost of using, reviewing, and contributing to a repository. In many projects, documentation quality is one of the main factors that determines whether a newcomer becomes a contributor or gives up early.

## Why documentation matters

Documentation helps different audiences answer different questions.

* Users want to know what the project does and how to run it.
* Contributors want to know how to set up the environment, run tests, and submit changes.
* Maintainers want project knowledge to live in the repository rather than only in their heads.

Documentation is part of the product, not an afterthought.

## The role of the README

For many repositories, `README.md` is the first page a newcomer sees. A good README usually includes:

* what the repository is for
* how to install or set it up
* how to run the project
* how to contribute
* where to find more detailed documentation

If the README grows too large, that is often a sign the project is ready for fuller documentation rather than a sign the README should be abandoned.

## Layered documentation

Healthy projects often use several layers of documentation.

* README for quick orientation
* contributor guide for workflow and setup
* API or developer docs for code-level detail
* tutorials or examples for common tasks
* changelog or release notes for project history

Each layer serves a different purpose.

## Documentation for code and research repositories

In research-oriented open-source work, documentation may need to cover more than software usage. It may also need to explain:

* modeling assumptions
* data inputs
* expected outputs
* limitations and known caveats
* how results should be interpreted

This kind of context is often essential for reproducibility.

## Documentation tooling

Projects use many different documentation tools. Common options include:

* plain Markdown in the repository
* Jupyter Book
* Sphinx
* notebooks and example galleries

The best tool is often the one the team will maintain consistently.

This repository uses Jupyter Book and MyST Markdown. If you are editing MyST files in VS Code, the [MyST extension](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) can make the authoring experience smoother.

## What good contributor documentation should cover

A newcomer should not need tribal knowledge to contribute. At minimum, contributor documentation should explain:

* how to create the project environment
* how to run tests
* how to build docs, if applicable
* how to format or lint code
* the expected pull request workflow

## Treat documentation as part of review

One good maintainer habit is to ask during review: does this change require documentation updates?

Examples include:

* a new feature
* a changed command-line interface
* a new dependency
* a workflow change
* a changed result or interpretation in a research project

If the answer is yes, the docs should usually change in the same pull request.

## Good habits

* Keep examples current.
* Prefer concrete commands over vague prose.
* Write for a reader who does not already know the project.
* Document the supported setup path explicitly.
* Fix stale docs quickly once discovered.

Documentation quality compounds over time. A small improvement today often saves many future contributors from the same confusion.
