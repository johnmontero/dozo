# -*- coding: utf-8-*-
"""
dozo: typing commands on the fly.

Usage:
    dozo [subcommands]

    --h, --help, help     Prints this help text and exits.    
"""

import sys

from tambo import Transport

from dozo.util      import get_extend_commands
from dozo.util      import load_extend_commands
from dozo.commands  import config
from dozo.commands  import extend

__version__         = '0.0.2'

class DozoApp(object):

    mapper = {
        'config'    : config.Command,
        'extend'    : extend.Command
    }
    
    def __init__(self, argv=None, parse=True):
        self.argv = argv or sys.argv
        if parse:
            self.parse_args(self.argv)

    def get_extend_commands(self):
        cmds = get_extend_commands()
        if len(cmds) is not 0:
            for cmd in cmds:
                if cmd not in ['config','extend']:
                    self.mapper.update({ "%s" % cmd: 
                                     load_cmd_extend(cmd) })
                        
    def parse_args(self, argv):
        """
        Main method for parsing arguments, it uses whatever `argv` is although
        it should always be a list. Once it goes through the ``Transport`` class
        it tries to generate the help from the mapped classes and the current
        docstring for this module.

        If nothing matches it will return the help.
        """
        
        self.get_extend_commands()

        transport = Transport(argv, self.mapper)
        transport.catch_help    = "%s \n%s" % (__doc__, transport.subhelp())
        transport.catch_version = "dozo version {0}".format(__version__)
        if len(self.argv) <= 1:
            transport.print_help()
        transport.dispatch()

def main():
    DozoApp()
