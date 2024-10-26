# Contributing to this project

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

Please follow the guidelines below to ensure smooth collaboration.

## Table of Contents

- [How Can I Contribute?](#how-can-i-contribute)

- [Reporting Bugs](#reporting-bugs)

- [Suggesting Enhancements](#suggesting-enhancements)

- [Improving Documentation](#improving-documentation)

- [Submitting a Pull Request](#submitting-a-pull-request)

- [Code Style Guidelines](#code-style-guidelines)

## How Can I Contribute?

There are several ways you can contribute to this project:

- Reporting bugs and issues.

- Suggesting new features or enhancements.

- Submitting pull requests for bug fixes, new features, or documentation updates.

- Reviewing and commenting on open pull requests.

## Reporting Bugs

**If you find a security vulnerability, please refer to [SECURITY.md](SECURITY.md) to submit a vulnerability report to us.**

If you've encountered a bug, we appreciate your help in reporting it. Please follow these steps:

1. **Check for existing issues**: Before submitting a new bug report, please check if the issue has already been reported in [Issues](https://github.com/JacksonQu/Software-Supply-Chain-Security-Assignment1/issues)

2. **Create a detailed issue**: If the bug hasn't been reported yet, please provide the following details:

    - Clear title and description of the issue.

    - Steps to reproduce the issue, including any relevant configurations or input data.

    - Expected behavior vs. actual behavior.

    - Environment details (OS, Python version, dependencies).

    - Any screenshots or logs that can help diagnose the problem.

3. **Label appropriately**: Use appropriate labels (e.g., `bug`) to categorize the issue.

## Suggesting Enhancements

We welcome ideas for new features and improvements. If you have a suggestion, please:

1. **Search existing issues**: Make sure a similar suggestion hasn't already been discussed.

2. **Create a new issue**: If your suggestion is new, please create a new issue and include:

    - A detailed description of the enhancement or feature.

    - Why this feature would be useful.

    - Any possible implementation ideas (if applicable).

## Improving Documentation

Good documentation is vital for any project. You can help by:

- Fixing typos or improving clarity.

- Adding usage examples or better explanations.

- Updating outdated sections.

To contribute to documentation, please submit a pull request with your suggested changes.

## Submitting a Pull Request

### 1. Fork the repository

First, fork the repository by clicking the "Fork" button at the top right of the GitHub page. Clone your forked repo locally:

```bash
git clone https://github.com/{YOUR-USERNAME}/Software-Supply-Chain-Security-Assignment1
```

### 2. Create a new branch

Create a branch for your work to keep changes isolated:

```bash
git checkout -b feature-or-bugfix-branch
```

### 3. Make your changes

- Ensure the project works after your changes by running the necessary tests or performing manual testing.

### 4. Write clear commit messages

- Use concise and meaningful commit messages.

### 5. Ensure tests are passing

- If applicable, add tests for new features or bug fixes. Use the pytest framework (or any applicable framework) to run tests.

### 6. Open a Pull Request

- Once you're ready, push your branch to your forked repo.

```bash
git push origin feature-or-bugfix-branch
```

Then open a Pull Request from your branch into the main branch of the original repository. In your PR description, include:

- A summary of your changes.

- The related issue number (if applicable).

- Any additional context or information for the reviewers.

## Code Style Guidelines

To ensure consistency across the project, please follow these guidelines:

- **PEP 8**: Follow the Python [PEP 8](https://peps.python.org/pep-0008/) style guide.

- **Type hints**: Wherever possible, use type hints to improve code clarity and maintainability.

- **Linting**: Run flake8 or pylint to catch any style issues before submitting a PR.

- **Docstrings**: Add docstrings to functions and classes, describing the purpose, inputs, and outputs of the code.
