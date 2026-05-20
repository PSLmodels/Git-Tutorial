(chap_license)=
# Open Source License Options

Choosing a license is one of the most important early decisions for an open-source repository. A license tells other people what they are allowed to do with the code and what obligations come with that use.

## License used by this project

The Git Tutorial project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (CC BY-NC-SA 4.0).

The copyright notice for the project should read:

`Copyright (c) 2026, PSLmodels/Git-Tutorial contributors`

This is a more restrictive license than permissive software licenses such as BSD or MIT because it requires attribution, limits use to non-commercial purposes, and requires adapted versions to be shared under the same license terms.

## Why a license matters

Without a license, a public GitHub repository may be visible, but others usually do not have clear legal permission to reuse, modify, or redistribute the code.

A clear license:

* makes reuse expectations explicit
* reduces uncertainty for contributors and users
* helps organizations decide whether they can adopt the project
* clarifies how improvements can flow back into the community

## Common open-source license families

Open-source licenses often fall into two broad categories.

### Permissive licenses

Permissive licenses such as MIT, BSD, and Apache 2.0 usually allow broad reuse with relatively few obligations beyond preserving notices and, in some cases, including the license text.

These licenses are often chosen when the project wants to maximize downstream adoption.

### Copyleft licenses

Copyleft licenses such as GPL require derivative works to remain under compatible open-source terms when distributed. These licenses are often chosen when maintainers want changes to remain open in downstream redistributions.

### Creative Commons licenses

Creative Commons licenses are more commonly used for documentation, books, and other written or creative works than for software source code. A license such as CC BY-NC-SA 4.0 allows sharing and adaptation with attribution, restricts commercial use, and requires derivatives to use the same license.

## Questions maintainers should ask

Before choosing a license, it helps to ask:

* Do we want the broadest possible reuse?
* Do we want derivative works to remain open?
* Are there funder, employer, or institutional requirements?
* Are we combining code with dependencies that have license compatibility constraints?

## A practical beginner rule

If you are contributing to an existing repository, do not choose a new license on your own. Follow the license already used by the project and ask maintainers before making changes to licensing files.

If you are starting a new repository, choose a standard well-known license rather than inventing custom terms.

## Private repositories

Not every repository is open source. Some projects are private because they contain sensitive data, internal tools, unpublished research, or code that an organization is not ready to release.

A private repository can still benefit from all the workflow practices described in this book:

* branches
* pull requests
* code review
* CI
* issue tracking

The difference is access control, not the basic collaboration model.

## Documentation matters too

Once a project chooses a license, that decision should be easy to find.

Good practice includes:

* a top-level `LICENSE` file
* a short note in the `README.md`
* consistent statements in package metadata when relevant

## The social side of licensing

Licensing is partly legal, but it is also cultural. A project's license signals something about how it wants to participate in the open-source ecosystem.

For collaborative research repositories, it is often worth pairing the code license with clear guidance on:

* attribution expectations
* contribution workflow
* data or documentation licensing, if different from the code

That combination makes the repository easier to understand and safer to contribute to.
