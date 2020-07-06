[![PSL incubating](https://img.shields.io/badge/PSL-incubating-ff69b4.svg)](https://www.PSLmodels.org)

# <img src="https://raw.githubusercontent.com/PSLmodels/Git-Tutorial/master/jb_git_tutorial/jb_git_tutorial_logo.png" width=40 /> Git and GitHub Use, Collaboration, and Workflow (*IN PROGRESS*)
This repository will house the `Git` and [GitHub.com](https://github.com/) tutorial and training that many contributors to the [PSLmodels](https://github.com/PSLmodels) community use. This project uses [Jupyter Book](https://jupyterbook.org/intro.html) 0.7.1 to create the HTML and Jupyter notebook forms of the tutorial. We hope to add tutorial videos at some point in the future.


## Contributing to the book

We welcome contributions and updates to the content of the book. This is done by following fork/edit/pull-request workflow.

From your fork of this repository, you can generate your own version of the book by creating and activating a customized conda environment (virtual environment) and using the Jupyter Book build commands.


### Setting up the virtual environment

The virtual environment specifications are defined in the [`environment.yml`]() file. If you have not set up the conda environment, navigate to your Git-Tutorial repository folder in your terminal on your local machine and execute the following two commands. If you have already created the

```bash
conda env create -f environment.yml
conda activate jb-git-tutorial
```


## Building a Jupyter Book

Run the following command in your terminal:

```bash
jb build mini_book/
```

If you would like to work with a clean build, you can empty the build folder by running:

```bash
jb clean mini_book/
```

If jupyter execution is cached, this command will not delete the cached folder.

To remove the build folder (including `cached` executables), you can run:

```bash
jb clean --all mini_book/
```

## Publishing this Jupyter Book

This repository is published automatically to `gh-pages` upon `push` to the `master` branch.

## Notes

This repository is used as a test case for [jupyter-book](https://github.com/executablebooks/jupyter-book) and
a `requirements.txt` file is provided to support this `CI` application.
