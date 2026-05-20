[![PSL incubating](https://img.shields.io/badge/PSL-incubating-ff69b4.svg)](https://www.PSLmodels.org)

# <img src="https://raw.githubusercontent.com/PSLmodels/Git-Tutorial/master/book/_static/logo/jb_git_tutorial_logo.png" width=40 /> Git and GitHub Use, Collaboration, and Workflow
This repository houses the source code and content files for the open access, *Git and GitHub Use, Collaboration, and Workflow* book tutorial and training used by many contributors in the [PSLmodels](https://github.com/PSLmodels) community. This project uses [Jupyter Book](https://jupyterbook.org/intro.html) and MyST to create the published HTML version of the tutorial. The source lives in this GitHub repository, and the compiled book is available at [https://pslmodels.github.io/Git-Tutorial](https://pslmodels.github.io/Git-Tutorial). This project is maintained by [Richard W. Evans](https://sites.google.com/site/rickecon/) and [Jason DeBacker](https://www.jasondebacker.com/).


## Contributing to the book

We welcome contributions and updates to the content of the book. This is done by following fork/edit/pull-request workflow.

From your fork of this repository, you can generate your own version of the book by syncing the `uv` environment and using the Jupyter Book build commands.


### Setting up the environment

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency management. If you do not already have `uv` installed, follow the official installation instructions in the `uv` documentation.

Once `uv` is installed, navigate to your local `Git-Tutorial` repository folder and sync the project dependencies with:

```bash
uv sync
```


### Building a Jupyter Book

Run the following command in your terminal from the repository root:

```bash
make book
```

The `book` target first removes the existing Jupyter Book build artifacts and then performs a fresh site build using `uv run jupyter book build --all`.

## Notes

This repository is actively maintained and contributions are welcome. The most helpful contributions usually improve tutorial clarity, correct command examples, add beginner-friendly explanations, or expand the hands-on workflow chapters.
