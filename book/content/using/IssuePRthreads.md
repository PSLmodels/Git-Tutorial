(chap_threads)=
# Issue Threads and PR Threads

GitHub is not just a place to store code. It is also the record of why a project changed, who discussed the change, what concerns were raised, and how the final decision was made. Two of the most important parts of that record are issue threads and pull request threads.

## Issue threads

An issue thread is the right place to discuss a problem, idea, bug report, or proposed enhancement before code is merged.

Issues are especially useful for:

* reporting a bug
* proposing a new feature
* asking whether a change would be welcome
* documenting design decisions
* giving newcomers a place to ask clarifying questions

For new contributors, issues reduce wasted effort. A quick issue can confirm that a problem is real, that a maintainer agrees with the direction, and that nobody else is already solving the same thing.

## Pull request threads

A pull request thread is where a proposed code change is reviewed. Unlike an issue, a PR thread is attached to a concrete set of commits and file diffs.

PR threads are where collaborators:

* review the implementation
* ask for revisions
* discuss tradeoffs
* link related issues
* confirm that tests and documentation are adequate

The PR thread becomes part of the long-term project history, which is valuable when future contributors want to understand why a change was accepted.

## How issues and PRs work together

In many healthy repositories, the flow looks like this:

1. An issue identifies a problem or desired improvement.
2. Someone opens a branch and implements a fix.
3. A pull request references the issue.
4. Review discussion happens in the PR.
5. Once merged, the issue is closed.

This structure keeps problem definition and code review related, but distinct.

## Good habits in issue threads

* Use a clear title.
* Include steps to reproduce a bug when relevant.
* Explain the expected behavior and the actual behavior.
* Link to related PRs, commits, or outside references.
* Be specific about what help you need.

## Good habits in PR threads

* Explain what changed and why.
* Keep PRs focused on one main task.
* Respond to review comments directly in the thread.
* Push follow-up commits to the same branch rather than opening a new PR for each revision.
* Say when you intentionally did not make a suggested change and explain why.

## Why this matters in PSLmodels-style collaboration

Many PSLmodels repositories support research, teaching, and policy analysis. In that setting, the discussion around a change can be almost as important as the final code itself.

A good issue or PR thread helps future contributors answer questions such as:

* Why was this modeling choice made?
* Was an alternative approach considered?
* Did maintainers expect follow-up work?
* Were there known limitations at the time of merge?

That kind of written context makes collaboration more scalable and lowers the cost of onboarding new contributors.
