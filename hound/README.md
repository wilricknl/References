# Hound

An extremely fast source code search engine.

**Table of Contents**

- [Hound](#hound)
- [Information](#information)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

# Information

* [hound Github](https://github.com/hound-search/hound)
* License: MIT
* Platforms: Linux, MacOS, Windows (not supported, but it works)

# Installation

Hound requires the Go programming language to be installed, which can be done
as specified below. The command to install latest version of Go can be found
[here](https://go.dev/doc/install).

```shell
sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.18.3.linux-amd64.tar.gz
```

Once Go is installed Hound can be installed with the followings commands:

```shell
git clone https://github.com/hound-search/hound.git
cd hound
go build ./cmds/hound
go build ./cmds/houndd
sudo mv hound houndd /usr/local/go/bin/
```

Now Hound should be accessible from commandline.

# Configuration

To start Hound a JSON configuration file is required to specify all 
repositories that you wish to search through. An example on how
to write such file can be found 
[here](https://github.com/hound-search/hound/blob/main/config-example.json).
To get started the following configuration can be used:

```json
{
    "dbpath" : "db",
    "repos" : {
        "Hound" : { "url" : "https://github.com/etsy/hound.git" },
        "References": { "url": "https://github.com/wilricknl/References.git" } 
    }
}
```

# Usage

In the folder where the configuration is stored the Hound server can be started
from commandline by calling `houndd`. By default Hound will run on 
`http://localhost:6080`. To search through the code there are two options:

1. Open the URL and search via the web interface.
2. Search via the commandline interface, e.g. `hound " license "`. Enter just
`hound` to get more information on available options.
