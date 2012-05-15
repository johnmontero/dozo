from os import path
from os import mkdir

import pystache
import envoy
from tambo import Transport

from dozo.config    import db
from dozo.config    import get_config_value
from dozo.commands  import CommandError

TEMPLATE_OPTION_COMMAND = '''# -*- coding: utf-8-*-
from tambo import Transport

from dozo.config    import db
from dozo.config    import get_config_value

class Command(object):
    """
    {{name}} related actions:

    --h, --help, help     Prints this help text and exits.

    print                 Print description of the {{name}}

    """

    help = "Commands associated with {{name}}"


    def __init__(self, argv, conf=None):
        self.argv = argv
        self.config = conf or db.stored_config()
        self.actions = {
            'print'     : self.{{name}}_print
        }

    def {{name}}_print(self):
        print "Print {{name}}"

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

'''
  
class Command(object):
    """
    Command Extend related actions:

    -h, --help, help     Prints this help text and exits.

    create               Create subcommand
    edit                 Edit subcommand
    path                 Path to extend subcommands
    """

    help = "Commands associated with this commands extend's Dozo"


    def __init__(self, argv, conf=None):
        self.argv = argv
        self.config = conf or db.stored_config()
        self.actions = {
            'create'    : self.cmd_create,
            'edit'      : self.cmd_edit,
            'path'      : self.cmd_path_extend
        }
    
    def cmd_create(self):
        """
        """
        if len(self.argv) < 3:
            value = None
        else:
            value = self.argv[2]

        if value is not None:
            if value.endswith('.py'):
                raise CommandError("\nNot include '.py'\n")

            path_extend = get_config_value('path-extend')

            if path_extend is None:
                print "Path extend is not define."
                print "Use:\n   dozo extend path /path/to/extend"
                return

            path_to_file = "{0}/commands/{1}.py".format(path_extend,value)
            if path.isfile(path_to_file):
                print "\nOption command '{0}' exist.\n".format(value)

            filename = '%s/commands/%s.py' % ( path_extend, value )
            f = open(filename,'w+')    
            f.write(pystache.render(TEMPLATE_OPTION_COMMAND,
                    {'name':value}))
            f.close()

    def cmd_edit(self):
        """
        """
        try:
            extend_command = self.argv[2]
        except:
            extend_command = None

        if extend_command is None:
            #print "Please use option:"
            #print "   dozo %s" % self.usage
            return

        text_editor = get_config_value('text-editor')

        if text_editor is None:
             print "\n Text editor is not define.\n"
             print "Use:\n   dozo config add text-editor=vim\n"
             return

        path_extend =  get_config_value('path-extend')
        if path_extend is None:
            print('''\n Path extend is not define.\n
Use:\n   dozo config path-extend /opt/dozo/dozo_extend''')
            return

        filename = '{0}/commands/{1}.py'.format(path_extend, extend_command)

        if not path.isfile(filename):
            print('\n{0}: Extend command not exist.\n'.format(
                                extend_command))
            return

        cmd = '{0} {1}'.format(text_editor, filename)
        
        r = envoy.run(cmd)
        if r is not 0:
           print('\n{0}\n'.format(r.std_err))
        
    def cmd_values(self):
        """
        """
        try:
            for i in self.config.items():
                print "%-15s= %-4s" % (i[0], i[1])
            print ''
        except Exception, error:
            raise CommandError("Could not complete command: %s" % error)


    def cmd_path_extend(self):
        """
        """
        try:
            path_extend = self.argv[2]
        except:
            path_extend = None

        if path_extend is None:
            try:
                del self.config['path-extend'] 
            except KeyError:
                pass
        else:
            if '-' in '/'.join(path_extend.split('/')[-1:]):
                raise CommandError("\nIs not character valid '-'.\n")

            if not path.isdir(path_extend):
                mkdir(path_extend)

            path_to_file = '%s/__init__.py' % path_extend
            if not path.isfile(path_to_file):
                f = open(path_to_file,'w+')
                f.write('__name__="path-extend"\n')
                f.close()

            path_command = '%s/commands' % path_extend

            if not path.isdir(path_command):
                mkdir(path_command)
            
            path_to_file = '%s/__init__.py' % path_command
            if not path.isfile(path_to_file):
                f = open(path_to_file,'w+')
                f.write('__name__="commands"\n')
                f.close()

            self.config['path-extend'] = path_extend
        

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
