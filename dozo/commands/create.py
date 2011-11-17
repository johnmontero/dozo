from dozo.util      import get_commands
from dozo.config    import get_config_value
from dozo.commands  import BaseCommand, CommandError

import pystache

TEMPLATE_OPTION_COMMAND = '''
from dozo.config    import get_config_value
from dozo.commands  import BaseCommand, CommandError

class Command(BaseCommand):
    """
    Description {{name}}.
    """
    
    # command information
    usage = '--{{name}} value'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
    
    def handle(self):
        value = self.args.get_value('--{{name}}')
        if value is not None:
            print "Option: --{{name}}"
            print "Value : %s" % value 
        else:
             print "Please use option:"
             print "   dozo %s" % self.usage
'''

class Command(BaseCommand):
    """
    Create your own option command.
    """
    
    # command information
    usage = '--create name_option_command'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):

        value = self.args.get_value('--create')
        if value is not None:
            if value.endswith('.py'):
                raise CommandError("\nNot include '.py'\n")

            if value in get_commands() or value in get_commands(extend=True):
                raise CommandError("\nOption command %s exist.\n" % value)

            filename = '%s/commands/%s.py' % ( get_config_value('dozo-extend'),
                                               value )
            f = open(filename,'w+')    
            f.write(pystache.render(TEMPLATE_OPTION_COMMAND,
                    {'name':value}))
            f.close()
        else:
            print "Please use options"
            print "   dozo %s" % self.usage