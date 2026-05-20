[![PSL incubating](https://img.shields.io/badge/PSL-incubating-ff69b4.svg)](https://www.PSLmodels.org)

# <img src="https://raw.githubusercontent.com/PSLmodels/Git-Tutorial/master/book/_static/logo/jb_git_tutorial_logo.png" width=40 /> Git and GitHub Use, Collaboration, and Workflow
This repository houses the source code and content files for the open access, *Git and GitHub Use, Collaboration, and Workflow* book tutorial and training used by many contributors in the [PSLmodels](https://github.com/PSLmodels) community. This project uses [Jupyter Book](https://jupyterbook.org/intro.html) and MyST to create the published HTML version of the tutorial. The source lives in this GitHub repository, and the compiled book is available at [https://pslmodels.github.io/Git-Tutorial](https://pslmodels.github.io/Git-Tutorial). This project is maintained by [Richard W. Evans](https://sites.google.com/site/rickecon/) and [Jason DeBacker](https://www.jasondebacker.com/).


## Contributing to the book

We welcome contributions and updates to the content of the book. This is done by following fork/edit/pull-request workflow.

From your fork of this repository, you can generate your own version of the book by creating and activating a customized conda environment (virtual environment) and using the Jupyter Book build commands.


### Setting up the virtual environment

The virtual environment specifications are defined in the [`environment.yml`](environment.yml) file. If you have not set up the conda environment, navigate to your `Git-Tutorial` repository folder in your terminal on your local machine and execute the following two commands. If you have already created the conda environment, then simply activate it using the second command below (skip the first command).

```bash
conda env create -f environment.yml
conda activate jb-git-tutorial
```


### Building a Jupyter Book

Run the following command in your terminal from the `book` directory:

```bash
cd book
jupyter book build --all
```

If you would like to work with a clean build, you can empty the build folder by running:

```bash
jupyter book clean
```

If jupyter execution is cached, this command will not delete the cached folder.

To remove the build folder (including `cached` executables), you can run:

```bash
jupyter book clean --all
```

## Notes

This repository is actively maintained and contributions are welcome. The most helpful contributions usually improve tutorial clarity, correct command examples, add beginner-friendly explanations, or expand the hands-on workflow chapters.
