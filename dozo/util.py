import os
import sys
import types
from dozo.config    import get_config_value


def get_commands(extend=False):
    """
    Returns a list of all the command names that are available.

    Returns an empty list if no commands are defined.
    """
    if extend:
        command_dir = '%s/commands' % get_config_value('path-extend')
    else:
        command_dir = os.path.join('/'.join(__file__.split('/')[:-1]), 'commands')
    
    try:
        return [f[:-3] for f in os.listdir(command_dir)
                if not f.startswith('_') and f.endswith('.py')]
    except OSError:
        return []


def load_command_class(name):
    full_name = 'dozo.commands.%s' % name
    try:
        __import__(full_name)
    except:
        path_ext = ('/'.join(get_config_value('path-extend').split('/')[:-1]))
        path_ext_cmd = get_config_value('path-extend').split('/')[-1:]
            
        if  path_ext not in sys.path:
            sys.path.append(path_ext)
            
        full_name = '%s.commands.%s' % ('/'.join(path_ext_cmd[-1:]), name)

        try:
            __import__(full_name)
        except Exception, error:
            #sys.stderr.write(error)
            print error
            sys.exit(1)

    return sys.modules[full_name].Command()


def run_command(command):
    try:
        klass = load_command_class(command)
    except (KeyError, ImportError):
        sys.stderr.write("Unknown command: %r\nType 'dozo' for usage.\n" % \
                (command))
        sys.exit(1)
    return klass


def out(msg):
    sys.stdout.write(msg)
    sys.stdout.flush()


def err(msg):
    sys.stderr.write(msg)
    sys.stderr.flush()


def error(msg, exit=True):
    err("ERROR: %s" % msg)
    if exit:
        sys.exit(1)

get_sumary_commad = lambda command: load_command_class(command).summary
