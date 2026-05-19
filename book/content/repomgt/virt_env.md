(chap_virtenv)=
# Virtual Environments

One of the first practical problems new contributors encounter is that the same repository may behave differently on different machines. Virtual environments help reduce that problem by isolating project dependencies from the rest of the system.

## Why virtual environments matter

Without an isolated environment, installing a package for one project can interfere with another project. Version conflicts become harder to diagnose, and reproducing another contributor's setup becomes much less reliable.

Virtual environments help by:

* keeping project dependencies together
* reducing accidental conflicts with global packages
* making installation steps more reproducible
* making onboarding easier for new contributors

## Conda environments

Many scientific Python projects use Conda because it manages both Python packages and non-Python dependencies well.

If a repository includes an `environment.yml` file, the usual workflow is:

```bash
conda env create -f environment.yml
conda activate jb-git-tutorial
```

If the environment already exists and the specification changed, contributors often update it with:

```bash
conda env update -f environment.yml --prune
```

The `--prune` option removes packages that are no longer listed in the environment specification.

## Python's built-in virtual environments

Some repositories prefer Python's built-in `venv` tool instead of Conda. A common pattern looks like this:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

This approach is lightweight and widely available, though it may require more manual handling of non-Python system dependencies.

## Which approach should a project choose?

There is no single best choice for every repository.

Conda is often a good fit when:

* the project has compiled dependencies
* contributors work across different operating systems
* the repository includes scientific or numeric libraries

`venv` is often a good fit when:

* the dependency stack is relatively simple
* the project is pure Python
* the team wants a minimal default setup

The important thing is to document one recommended path clearly.

## Reproducibility and lock-in

An environment file helps, but it does not guarantee perfect reproducibility forever. Package indexes change, upstream packages release new versions, and operating-system differences remain relevant.

For that reason, it is good practice to:

* keep dependency files under version control
* update them intentionally
* document the supported Python version
* mention platform-specific steps when needed

## Docker

Some projects go one step further and package the whole runtime in Docker. This can be useful when:

* the environment is complex
* the project includes services or system packages that are hard to install locally
* exact reproducibility matters a great deal

Docker is powerful, but it adds complexity. For many beginner-friendly repositories, a documented Conda or `venv` setup is the better starting point.

## Good repository habits

* Include one clearly documented environment setup path.
* Keep dependency specifications current.
* Avoid requiring contributors to guess which packages they need.
* Explain whether tests or docs require extra dependencies.
* Note when a project supports both Conda and `venv`, but recommend one default path.

For collaborative work, a virtual environment is not just a convenience. It is part of the repository's social contract: it helps contributors arrive at the same working setup with less trial and error.
