(chap_attrib)=
# Attribution

One of the strengths of Git and GitHub is that they provide much more precise attribution than many older collaboration methods. In a healthy repository, you can usually tell not only who wrote a line of code, but also when it was added, what issue or pull request motivated it, and what discussion surrounded the change.

## Why attribution matters

Attribution is important for several reasons.

* It gives contributors visible credit for their work.
* It helps maintainers know who may understand a particular part of the repository.
* It supports reproducibility by showing when and why a change entered the project.
* It creates a richer record than a static author list on a paper or report.

This is especially valuable in open-source research collaboration, where software, documentation, and analysis may evolve over many years and across many contributors.

## Commits as attribution records

Every Git commit records an author, a timestamp, and a message. If commit messages are informative, the history becomes a useful project narrative rather than a list of opaque snapshots.

A good commit history helps answer questions such as:

* Who introduced this change?
* What problem was this commit trying to solve?
* Was this part of a larger refactor or a one-line fix?

## Pull requests as attribution plus review history

A pull request records more than authorship. It also preserves:

* the branch where the work happened
* the commits that made up the change
* review comments
* requests for revision
* links to related issues
* CI results at the time of review

That makes a PR thread one of the best places to understand the history and reasoning behind a change.

## `git blame`

The command `git blame` shows which commit last changed each line of a file.

```bash
git blame path/to/file
```

This is often the fastest way to identify the commit that introduced or revised a line you are trying to understand. From there, you can inspect the commit message or find the related pull request on GitHub.

## Attribution in an academic and research setting

In many academic settings, attribution is compressed into an author list, acknowledgments section, or changelog. Git and GitHub provide a much finer-grained record.

They can show:

* which contributor wrote or revised a section
* which contributor fixed a bug
* which reviewer requested an important change
* which maintainer ultimately approved the result

That level of detail can be very helpful for onboarding, collaboration, and transparency.

## A note of caution

Attribution tools are powerful, but they should be interpreted carefully. A line-based tool such as `git blame` identifies the most recent editor of a line, not necessarily the only person responsible for the underlying idea or design.

Use Git history as one source of evidence, and read related commits, issues, and PRs for fuller context.
