from os import path
from os import mkdir

from tambo import Transport

from dozo.config    import db
from dozo.config    import get_config_value
from dozo.commands  import CommandError
  
class Command(object):
    """
    Config related actions:

    -h, --help, help     Prints this help text and exits.

    add                  Add config value
    del                  Delete config value
    values               Displays the current configuration values used
    export               Export the current configuration values used
    import               Import the configuration values new

    """

    help = "Commands associated with this config's Dozo"

    def __init__(self, argv, conf=None):
        self.argv = argv
        self.config = conf or db.stored_config()
        self.actions = {
            'add'           : self.config_add,
            'del'           : self.config_del,
            'values'        : self.config_values,
            'export'        : self.config_export,
            'import'        : self.config_import
        }

    def config_add(self):
        """
        Usage:

            dozo add key1=value1 key2=value2 ...

        Example:
        
            dozo add host=128.1.1.1 port=8080    

        """
        if len(self.argv) <= 2:
            print self.__doc__
            return

        try:
            for argv in self.argv:
                if argv not in ['config','add']:
                    key, value = argv.split('=')
                    if "DOZO" not in key.upper():    
                        self.config[key] = value
                    else:
                        print("'Dozo' is word reserved")
        except Exception, error:
            raise CommandError('Could not complete command "%s"' % error)

    def config_del(self):
        """
        """
        try:
            for key in self.argv:
                if key not in ['config','del']:
                    if "DOZO" not in key.upper():
                        try:
                            del self.config[key]
                        except KeyError:
                            print "key '%s' not found" % key
        except Exception, error:
            raise CommandError("Could not complete command: %s" % error)
            
    def config_values(self):
        """
        """
        try:
            for i in self.config.items():
                print "%-15s= %-4s" % (i[0], i[1])
            print ''
        except Exception, error:
            raise CommandError("Could not complete command: %s" % error)

    def config_export(self):
        """
        """
        filename = self.argv[2]
        if filename is not None:
            try:
                f = open(filename,'w+')
                for i in self.config.items():
                    f.write("%-15s= %-4s\n" % (i[0], i[1]) )
                f.close()
            except Exception, error:
                print "Could not complete command: %s" % error

    def config_import(self):
        """
        """
        filename = self.argv[2]
        if filename is not None:
            try:
                f = open(filename,'r+')
                for l in f.readlines():
                    key, value = l.replace('\n','').split('=')
                    self.config[key.replace(' ','')] = value.replace(' ','') 
                f.close()
            except Exception, error:
                print "Could not complete command: %s" % error

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
