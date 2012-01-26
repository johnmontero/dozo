from os import path

from dozo.config    import get_config_value
from dozo.commands  import BaseCommand, CommandError

import envoy

class Command(BaseCommand):
    """
    Edit extended command.
    """
    
    # command information
    usage = '--cmd-edit extend-command'
    summary = __doc__.strip().splitlines()[0].rstrip('.')
    
    def handle(self):
        extend_command = self.args.get_value('--cmd-edit')
        if extend_command is None:
             print "Please use option:"
             print "   dozo %s" % self.usage
             return

        text_editor = get_config_value('text-editor')

        if text_editor is None:
             raise CommandError('''\n Text editor is not define.\n
Use:\n   dozo --config-add text-editor=vim\n''')

        path_extend =  get_config_value('path-extend')
        if path_extend is None:
            raise CommandError('''\n Path extend is not define.\n
Use:\n   dozo --path-extend /opt/dozo/dozo_extend''')

        filename = '{0}/commands/{1}.py'.format(path_extend, extend_command)

        if not path.isfile(filename):
            raise CommandError('\n{0}: Extend command not exist.\n'.format(
                                extend_command))

        cmd = '{0} {1}'.format(text_editor, filename)
        
        r = envoy.run(cmd)
        if r is not 0:
            raise CommandError('\n{0}\n'.format(r.std_err))

