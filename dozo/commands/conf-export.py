from dozo.config    import db
from dozo.commands  import BaseCommand, CommandError

class Command(BaseCommand):
    """
    Export the current configuration values used.
    """
    
    # command information
    usage = '--conf-export /path/to/export-file.conf'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
     
    def handle(self):
        
        conf = db.stored_config()
        filename = self.args.get_value('--conf-export')
        if filename is not None:
            try:
                f = open(filename,'w+')
                for i in conf.items():
                    f.write("%-15s= %-4s\n" % (i[0], i[1]) )
                f.close()
            except Exception, error:
                print "Could not complete command: %s" % error
        else:
            print "Please use options\n dozo %s" % self.usage
