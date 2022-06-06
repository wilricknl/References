# Pre-commit

A framework for managing and maintaining multi-language pre-commit hooks.

**Table of Contents**

- [Pre-commit](#pre-commit)
- [Information](#information)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Example `.pre-commit-config.yaml`](#example-pre-commit-configyaml)
- [Command line interface](#command-line-interface)
  - [Updating hooks](#updating-hooks)
  - [Cleaning cache](#cleaning-cache)
  - [Uninstalling hooks](#uninstalling-hooks)

# Information

* [pre-commit documentation](https://pre-commit.com/)
* License: MIT
* Platforms: Linux, MacOS, Windows

# Requirements

* Python3

# Installation

Pre-commit can be installed with `pip` as follows:

```shell
pip install pre-commit
```

# Usage

1. Create a `.pre-commit-config.yaml` with the hooks that you wish to 
   apply to the project.
2. Run `pre-commit install` to setup the git hook scripts. From then on
   all the hooks will be applied to every commit. This should be the
   first thing you do, when you clone a repository that makes use of
   `pre-commit`!
3. (optional) Run `pre-commit run --all-files` to run the hooks against
   all files within the repository. This is recommended when adding new
   hooks to the project.

## Example `.pre-commit-config.yaml`

More information on creating a configuration can be found 
[here](https://pre-commit.com/#adding-pre-commit-plugins-to-your-project).

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
```

# Command line interface

Pre-commit supports various commands to update hooks, clean cache and 
more. All commands can be found 
[here](https://pre-commit.com/#command-line-interface). The following
is a list of commands that are most useful.

## Updating hooks

Hooks can be updated as follows. By default, this will bring the hooks
to the latest tag on the default branch.

```shell
pre-commit autoupdate
```

## Cleaning cache

When getting errors executing `pre-commit` you can try cleaning the 
cache with the following command:

```shell
pre-commit clean
```

## Uninstalling hooks

Finally, hooks can be uninstalled from the project:

```shell
pre-commit uninstall
```
