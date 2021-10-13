# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import shutil
import sys
from abc import ABC, abstractmethod

import click


class PrinterBase(ABC):

    @abstractmethod
    def echo(self, text=''):
        """Abstract Printer"""


class DefaultPrinter(PrinterBase):
    @classmethod
    def echo(cls, text=''):
        print(text)
        return text


class ClickPrinter(PrinterBase):
    @classmethod
    def echo(cls, text='', color='white'):
        click.echo(click.style(text, fg=color))
        return text


class PagerPrinter(PrinterBase):
    @classmethod
    def echo(cls, text=''):
        try:
            click.echo_via_pager(text)
        except (PermissionError, OSError):
            pass


class SmartPrinter(PrinterBase):
    def_printer = DefaultPrinter()
    click_printer = ClickPrinter()

    @classmethod
    def echo(cls, text='', char='-', print_flag=True):
        printer = cls.def_printer
        columns = cls.term_width()
        symbol = ' ' if not char else char
        msg = f' {text} '.center(columns, symbol[:1]) \
            if text else f''.center(columns, symbol[:1])
        if print_flag:
            printer.echo(msg)
        return msg

    @classmethod
    def term_width(cls):
        return shutil.get_terminal_size()[0]


def def_print(text=''):
    printer = DefaultPrinter()
    return printer.echo(text)


def click_print(text='', color='white'):
    printer = ClickPrinter()
    return printer.echo(text, color)


def pager_print(text=''):
    printer = PagerPrinter()
    return printer.echo(text)


def smart_print(text='', char='-'):
    printer = SmartPrinter()
    return printer.echo(text, char)


class Printer:

    @classmethod
    def echo(cls, msg):
        def_print(msg)

    @classmethod
    def click_echo(cls, msg='', color='white'):
        click_print(click.style(msg, fg=color))

    @classmethod
    def smart_echo(cls, msg='', char='-'):
        smart_print(msg, char)

    @classmethod
    def pager_echo(cls, msg=''):
        pager_print(msg)


class PrintersFactory:
    @classmethod
    def get_printer(cls):
        return Printer()

    @classmethod
    def get_def_printer(cls):
        return DefaultPrinter()

    @classmethod
    def get_click_printer(cls):
        return ClickPrinter()

    @classmethod
    def get_smart_printer(cls):
        return SmartPrinter()

    @classmethod
    def get_pager_printer(cls):
        return PagerPrinter()

    @classmethod
    def get_func_def_print(cls):
        return def_print

    @classmethod
    def get_func_click_print(cls):
        return click_print

    @classmethod
    def get_func_smart_print(cls):
        return smart_print

    @classmethod
    def get_func_pager_print(cls):
        return pager_print


class ActionMan:
    printer = PrintersFactory.get_printer()

    @classmethod
    def get_action(cls, title: str) -> bool:
        while 1:
            cls.printer.echo(f'{title} [y/n/e]: ')
            char = click.getchar()

            if char.lower() in ('y', ):
                return True
            elif char.lower() in ('n',):
                return False
            elif char.lower() in ('e', ):
                sys.exit(0)


class Informer:
    printer = Printer()
    name = ''
    title = ''
    description = ''
    copyright = ''
    url = ''
    msg = ''
    version = '0.0.0'

    @classmethod
    def show_head(cls):
        cls.printer.smart_echo(char='*')
        cls.printer.smart_echo(cls.title, char='*')
        cls.printer.smart_echo(cls.description, char='*')

    @classmethod
    def show_footer(cls):
        cls.printer.smart_echo(cls.url, char='*')
        cls.printer.smart_echo(cls.copyright, char='*')
        cls.printer.smart_echo(char='*')


class InputMan:
    @classmethod
    def input(cls, title):
        return input(f'{title}: ')

    @classmethod
    def prompt(cls, title):
        return click.prompt(title)


class StatusMan:
    printer = PrintersFactory.get_printer()

    @classmethod
    def show_status(cls, status, show=True):
        msg = 'Ok!' if status else 'Error!'
        if show:
            cls.printer.echo(msg)
        return msg


class ClickMan:
    printer = PrintersFactory.get_printer()
    input_man = InputMan()
    status_man = StatusMan()
    action_man = ActionMan()
