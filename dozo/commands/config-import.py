from dozo.config    import db
from dozo.commands  import BaseCommand, CommandError

class Command(BaseCommand):
    """
    Import the configuration values new.
    """
    
    # command information
    usage = '--config-import /path/to/import-file.conf'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):
        
        conf = db.stored_config()
        filename = self.args.get_value('--config-import')
        if filename is not None:
            try:
                f = open(filename,'r+')
                for l in f.readlines():
                    key, value = l.replace('\n','').split('=')
                    conf[key.replace(' ','')] = value.replace(' ','') 
                f.close()
            except Exception, error:
                print "Could not complete command: %s" % error
        else:
            print "Please use options\n dozo %s" % self.usage
