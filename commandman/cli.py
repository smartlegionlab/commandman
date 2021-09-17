# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# Url: https://github.com/smartlegionlab
# --------------------------------------------------------
from commandman.config import ClickConfig
from commandman.managers import ManagersBuilder


@ClickConfig.click_group
@ClickConfig.click_version_option
@ClickConfig.click_argument_file
@ClickConfig.click_option_add_list
@ClickConfig.click_option_exc_list
@ClickConfig.click_option_auto
def cli(file, auto, add_list, exc_list):
    """
    commandman - Cross-platform console command manager.

    Store your commands in one place for automatic
    or manual launch and execution at any time.

    It is convenient to store and run many commands for
    automatic execution after system installation.

    Recommended for use on *nix systems.

    File - a file in format 1 or 2 with the correct structure.

    A command package - name for grouping commands in a file.

    Command - a command to be executed in the console or terminal.

    Create one or several files and store the necessary commands in them under names (in packages).

    The file must have the correct structure.

    At the moment, the simplest * .cfg and * .json are supported.

    The file must have the correct structure.

    *.cfg - The simplest file with command packages:

    \b
        [package name 1]
        command 1
        command 2
        command N
        [package name 2]
        command 1
        command 2
        command N

    *.json - The simplest file with command packages:

    \b
    {#
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


    Packages:

    Package names are placed in square brackets,
    below the name are the commands included in this package.

    Commands:

    The commands are grouped under the desired names in packages.

    To run the file use the command:

    python3 commandman.py [arguments] [file]

    Arguments:

    Using the -a option when starting the utility,
    you can specify which command package to run using
    the existing package name from the file. Use the option multiple
    times to add multiple packages:

    -a name1 -a name2 -a name3

    Using the -e parameter, you can specify which command package
    to exclude using the existing package name from the file.
    Use the option multiple times to exclude multiple packages:

    -e name1 -e name2 -e name3

    The --no-auto option will cancel autorun of commands from the package.

    Before executing each package and each command
    the utility will ask for permission to execute.

    The default is to autorun packages and commands --auto.

    Licensed under the terms of the BSD 3-Clause License.

    Copyright © 2018-2021, A.A Suvorov; All rights reserved.

    """
    cli_manager = ManagersBuilder.create_cli_manager()
    cli_manager.show_head()
    cli_manager.start(file, add_list=add_list, exc_list=exc_list, auto=auto)
    cli_manager.show_footer()
