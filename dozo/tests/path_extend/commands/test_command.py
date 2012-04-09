# -*- coding: utf-8-*-
from tambo import Transport

from dozo.config    import db
from dozo.config    import get_config_value

class Command(object):
    """
    test_command related actions:

    --h, --help, help     Prints this help text and exits.

    print                 Print description of the test_command

    """

    help = "Commands associated with test_command"


    def __init__(self, argv, conf=None):
        self.argv = argv
        self.config = conf or db.stored_config()
        self.actions = {
            'print'     : self.test_command_print
        }

    def test_command_print(self):
        print "Print of test command"

    def parse_args(self):
        transport = Transport(self.argv, check_help=False)
        transport.catch_help = self.__doc__
        if len(self.argv) <= 1:
            transport.print_help()
        transport.parse_args()

        for action in self.actions:
            if transport.has(action):
                return self.actions.get(action)()

        # If nothing matches, print the help
        transport.print_help()