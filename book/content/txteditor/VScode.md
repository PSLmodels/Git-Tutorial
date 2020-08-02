(chap_vscode)=
# VS Code Git Configuration

Show how to configure VS Code to efficiently interact with Git and GitHub.

## Mergetool and difftool

Great article, "[Using VSCode as git mergetool and difftool](https://medium.com/faun/using-vscode-as-git-mergetool-and-difftool-2e241123abe7)" by Kenichi Shibata, showing `gitconfig` setup for using VS Code as your Git mergetool and difftool. He suggests adding the following lines to the `.gitconfig` file.

```
# Add lines below to existing content in ~/.gitconfig file
[merge]
    tool = vscode
[mergetool "vscode"]s
    cmd = code --wait $MERGED
[diff]
    tool = vscode
[difftool "vscode"]
    cmd = code --wait --diff $LOCAL $REMOTE
```

The [Jupyter Book](https://jupyterbook.org/intro.html) documentation has a section in the [MyST Markdown Overview](https://jupyterbook.org/content/myst.html) chapter suggesting that if you are using VS Code to modify markdown files, you should download the [vscode MyST markdown extension](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) that provides highlighting and other features.
