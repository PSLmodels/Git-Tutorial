(chap_gitconfig)=
# Setting up Git with git config

Show how to set up Git and make it your own using git config.

To view all of your settings, you can type the following into your computers terminal:

```
git config --list --show-origin
```

When getting set up, it's important to enter your credentials so that `git` on your local machine is linked to your account on GitHub.  You'll do this by first entering your name:

```
git config --global user.name "Your Name"
```

Then, you'll enter your email (using the email that you used to register your account on GitHub.com):
```
git config --global user.email yourname@example.com
```

You can also set your default text editor for use with `git` by following the example below, which makes `vim` the default:

```
git config --global core.editor vim
```

We have some discussion in the {ref}`chap_vscode` Chapter about setting up VS Code as a `mergetool` and `difftool`.

For more information on configuing `git`, see the full instructions from `git` [here](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).
