# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# Url: https://github.com/smartlegionlab
# --------------------------------------------------------
import datetime
import os
import shutil
import sys

import click
from commandpack.executors import OsCommandExecutor
from commandpack.packmakers import make_pack_list

from commandman.config import Config


class ClickManager:

    def __init__(self, config):
        self.config = config

    def show_head(self):
        msg = self.smart_echo(text='', char='*')
        msg += self.smart_echo(f'{self.config.title}', '-')
        msg += self.smart_echo(f'{self.config.description}', '-')
        return msg

    def show_footer(self):
        msg = self.smart_echo(f'{self.config.copyright}', '-')
        msg += self.smart_echo(f'{self.config.url}', '*')
        return msg

    @staticmethod
    def echo(msg: str, print_flag=True) -> str:
        if print_flag:
            click.echo(str(msg))
        return msg

    def smart_echo(self, text='', char='-', print_flag=True):
        columns = self.term_width()
        symbol = ' ' if not char else char
        msg = f' {text} '.center(columns, symbol[:1]) \
            if text else f''.center(columns, symbol[:1])

        if print_flag:
            self.echo(msg)

        return msg

    @staticmethod
    def open_url(url):
        click.launch(url)

    def show_status(self, status, console=True):
        msg = 'Successfully!' if status else 'Error!'

        if console:
            self.echo(msg)

        return msg

    @staticmethod
    def get_action(title: str) -> bool:
        while 1:
            click.echo(f'{title} [y/n/e]?: ')
            char = click.getchar()

            if char.lower() in ('y', 'н'):
                return True
            elif char.lower() in ('n', 'т'):
                return False
            elif char.lower() in ('e', 'у'):
                sys.exit(0)

    @staticmethod
    def term_width():
        return shutil.get_terminal_size()[0]

    @staticmethod
    def input(title):
        return input(title)

    @staticmethod
    def print_via_pager(msg):
        try:
            click.echo_via_pager(msg)
        except (PermissionError, OSError):
            pass

    def __str__(self):
        return f'{self.config.title} {self.config.version} {self.config.copyright}.'


class CliManager(ClickManager):
    """Cli Manager"""

    def __init__(self, config):
        super().__init__(config)
        self.errors = []
        self._executor = OsCommandExecutor()

    @staticmethod
    def print_via_pager(msg):
        click.echo_via_pager(msg)

    def start(self, file, auto, add_list, exc_list):
        pack_list = make_pack_list(
            file=file,
            add_list=add_list,
            exc_list=exc_list
        )
        return self._work(pack_list=pack_list, auto=auto)

    def _work(self, pack_list, auto=True):
        len_pack_list = len(pack_list)
        sum_commands = sum([pack.count for pack in pack_list])
        self._print_start_report(len_pack_list, sum_commands)

        count_packs = 0
        count_commands = 0
        for pack in pack_list:
            count_packs += 1
            msg = f' [{count_packs}/{len_pack_list}] Package[{pack.name}]:Commands({pack.count}) '
            self.smart_echo(msg, '-')

            if not auto:
                action = self.get_action(f'Execute package [{pack.name}]')

                if not action:
                    self.echo(f'Command package: [{pack.name}] will not be launched.')
                    self.echo('Skip...')
                    continue
                else:
                    self.echo(f'Command package: [{pack.name}], will be launched for execution.')

            count = 0
            for command in pack.get_commands():
                count += 1
                msg = f'[{count}/{pack.count}] Command: [{command.name}]'
                self.smart_echo(f'Command: {count}')
                self.echo(msg)
                if not auto:
                    action = self.get_action('Execute command')

                    if not action:
                        self.echo('Skip...')
                        continue

                self.echo('Processing...')
                status = self._executor.execute(command.name)

                if not status:
                    self.errors.append(f'[error]:[{command.name}]')
                else:
                    count_commands += 1

                self.show_status(status=status)
                self.smart_echo(f'Pack[{pack.name}]:Done({count}/{pack.count})', '-')
        self._print_end_report(count_packs, count_commands)
        return count_packs, count_commands, self.errors

    def _print_start_report(self, len_pack_list, sum_commands):
        self.smart_echo('Start report:')
        msg = f'Starting the execution of command packages: '
        msg += f'[{datetime.datetime.today().strftime("%d.%m.%Y")} '
        msg += f'{datetime.datetime.today().strftime("%H:%M:%S")}].\n'
        msg += f'System: [{os.name}].\n'
        msg += f'Packs({len_pack_list}), Commands({sum_commands}).'
        self.echo(msg)
        return msg

    def _print_end_report(self, count_packs, count_commands):
        self.smart_echo('Report')
        msg = f'Execution of command packages finished: '
        msg += f'[{datetime.datetime.today().strftime("%d.%m.%Y")} '
        msg += f'{datetime.datetime.today().strftime("%H:%M:%S")}].\n'
        msg += f'Completed packages({count_packs}).\n'
        msg += f'Executed commands({count_commands}).\n'
        msg += f'Errors: {len(self.errors)}.'
        self.echo(msg)
        return msg


class ManagersBuilder:
    _config = Config()

    @classmethod
    def create_click_manager(cls):
        return ClickManager(config=cls._config)

    @classmethod
    def create_cli_manager(cls):
        return CliManager(config=cls._config)
