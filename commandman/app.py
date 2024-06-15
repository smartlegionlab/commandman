# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
import click
from commandman.config import Config
from commandman.manager import CliMan


@Config.click_group
@click.version_option(version=f'{CliMan.name} {CliMan.version}; {CliMan.copyright};')
@Config.click_argument_file
@Config.click_option_add_list
@Config.click_option_exc_list
@Config.click_option_auto
def cli(file, add_list, exc_list, auto):
    """
    clipassman - Cross-platform console command manager.

    https://github.com/smartlegionlab/

    \b
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A. Suvorov
    All rights reserved.

    """
    CliMan.show_head()
    CliMan.commander.run(file, add_list, exc_list, auto)
    CliMan.show_footer()


if __name__ == '__main__':
    cli()
