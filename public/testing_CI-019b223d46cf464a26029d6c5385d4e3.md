(chap_testCI)=
# Continuous Integration (CI) and Unit Testing

As repositories grow, contributors need more than good intentions to keep the default branch working. They need automatic checks that run consistently for every proposed change. This is the role of {term}`continuous integration`, usually abbreviated as CI.

## What CI does

Continuous integration is the practice of running automated checks whenever code is pushed or a pull request is opened or updated. In GitHub-based projects, these checks are often run with GitHub Actions, but the basic idea is broader than any one platform.

Typical CI jobs include:

* running unit tests
* running style or lint checks
* building documentation
* checking that notebooks or examples execute successfully
* measuring code coverage

The purpose of CI is not to replace human review. It is to catch routine problems quickly and consistently so reviewers can focus on design, correctness, and maintainability.

## Unit testing, regression testing, and CI

These ideas are related, but they are not identical.

### Unit testing

Unit tests check small, individual pieces of the code base. A unit test might verify that one function returns the expected output for a known input.

### Regression testing

Regression tests check that behavior that used to work still works after a change. A regression test may be a unit test, but it can also be a larger end-to-end or integration-style test that guards against reintroducing a known bug.

### Continuous integration

CI is the automation framework that runs tests and other checks whenever the repository changes. CI is the delivery mechanism, not the test itself.

## Why this matters in collaborative repositories

In a shared repository, a broken default branch creates friction for everyone. CI lowers that risk by making sure that each pull request is evaluated under the same rules.

For PSLmodels-style collaboration, CI is especially valuable because repositories often combine code, documentation, examples, and research outputs. A pull request may look harmless in one file while breaking something important elsewhere.

## What a healthy CI setup looks like

A good CI setup is usually:

* fast enough that contributors will actually pay attention to it
* reliable enough that failures usually mean something real
* broad enough to test the most important project behavior
* visible in pull requests so contributors and reviewers can act on results

For a small project, that might mean only a few checks. For a mature project, it might involve several operating systems, multiple Python versions, documentation builds, and separate slow-running jobs.

## A simple CI path for a Python project

Many Python repositories start with something like the following:

1. install project dependencies
2. run the test suite
3. run formatting or linting checks
4. optionally collect coverage

If the project publishes documentation, another good early step is to add a documentation build check so broken examples or malformed Markdown are caught before merge.

## Code coverage

Coverage tools measure how much of your code is exercised by the test suite. Coverage is useful, but it should be interpreted carefully.

Coverage can answer:

* Did our tests execute this function at all?
* Which files have very little test attention?

Coverage cannot answer:

* Are the tests meaningful?
* Do the tests assert the right behavior?
* Are the most important edge cases covered?

High coverage is not the same thing as high quality. Still, coverage reports can be useful for spotting neglected parts of a code base.

## Test-driven development

Test-driven development, or TDD, is the practice of writing a failing test before implementing the code that makes it pass. Some teams use TDD heavily, while others use it selectively.

Even if a project does not follow TDD strictly, it is still a strong habit to add or update tests whenever behavior changes.

## Good contributor habits around CI

* Run relevant tests locally before pushing, when practical.
* Read the CI failure output rather than guessing.
* Keep fixes for a failing check on the same pull request branch.
* Treat flaky tests as real maintenance problems.
* Make sure documentation changes are tested if the repo has docs automation.

## Good maintainer habits around CI

* Keep required checks clear and documented.
* Avoid adding slow or brittle checks without strong benefit.
* Make failure messages readable.
* Update CI when the supported environment changes.
* Keep secrets and deployment credentials out of general-purpose workflows.

## Start simple

Beginners sometimes think a project needs an elaborate CI system before it can benefit from automation. In practice, even a single workflow that installs dependencies and runs tests can dramatically improve collaboration quality.

The best CI setup is usually one that the team understands, trusts, and maintains.
