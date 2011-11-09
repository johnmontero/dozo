import sys

class CommandError(Exception):
    """
    Exception class indicating a problem while executing a management
    command.

    If this exception is raised during the execution of a management
    command, it will be caught and turned into a nicely-printed error
    message to the appropriate output stream (i.e., stderr); as a
    result, raising this exception (with a sensible description of the
    error) is the preferred way to indicate that something has gone
    wrong in the execution of a command.

    """
    pass


class BaseCommand(object):
    """
    The base class from which all management commands ultimately
    derive.
    """

    def __init__(self, args=None):
        self.args = args     
              
            
    def execute(self, args):
        self.args = args
        try:
            self.handle()
        except CommandError, e:
            sys.stderr.write('Error: %s\n' % e)
            sys.exit(1)

    def handle(self):
        """
        The actual logic of the command. Subclasses must implement
        this method.
        """
        raise NotImplementedError()
