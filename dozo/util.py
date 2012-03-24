import os
import sys
import types
from dozo.config    import get_config_value


def get_cmds_extend():
    """
    Returns a list of all the command names that are available.

    Returns an empty list if no commands are defined.
    """
    command_dir = '%s/commands' % get_config_value('path-extend')
    
    try:
        return [f[:-3] for f in os.listdir(command_dir)
                if not f.startswith('_') and f.endswith('.py')]
    except OSError:
        return []

def load_cmd_extend(name):
    path_ext = ('/'.join(get_config_value('path-extend').split('/')[:-1]))
    path_ext_cmd = get_config_value('path-extend').split('/')[-1:]
            
    if  path_ext not in sys.path:
        sys.path.append(path_ext)
            
    full_name = '%s.commands.%s' % ('/'.join(path_ext_cmd[-1:]), name)

    try:
        __import__(full_name)
    except Exception, error:
        print error
        sys.exit(1)

    return sys.modules[full_name].Command

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
