from dozo.config    import db
from dozo.commands  import BaseCommand, CommandError
from os import path

class Command(BaseCommand):
    """
    Path to extend subcommand.
    """
    
    # command information
    usage = '--dozo-extend /path/to/extend/subcommand'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):
        
        conf = db.stored_config()        
        value = self.args.get_value('--dozo-extend')
        if value is None:
            try:
                del conf['dozo-extend'] 
            except KeyError:
                pass
        else:
            if '-' in '/'.join(value.split('/')[-1:]):
                raise CommandError("\nIs not character valid '-'.\n")

            if path.isdir(value):
                conf['dozo-extend'] = value
            else:
                raise CommandError("\nIs not directory %s\n" % value)