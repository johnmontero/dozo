Dozo
====

The main goal is to get Dozo is the base of one application of line command for
create and run your own code written in python as options own of Dozo.


Installation
------------
If you have Setup Tools installed (along with Python) in your machine you can do::

    sudo pip install dozo

If you download the tar.gz file or the source code, use the setup.py file to install it::

    python setup.py install


How do Use?
-----------
You only need two steps::
    
* First specify the directory that will have your own code,
  with the option::

    dozo --dozo-extend /home/dozo/dozo_extend

* Second indicate the name of your own choice dozo extended to create,
  with the option::

    dozo --dozo-create hello

* Third run your choice, with the option::

    dozo --hello


.. highlight:: ruby

::

	dozo: Run your own subcommand

	Version: 0.0.1

	Run:
    	dozo [options]  

	Options:
    	--version, version      Shows the current installed version
    	--config-add            Add config value
    	--config-del            Delete config value
    	--config-export         Export the current configuration values used
    	--config-import         Import the configuration values new
    	--config-values         Displays the current configuration values used
    	--dozo-create           Create your own option command
    	--dozo-extend           Path to extend options commands






Questions? Requests?
---------------------

Fork the project and start contributing.
If you have any ideas or suggestions send me an email: jmonteroc at gmail dot com