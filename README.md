# commandman

***


![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/commandman)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/commandman?label=pypi%20downloads)](https://pypi.org/project/commandman/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/commandman)](https://github.com/smartlegionlab/commandman/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/commandman)](https://github.com/smartlegionlab/commandman/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/commandman)](https://pypi.org/project/commandman)
[![PyPI - Format](https://img.shields.io/pypi/format/commandman)](https://pypi.org/project/commandman)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/commandman?style=social)](https://github.com/smartlegionlab/commandman/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/commandman?style=social)](https://github.com/smartlegionlab/commandman/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/commandman?style=social)](https://github.com/smartlegionlab/commandman/)

***

## Short description:
___commandman___ - Console command manager.

***

Author and developer: ___A.A Suvorov.___

[![smartlegiondev@gmail.com](https://img.shields.io/static/v1?label=email&message=smartlegiondev@gmail.com&color=blue)](mailto:smartlegiondev@gmail.com)

***

## Help the project financially:

- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)
- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)
- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)
- Visa: 4048 0250 0089 5923

***

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).
    
***

## Images:

![commandman image](https://github.com/smartlegionlab/commandman/raw/master/data/images/commandman.png)

***

## What's new?

### ___commandman v0.3.1___

- Go to new version [smartcliapp](https://github.com/smartlegionlab/smartcliapp).

***

## Description:

___commandman___ - Cli command manager.

`pip install commandman`

The utility uses the package: [commandex](https://github.com/smartlegionlab/commandex).
The utility uses the package: [smartcliapp](https://github.com/smartlegionlab/smartcliapp).
The utility uses the package: [click](https://github.com/pallets/click) by [license](https://github.com/pallets/click/blob/main/LICENSE.rst).

***

Store your commands in one place for automatic
or manual launch and execution at any time.

It is convenient to store and run many commands for
automatic execution after system installation.

Recommended for use on `*nix` systems.

Possibilities:

- Storing named packages of commands in one file.
- Launching the execution of a batch or batch of commands from a file in automatic or manual mode.
- Add and run only certain packages.
- Exclusion of certain command packages from launch.
- Ability to run and skip command packets and individual commands in manual mode.

***

___File___ - a file in format 1 or 2 with the correct structure.

***

___A command package___ - name for grouping commands in a file.

***

___Command___ - a command to be executed in the console or terminal.

***

Create one or several files and store the necessary commands 
in them under names (in packages).  
The file must have the correct structure. 
At the moment, the simplest `*.cfg` and `*.json` are supported.

The file must have the correct structure.

***

`*.cfg` - The simplest file with command packages:

    [package name 1]
    command 1
    command 2
    command N
    [package name 2]
    command 1
    command 2
    command N

***

`*.json` - The simplest file with command packages:

```json
{
    "pack1":
      [
        "command1",
        "command2"
      ],
    "pack2":
      [
        "command1",
        "command2"
      ]
}
```

***

Packages:

Package names are placed in square brackets,
below the name are the commands included in this package.

***

Commands:

The commands are grouped under the desired names in packages.

***

To run the file use the command:

`python3 commandman.py [arguments] [file]`

A warning! If the file name contains spaces or invalid characters,
when typing a terminal, enclose it in quotation marks.

***

Arguments:

Using the `-a` option when starting the utility,
you can specify which command package to run using
the existing package name from the file. Use the option multiple
times to add multiple packages:

`python3 commandman.py -a name1 -a name2 -a name3 file.cfg`

Using the `-e` parameter, you can specify which command package
to exclude using the existing package name from the file.
Use the option multiple times to exclude multiple packages:

`python3 commandman.py -e name1 -e name2 -e name3 file.cfg`

A warning! If the command package name contains spaces or invalid characters,
when typing a terminal, enclose it in quotation marks.

The `--no-auto` option will cancel autorun of commands from the package.

Before executing each package and each command
the utility will ask for permission to execute.

The default is to autorun packages and commands `--auto`.

***

## Help:

### Install and Use:

#### Install:

- `pip3 install commandman`

#### Use:

- `commandman [options] [path to the file with command packages]`

#### Build your command packages using example files:

- [example.cfg](https://github.com/smartlegionlab/commandman/blob/master/data/configs/example.cfg)


A warning! If the command package name or file name 
contains spaces or invalid characters,
when typing a terminal, enclose it in quotation marks.

Try to name your packages and files with short, meaningful names.

#### Variant 1:

- Go to the project folder
- `python setup.py install`
- `commandman -h`

#### Variant 2:

- Go to the project folder
- `pip3 install -r requirements.txt`
- `python3 commandman.py [options] [path to the file]`

### Termux support:

#### Variant 1:

- Install [Termux](https://termux.com)
- `apt update`
- `pkg install python`
- Go to the project folder
- `python setup.py install`
- `commandman -h`
or
- `pip3 install -r requirements.txt`
- `python3 commandman.py [options] [path to the file]`

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2021, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
