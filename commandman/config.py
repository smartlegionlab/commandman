# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# Url: https://github.com/smartlegionlab
# --------------------------------------------------------
import click


class Config:
    name = 'commandman'
    title = 'Command Manager'
    description = 'Cross-platform console command manager.'
    version = '0.1.0'
    author = 'A.A Suvorov'
    email = 'smartlegiondev@gmail.com'
    url = 'https://smartlegion.ru'
    github_url = 'https://github.com/smartlegionlab'
    donate = 'https://smartlegionlab.github.io/donate'
    copyright = 'Copyright © 2018-2021, A.A Suvorov; All rights reserved.'
    license = 'BSD 3-Clause License'


class ClickConfig:
    click_group = click.group(
        context_settings={'help_option_names': ['-h', '--help']},
        invoke_without_command=True
    )
    click_argument_file = click.argument(
        'file',
        type=click.Path(exists=True)
    )
    click_option_add_list = click.option(
        "-a",
        "--add-list",
        multiple=True,
        type=click.STRING,
        help='The name of the package to run.'
    )

    click_option_exc_list = click.option(
        '-e', '--exc-list',
        multiple=True,
        help='The name of the package to exclude from startup.'
    )
    click_option_auto = click.option(
        '--auto/--no-auto',
        default=True,
        help='Automatic / Manual execution.'
    )
