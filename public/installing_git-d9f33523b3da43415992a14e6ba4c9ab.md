(chap_installgit)=
# Installing Git

Before you can use GitHub effectively from your local machine, you need Git installed in your terminal environment.

## Check whether Git is already installed

On many machines, Git is already available. You can check with:

```bash
git --version
```

If that command prints a version number, Git is installed. If not, you will need to install it.

## Use the official installation instructions

The most reliable installation instructions are maintained by the Git project itself:

[Git installation guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

That page covers macOS, Windows, and Linux.

## After installation

Installing Git is only the first step. After Git is available, most contributors should immediately continue with:

1. setting `user.name` and `user.email`
2. choosing an editor
3. setting up authentication for GitHub

Those next steps are covered in {ref}`chap_gitconfig` and {ref}`chap_gitacct`.

## A beginner sanity check

After installation, verify that Git runs from the same terminal where you plan to do your development work. This matters because some users have multiple terminals, shells, or Python environments and assume Git is available everywhere when it is not.

Once `git --version` works and Git can be found in your normal shell, you are ready to continue.
