(chap_cheatsheet)=
# Git and GitHub Cheat Sheet

About 99% of the commands you'll type in `git` are summarized in the table below:


| Functionality                                               | Git Command                                                          |
|-------------------------------------------------------------|----------------------------------------------------------------------|
| See active branch and uncommitted changes                   | `git status`                                                         |
| Change branch                                               | `git checkout <branch name>`                                         |
| Create new branch and change to it                          | `git checkout -b <new branch name>`                                  |
| Stage file changes                                          | `git add <filename>`                                                 |
| Commit staged changes                                       | `git commit -m "message describing changes"`                         |
| Push committed changes to remote branch                     | `git push origin <branch name>`                                      |
| Update local information from upstream                      | `git fetch upstream`                                                 |
| Merge upstream main into local main                         | `git checkout main` then `git merge upstream/main`                   |
| Merge local main into your feature branch                   | `git checkout <feature branch>` then `git merge main`                |
| List current tags                                           | `git tag`                                                            |
| Create a new tag                                            | `git tag -a v<version number> -m "message with new tag"`             |
| Fast-forward local branch from a remote when possible       | `git pull --ff-only`                                                 |
| See unstaged changes                                        | `git diff`                                                           |
| See staged changes                                          | `git diff --staged`                                                  |
| Clone a remote repository                                   | `git clone <url to remote repo>`                                     |
