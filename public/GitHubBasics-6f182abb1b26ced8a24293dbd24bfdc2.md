(chap_basics)=
# Git and GitHub basics

This chapter introduces the key concepts that appear again and again in the rest of the book. A newcomer can learn Git commands by memorization, but it is much easier to build good habits if you first understand where your files live and which tool is responsible for which part of the workflow.

## Git versus GitHub

{term}`Git` is the version control software that runs on your local machine. It tracks changes to files, records those changes in {term}`commit`s, and helps you move changes between related copies of a {term}`repository`.

{term}`GitHub` is a website and collaboration platform built around Git repositories. GitHub hosts remote repositories and adds tools for code review, pull requests, issue tracking, access control, documentation hosting, and automated testing.

In short:

* Git tracks and moves changes.
* GitHub helps people collaborate around those changes.

## Repository, local clone, origin, and upstream

When you work on an open-source repository, there are usually three important places where the same project exists.

1. The main repository, often owned by an organization such as `PSLmodels`. This is usually called the {term}`upstream` repository.
2. Your personal copy of that repository on GitHub. This is called your {term}`fork`.
3. The copy on your computer created with `git clone`. This is your local repository.

When you clone your fork, Git automatically names that remote repository `origin`. In a fork-based workflow, you usually add the main organization repository as a second remote named `upstream`.

```{admonition} Typical naming convention
:class: note
For a repository `https://github.com/PSLmodels/project`, a beginner often works with the following:

* `upstream` = `https://github.com/PSLmodels/project`
* `origin` = `https://github.com/yourname/project`
* local repository = directory `project` on your computer
```

## Branches

A {term}`branch` is a named line of development. Branches let you work on one change without disturbing another.

For example, you might keep your local `main` branch synchronized with the latest tested code from `upstream/main`, while making your actual edits on a branch such as `fix-typo-intro` or `add-ci-docs`.

This is one of the most important beginner habits:

* keep `main` clean
* create a new branch for each distinct piece of work
* open a pull request from that branch

## The basic command cycle

Most day-to-day Git work follows the same pattern:

1. Update your local `main` branch from `upstream`.
2. Create a new branch from `main`.
3. Edit files.
4. Use `git status` to see what changed.
5. Use `git add` to stage the changes you want in the next commit.
6. Use `git commit -m "..."` to record a snapshot.
7. Use `git push origin your-branch-name` to upload the branch to GitHub.
8. Open a pull request on GitHub.

We walk through this process in detail in {ref}`chap_workflow`.

## `git add` and `git commit`

New users often confuse the staging area with a commit.

* `git add` puts selected file changes into the staging area.
* `git commit` records the staged changes as a new commit in your local history.

That two-step process is useful because it lets you decide exactly which changes belong together in a commit.

## `git fetch`, `git pull`, and `git push`

These commands all move information between repositories, but they do different things.

* `git fetch upstream` downloads new history from a remote without changing your working files.
* `git pull` is shorthand for `git fetch` followed by an integration step, usually a merge or rebase.
* `git push origin branch-name` uploads your local commits to a remote repository.

Because `git pull` performs two actions at once, beginners should understand what kind of integration behavior they want before using it automatically.

## `git pull` versus `git pull --ff-only` versus `git pull --rebase`

These three commands all begin by fetching new commits from the remote. They differ in what they do next.

### `git pull`

Plain `git pull` fetches changes and then integrates them using your current pull strategy. On many systems that means a merge. If your local branch and the remote branch have both moved forward, Git may create a merge commit.

This is convenient, but it can surprise beginners because a simple "get me up to date" command may create an extra commit.

### `git pull --ff-only`

This is the safest default for many beginners. A fast-forward-only pull succeeds only if Git can move your branch pointer forward without creating a merge commit.

If your branch has diverged from the remote, Git stops and tells you. That pause is helpful because it forces you to make an intentional decision about how to integrate your work.

### `git pull --rebase`

This command fetches remote commits and then reapplies your local commits on top of them. The resulting history is often linear and tidy, but rebasing rewrites commit history on your local branch.

Rebasing is extremely useful, but it is best used when you understand what it means to replay commits and when it is safe to force-push updated history.

```{admonition} Good beginner default
:class: tip
If you are still learning Git, `git pull --ff-only` is often a good habit for your local `main` branch. It avoids accidental merge commits and makes divergence visible right away.
```

## Pull requests

A {term}`pull request` or PR is a GitHub request asking maintainers to review and merge a branch. A PR is not just a code diff. It is also the place where collaborators discuss design choices, request changes, run automated tests, and document why a change was made.

In most PSLmodels-style workflows:

* you open a PR from your branch on your fork
* the PR targets the main branch of the upstream repository
* review comments lead to additional commits on the same branch
* the PR is merged only after discussion and testing pass

## Good beginner habits

The following habits prevent many common problems.

* Run `git status` often.
* Commit related changes together in small chunks.
* Write commit messages that explain the change.
* Open pull requests before your branch grows too large.
* Ask for help before resolving a confusing conflict by trial and error.
* Avoid working directly on `main`.

The next chapter puts these ideas together into a step-by-step collaborative workflow.
