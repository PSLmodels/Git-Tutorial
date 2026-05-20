(chap_gitconfig)=
# Setting up Git with git config

One reason Git feels personal to experienced users is that it can be configured to match your preferred workflow. Some settings are essential for everyone, while others are quality-of-life improvements that become more valuable as you use Git more often.

## Inspect your current configuration

To view your active settings and where they came from, run:

```bash
git config --list --show-origin
```

This is useful because Git settings can come from multiple scopes:

* system-wide configuration
* user-level global configuration
* repository-level local configuration

For most personal setup, you will want `--global`.

## Set your name and email

The first essential settings are your name and email, because Git records them in each commit.

```bash
git config --global user.name "Your Name"
git config --global user.email yourname@example.com
```

Use the email address you want associated with your GitHub contributions. If your GitHub account uses a privacy-protecting noreply address, you may prefer that instead of a personal email.

## Set your default editor

Git will sometimes open a text editor for commit messages, merge commits, or rebase instructions. Set an editor you are comfortable using.

For example, to use `vim`:

```bash
git config --global core.editor vim
```

If you prefer VS Code:

```bash
git config --global core.editor "code --wait"
```

We discuss editor integration further in {ref}`chap_vscode`.

## Choose a pull strategy

One helpful early choice is how `git pull` should behave. Many beginners are surprised when a pull creates a merge commit. If you want Git to update only when a fast-forward is possible, you can set:

```bash
git config --global pull.ff only
```

This is a good protective default for many new users.

Contributors who prefer rebasing local work onto updated remote history sometimes choose:

```bash
git config --global pull.rebase true
```

Either choice is better than leaving the behavior mysterious.

## Set the default branch name for new repositories

Many repositories now use `main` as the default branch name. To make newly initialized repositories match that convention:

```bash
git config --global init.defaultBranch main
```

## Credential helpers and authentication

Git needs a way to authenticate when you push to GitHub. That is usually handled through either HTTPS with a credential helper or SSH keys.

If you use HTTPS, a credential helper can save you from entering credentials repeatedly. The exact setup varies by operating system, but GitHub's authentication guides explain the options clearly.

If you use SSH, you will generate an SSH key pair, add the public key to GitHub, and clone or update remote URLs using the SSH form of the repository address.

```{admonition} Important note
:class: note
GitHub no longer accepts account passwords for command-line Git operations over HTTPS. If you use HTTPS, you will typically authenticate with a personal access token through a credential manager.
```

## Quality-of-life aliases

As you grow more comfortable with Git, you may want a few aliases for common commands. For example:

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
```

Aliases are optional. They are useful only if they make your workflow clearer rather than more cryptic.

## Keep configuration understandable

Git is extremely configurable, which is both a strength and a trap. A beginner should start with a small, understandable configuration and expand only as needed.

A sensible starting set is:

* `user.name`
* `user.email`
* `core.editor`
* `pull.ff only` or `pull.rebase true`
* `init.defaultBranch main`

For more information on configuring Git, see the official setup guide in *Pro Git* [here](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).
