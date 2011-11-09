# -*- coding: utf-8-*-

import sys
from dozo.argopts   import ArgOpts
from dozo.commands  import CommandError
from dozo.util      import get_commands, run_command, get_sumary_commad
from dozo.util      import out, error

__version__         = '0.0.1'

class DozoCommands(object):

    dozo_help = """
dozo: Run your own subcommand

Version: %s

Run:
    dozo [options]  

Options:
    --version, version      Shows the current installed version.
""" % __version__


    def __init__(self, argv=None, test=True):
        self.test = test
        
        if argv is None:
            argv = sys.argv

        self.parseArgs(argv)

    def parseArgs(self, argv):

        """ Commands
        """
        commands    = get_commands()
        commands.sort()
        options  = ['--%s' % cmd for cmd in commands]
        options_help = ['    --%-20s  %-5s' % (cmd, get_sumary_commad(cmd))
                         for cmd in commands]

        self.dozo_help += '\n'.join(options_help)+'\n\n'

        
        """ Commands Extend
        """
        commands_ext = get_commands(extend=True)

        if len(commands_ext) is not 0:
            commands_ext.sort()
            options_ext  = ['--%s' % cmd for cmd in commands_ext]
            options_ext_help = ['    --%-20s  %-5s' % (cmd, get_sumary_commad(cmd))
                         for cmd in commands_ext]

            options.extend(options_ext)

            self.dozo_help += 'Options Extend:\n'+'\n'.join(options_ext_help)+'\n\n'
        
        args = ArgOpts(options)
        args.parse_args(argv)
                        
        if args.catches_help():
            out(self.dozo_help)

        elif args.catches_version():
            message = "dozo version %s\n" % __version__
            out(message)

        elif args.match:
            try:
                try:
                    run_command(args.match[0][2:]).execute(args)
                except CommandError, e:
                    error('%s\n' % e)
            except KeyboardInterrupt:
                out("Exiting from dozo.\n")
        else:
            out(self.dozo_help)


def main():
    DozoCommands()