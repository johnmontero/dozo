import os
from guachi 		import ConfigMapper

#from dozo.config    import db
from dozo.util      import get_extend_commands
from dozo.util      import load_extend_commands

describe "valid extend commands":

    it "not exists extended commands":
        assert get_extend_commands() == []

    it "can't load the extended commands":
    	assert load_extend_commands("config") == None

describe "get extend commands":
  
    before all:
        # Fixes Database Absolute Location
        file_cwd = os.path.abspath("./")
        file_dir = os.path.dirname(file_cwd)
        self.db_file = file_dir+"/tests/test_dozo.db"

        db = ConfigMapper(self.db_file)
        self.config = db.stored_config()
        self.config["path-extend"] = file_dir+"/tests/path_extend"

    after all:
        try:
            os.remove(self.db_file)
        except:
            pass # who cares if you can't


    it "get the list of extended commands":
        cmds = get_extend_commands(self.config["path-extend"])
        assert cmds == ['test_command']
    
    it "load and execute extended test command":
        cmd = load_extend_commands('test_command',
        	    self.config["path-extend"])(['dozo','test_command','print'])
        assert cmd.parse_args() ==  "Print of test command"
