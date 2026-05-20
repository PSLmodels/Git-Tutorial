(chap_advgit)=
# Advanced Git and GitHub

This chapter collects several topics that are very useful once you are comfortable with the standard fork, branch, commit, push, and pull request workflow. These tools are powerful, but they are best learned after the beginner workflow already feels familiar.

## Branching from someone else's branch

Sometimes you want to continue work that started on another contributor's branch. There are a few ways to do this, but the safest approach is usually:

1. fetch the relevant remote branch
2. create your own local branch from it
3. push your new branch to your own fork

For example:

```bash
git fetch upstream contributor-branch
git checkout -b continue-contributor-work FETCH_HEAD
git push origin continue-contributor-work
```

This keeps your work under your own branch name and avoids accidental pushes to someone else's branch.

## Opening a pull request based on another branch

Not every pull request has to target `main`. Sometimes a repository may ask you to build on top of an open feature branch. In that case, the pull request base branch may be another contributor's branch rather than the default branch.

This can be helpful when:

* a large feature is being built in stages
* a maintainer asks you to contribute to work already in progress
* several related PRs need to merge in a specific order

When doing this, be extra clear in the PR description about which branch your work depends on.

## `git reset`

`git reset` moves branch history or unstages changes, depending on how it is used. Because it can rewrite history, it deserves care.

Common safe uses include:

```bash
git reset HEAD path/to/file
git reset --soft HEAD~1
```

These are often used to:

* unstage a file
* redo the most recent commit while keeping the changes

Avoid more destructive forms until you are confident you understand the consequences.

## `git rebase`

Rebasing reapplies commits on top of a different base commit. This is often used to produce a cleaner, more linear history.

For example, to replay your feature branch on top of updated `main`:

```bash
git checkout my-feature-branch
git rebase main
```

Rebasing is especially helpful before opening a PR or when a maintainer prefers a linear project history. However, rebasing rewrites commit history. If you have already pushed the branch, updating GitHub may require a force-push:

```bash
git push --force-with-lease origin my-feature-branch
```

Use `--force-with-lease`, not plain `--force`, because it adds a useful safety check.

## `git blame`

`git blame` shows which commit most recently changed each line of a file. It is a powerful way to understand the history behind a particular piece of code or documentation.

```bash
git blame path/to/file
```

This command is most useful when used with curiosity rather than blame in the ordinary sense of the word. It helps you answer questions like:

* When was this line introduced?
* Who might know the background of this code?
* Which commit should I read next?

## Contribution summaries

Some projects use tools that summarize who contributed what. One example is [git-fame](https://github.com/casperdcl/git-fame), which reports contributor statistics such as lines changed, files touched, and contribution shares.

These tools can be interesting and occasionally useful for project maintenance, but they should never replace careful reading of commit history, issues, and PR discussions.
