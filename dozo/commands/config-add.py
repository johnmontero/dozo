from dozo.config    import db
from dozo.commands  import BaseCommand, CommandError

class Command(BaseCommand):
    """
    Add config value.
    """
    
    # command information
    usage = '--config-add key=value'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):
        
        conf = db.stored_config()        
        arg = self.args.get_value('--config-add')
        if arg is not None:
            try:
                key, value = arg.split('=')
                if "DOZO" not in key.upper():    
                    conf[key] = value
                else:
                    print("'Dozo' is word reserved")
            except Exception, error:
                raise CommandError('Could not complete command "%s"' % error)
        else:
            print "Please use options\n dozo %s" % self.usage
    