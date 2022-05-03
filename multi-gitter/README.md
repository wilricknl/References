# Multi-gitter

A tool to make changes in multiple repositories simultaneously.

**Table of Contents**

- [Multi-gitter](#multi-gitter)
- [Information](#information)
- [Installation](#installation)
  - [Configure Git access token](#configure-git-access-token)
- [Options](#options)
- [Example usage](#example-usage)
  - [Run](#run)
  - [Status](#status)

# Information

* [multi-gitter Github](https://github.com/lindell/multi-gitter)
* License: Apache License 2.0
* Platforms: Linux, MacOS, Windows

# Installation

Download from [releases](https://github.com/lindell/multi-gitter/releases) or
install with the following command:

```shell
curl -s https://raw.githubusercontent.com/lindell/multi-gitter/master/install.sh | sh
```

## Configure Git access token

Optionally you can create an environment variable with an access token to the
Git server for easy access:

|        | Environment variable | How to create the access token?                                                                                             | Required permissions |
| ------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| GitHub | GITHUB_TOKEN         | [Tutorial](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) | `repo` permissions.  |
| GitLab | GITLAB_TOKEN         | [Tutorial](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)                                             | `api` permissions    |

# Options

The following options are available when using multi-gitter:

| Option | Description                                                                                             |
| ------ | ------------------------------------------------------------------------------------------------------- |
| run    | Clone repositories, run a script within each directory, and create a pull request with the new changes. |
| status | Get the status of pull requests.                                                                        |
| print  | Clone multiple repositories, run a script within each directory, and print the output of each run.      |
| merge  | Merge pull requests. Probably best not to use.                                                          |
| close  | Close pull requests.                                                                                    |

For each of the options a bunch of commandline arguments can be specified. The
available options can be found in the [documentation](https://github.com/lindell/multi-gitter#usage)
or by entering `multi-gitter <option>` in the terminal without any arguments.
It's also possible to configure multi-gitter using [configuration files](https://github.com/lindell/multi-gitter#usage).

# Example usage

My main usage of multi-gitter is to create pull requests in multiple
repositories and keeping track of the status of each pull request. In this
short example I will show how to do so using a simple configuration file.

This example will use a configuration file and a change script. The change
script is a simple Python script to change to year from 2022 to 2023 in the
LICENSE.

```yaml
# The email and name that will be used for the commit and pull request
author-email: 83393813+wilricknl@users.noreply.github.com
author-name: wilricknl

# Select platform and repository to update
platform: github
base-url: https://api.github.com/
repo: wilricknl/References
base-branch: main
# The name of the pull request branch
branch: multi-gitter-example

# When true, no merge requests will be made. This is great for testing
dry-run: true
# View the made changes before applying them
interactive: true

# The commit message that will be added to the change
commit-message: |
  Update year to 2023 in LICENSE

  This pull request is generated with multi-gitter by wilricknl.

# The title and description of the pull request
pr-title: Example pull request using multi-gitter
pr-body: |
  Update year to 2023 in the LICENSE.

  This pull request is generated with multi-gitter by wilricknl.
```

## Run

Now that the configuration and change are ready, we can use the `run` option to
apply the changes:

```shell
multi-gitter run "python3 $PWD/change.py" --config ./example.yaml
```

Within the parentheses we can specify any program or script to run. This gives
you the flexibility to use whatever language or program that you're most
comfortable with. Check the [documentation](https://github.com/lindell/multi-gitter#run-code-through-interpreter) 
for some more examples.

Don't forget about the access token. In this case I have mine set as an environment
variable `GITLAB_TOKEN`. For certain reasons I'm not sharing it in this tutorial.

## Status

To check the current status of the pull request use the `status` option:

```shell
multi-gitter status --config ./example.yaml
```
