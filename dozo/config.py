from guachi import ConfigMapper
import os


# Fixes Database Absolute Location
FILE_CWD = os.path.abspath(__file__)
FILE_DIR = os.path.dirname(FILE_CWD)
DB_FILE = FILE_DIR+'/dozo.db'

db = (lambda db_file: ConfigMapper(db_file))(DB_FILE)

def get_config_value(key):
    conf = db.stored_config()

    try:
        value = conf[key]
    except KeyError:
        value  = None
    return value
