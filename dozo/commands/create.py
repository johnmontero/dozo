from dozo.util      import get_commands
from dozo.config    import get_config_value
from dozo.commands  import BaseCommand, CommandError


TEMPLATE_SUBCOMMAND = '''
from dozo.config    import get_config_value
from dozo.commands  import BaseCommand, CommandError

class Command(BaseCommand):
    """
    %s description.
    """
    
    # command information
    usage = '--%s'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):
        print self.usage
'''

class Command(BaseCommand):
    """
    Create your own option command.
    """
    
    # command information
    usage = '--dozo-create name_option_command'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):

        value = self.args.get_value('--dozo-create')
        if value is not None:
            if value.endswith('.py'):
                raise CommandError("\nNot include '.py'\n")

            if value in get_commands() or value in get_commands(extend=True):
                raise CommandError("\nSubcommand %s exist.\n" % value)

            filename = '%s/commands/%s.py' % ( get_config_value('dozo-extend'),
                                               value )
            f = open(filename,'w+')    
            f.write(TEMPLATE_SUBCOMMAND)
            f.close()
        else:
            print "Please use options\n dozo %s\n" % self.usage