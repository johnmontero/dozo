from dozo.config    import db
from dozo.commands  import BaseCommand, CommandError
from os import path

class Command(BaseCommand):
    """
    Dozo extension subcommand.
    """
    
    # command information
    usage = '-dozo-ext /path/to/subcommand'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):
        
        conf = db.stored_config()        
        value = self.args.get_value('--dozo-ext')
        if value is None:
            try:
                del conf['dozo-ext'] 
            except KeyError:
                pass
        else:
            if path.isdir(value):
                conf['dozo-ext'] = value
            else:
                raise CommandError("Is not directory %s" % value)