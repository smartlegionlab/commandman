# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import os

from commandpack.factories import Factory

from smartcliapp.managers import ClickMan


class CommandMan:
    def __init__(self):
        self._errors = []
        self._executor = Factory.tools.executors.get_os_executor()
        self._click_man = ClickMan()
        self._maker = Factory.tools.makers.get_pack_maker()

    @property
    def errors(self):
        return self._errors

    def run(self, file, add_list=None, exc_list=None, auto=True):

        if exc_list is None:
            exc_list = []

        if add_list is None:
            add_list = []

        pack_list = self._maker.make_pack_list(
            file=file,
            add_list=add_list,
            exc_list=exc_list
        )

        if pack_list:
            return self._run(pack_list=pack_list, auto=auto)
        else:
            self._click_man.printer.base.echo(
                'No command packages found. '
                '(There may be an error in the file, '
                'or the file has the wrong structure).'
            )

    def _run(self, pack_list, auto=True):
        len_pack_list = len(pack_list)
        sum_commands = sum([pack.count for pack in pack_list])
        self._show_start_report(len_pack_list, sum_commands)

        count_packs = 0
        count_commands = 0
        for pack in pack_list:
            count_packs += 1
            msg = f' [{count_packs}/{len_pack_list}] Package[{pack.name}]:Commands({pack.count}) '
            self._click_man.printer.smart.echo(msg)

            if not auto:
                action = self._click_man.action_man.get_action(f'Execute package [{pack.name}]?')

                if not action:
                    self._click_man.printer.base.echo(f'Command package: [{pack.name}] will not be launched.')
                    self._click_man.printer.base.echo('Skip...')
                    continue
                else:
                    self._click_man.printer.base.echo(f'Command package: '
                                                      f'[{pack.name}], will be launched for execution.')

            count = 0
            for command in pack.get_commands():
                count += 1
                msg = f'[{count}/{pack.count}] Command: [{command.name}]'
                self._click_man.printer.smart.echo(f'Command: {count}')
                self._click_man.printer.base.echo(msg)
                if not auto:
                    action = self._click_man.action_man.get_action('Execute command?')

                    if not action:
                        self._click_man.printer.base.echo('Skip...')
                        continue

                self._click_man.printer.base.echo('Processing...')
                status = self._executor.execute(command.name)

                if not status:
                    self._errors.append(f'[error]:[{command.name}]')
                else:
                    count_commands += 1

                self._click_man.status_man.show_status(status=status)
                self._click_man.printer.smart.echo(f'Pack[{pack.name}]:Done({count}/{pack.count})', '-')
        self._show_end_report(sum_commands=sum_commands, count_commands=count_commands)
        return count_packs, count_commands, self._errors

    def _show_start_report(self, len_pack_list, sum_commands):
        self._click_man.printer.smart.echo('Start report:')
        msg = f'System: [{os.name}] | Packs: [{len_pack_list}] | Commands: [{sum_commands}]'
        self._click_man.printer.base.echo(msg)
        return msg

    def _show_end_report(self, sum_commands, count_commands):
        self._click_man.printer.smart.echo('End Report:')
        msg = f'Commands/Successfully/Errors: [{sum_commands}/{count_commands}/{len(self._errors)}]'
        self._click_man.printer.base.echo(msg)
        self._click_man.printer.smart.echo()
        return msg
