from dozo.config    import db
from dozo.commands  import BaseCommand, CommandError

class Command(BaseCommand):
    """
    Delete config value.
    """
    
    # command information
    usage = '--config-del key1,key2,key3,...'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):
        
        conf = db.stored_config()        
        arg = self.args.get_value('--config-del')
        if arg is not None:
            try:
                for key in arg.split(','):
                    if "DOZO" not in key.upper():
                        try:
                            del conf[key]
                        except KeyError:
                            print "key '%s' not found" % key
            except Exception, error:
                raise CommandError("Could not complete command: %s" % error)
        else:
            print "Please use options\n dozo %s" % self.usage