# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import click


class Config:

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
