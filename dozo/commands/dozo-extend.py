from dozo.config    import db
from dozo.commands  import BaseCommand, CommandError
from os import path
from os import mkdir

class Command(BaseCommand):
    """
    Path to extend options commands.
    """
    
    # command information
    usage = '--dozo-extend /path/to/extend/options/command'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):
        
        conf = db.stored_config()        
        path_extend = self.args.get_value('--dozo-extend')
        if path_extend is None:
            try:
                del conf['dozo-extend'] 
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
                f.write('__name__="dozo-extend"\n')
                f.close()

            path_command = '%s/commands' % path_extend

            if not path.isdir(path_command):
                mkdir(path_command)
            
            path_to_file = '%s/__init__.py' % path_command
            if not path.isfile(path_to_file):
                f = open(path_to_file,'w+')
                f.write('__name__="commands"\n')
                f.close()

            conf['dozo-extend'] = path_extend
