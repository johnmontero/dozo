from dozo.config    import db
from dozo.commands  import BaseCommand, CommandError

class Command(BaseCommand):
    """
    Displays the current configuration values used.
    """
    
    # command information
    usage = '--config-values'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):
        
        conf = db.stored_config()
        try:
            for i in conf.items():
                print "%-15s= %-4s" % (i[0], i[1])
            print ''
        except Exception, error:
            raise CommandError("Could not complete command: %s" % error)
