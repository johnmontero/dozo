import os
import sys
import types
from dozo.config    import get_config_value


def get_extend_commands(test_path_extend=None):
    """
    Returns a list of all the command names that are available.

    Returns an empty list if no commands are defined.
    """
    if test_path_extend is None:
        command_dir = '%s/commands' % get_config_value('path-extend')
    else:
        command_dir = '%s/commands' % test_path_extend
    
    try:
        return [f[:-3] for f in os.listdir(command_dir)
                if not f.startswith('_') and f.endswith('.py')]
    except OSError:
        return []

def load_extend_commands(name, test_path_extend=None):

    if test_path_extend is None:
        path_extend = get_config_value('path-extend')
    else:
        path_extend = test_path_extend

    if path_extend is None:
        return path_extend

    path_ext = ('/'.join(path_extend.split('/')[:-1]))
    path_ext_cmd = path_extend.split('/')[-1:]
            
    if  path_ext not in sys.path:
        sys.path.append(path_ext)
            
    full_name = '%s.commands.%s' % ('/'.join(path_ext_cmd[-1:]), name)

    try:
        __import__(full_name)
    except Exception, error:
        print error
        sys.exit(1)

    return sys.modules[full_name].Command
