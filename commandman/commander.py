# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
import os

from commandex.executors import OsExecutor
from commandex.parsers import CfgParser
from commandex.filters import PackFilter
from commandex.makers import PackMaker
from smartcliapp import CliManager


class Commander:
    executor = OsExecutor()
    parser = CfgParser()
    filter = PackFilter()
    maker = PackMaker()


class CommandMan:
    def __init__(self):
        self._cli_man = CliManager()
        self._commander = Commander()
        self._errors = []

    @property
    def errors(self):
        return self._errors

    def run(self, file, add_list=None, exc_list=None, auto=True):

        exc_list = [] if exc_list is None else exc_list
        add_list = [] if add_list is None or exc_list else add_list

        pack_dict = self._commander.parser.parse(file)
        packs = self._commander.filter.filter_pack_dict(pack_dict, add_list, exc_list)
        pack_list = self._commander.maker.make_pack_list(packs)

        if not pack_list:
            self._cli_man.printer.base.echo(
                'No command packages found. '
                '(There may be an error in the file, '
                'or the file has the wrong structure).'
            )
        else:
            self._run(pack_list, auto)

    def _run(self, pack_list, auto=True):
        len_pack_list = len(pack_list)
        sum_commands = sum([pack.command_count for pack in pack_list])
        self._show_start_report(len_pack_list, sum_commands)
        count_packs = 0
        count_commands = 0
        for pack in pack_list:
            count_packs += 1
            msg = f'Package [{pack.name}] [{count_packs}/{len_pack_list}]  | Commands({pack.command_count}) '
            self._cli_man.printer.smart.echo(char='=')
            self._cli_man.printer.smart.echo(msg, '*')
            self._cli_man.printer.smart.echo(char='=')
            if not auto:
                action = self._cli_man.get_action(f'* Execute package [{pack.name}]?')
                if not action:
                    self._cli_man.printer.base.echo(f'Command package: [{pack.name}] will not be launched.')
                    self._cli_man.printer.base.echo('Skip...')
                    continue
                else:
                    self._cli_man.printer.base.echo(f'Command package: '
                                                    f'[{pack.name}], will be launched for execution.')
            count = 0
            for command in pack.commands:
                count += 1
                msg = f'[{count}/{pack.command_count}] Command: [{command}]'
                self._cli_man.printer.smart.echo(f'Pack: [{pack.name}] | command: {count}/{pack.command_count}')
                self._cli_man.printer.base.echo(msg)
                if not auto:
                    action = self._cli_man.get_action('Execute command?')

                    if not action:
                        self._cli_man.printer.base.echo('Skip...')
                        continue

                self._cli_man.printer.base.echo('Processing...')
                status = self._commander.executor.execute(command)

                if not status:
                    self._errors.append(f'[error]:[{command}]')
                else:
                    count_commands += 1

                self._cli_man.show_status(status=status)
        self._show_end_report(sum_commands=sum_commands, count_commands=count_commands)
        return count_packs, count_commands, self._errors

    def _show_start_report(self, len_pack_list, sum_commands):
        self._cli_man.printer.smart.echo('Start report:', '=')
        msg = f'System: [{os.name}] | Packs: [{len_pack_list}] | Commands: [{sum_commands}]'
        self._cli_man.printer.base.echo(msg)
        return msg

    def _show_end_report(self, sum_commands, count_commands):
        self._cli_man.printer.smart.echo('End Report:', '=')
        msg = f'Commands/Successfully/Errors: [{sum_commands}/{count_commands}/{len(self._errors)}]'
        self._cli_man.printer.base.echo(msg)
        self._cli_man.printer.smart.echo()
        return msg
