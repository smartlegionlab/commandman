# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
from commandman import __version__
from commandman.commander import CommandMan
from smartcliapp import Informer


class CliMan(Informer):
    commander = CommandMan()
    name = 'commandman'
    title = 'CommandMan'
    description = 'Command manager'
    version = __version__
    copyright = 'Copyright © 2021, A.A Suvorov'
    url = 'https://github.com/smartlegionlab'
