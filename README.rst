dozo: typing commands on the fly.
=================================

Installation
------------
If you have Setup Tools installed (along with Python) in your machine you can do::

    sudo pip install dozo

If you download the tar.gz file or the source code, use the setup.py file to install it::

    python setup.py install


How do Use?
-----------
Specify the directory that will have your own code, with the option::

    dozo --cmd-path-ext /home/dozo/dozo_extend

Indicate the name of your own choice dozo extended to create, 
with the option::

    dozo --cmd-create hello

Run your choice, with the option::

    dozo --hello
    Please use option:
        dozo --hello value

    dozo --hello dozo
    Option: --hello
    Value : dozo

Options
-------
    **--version, version**      Shows the current installed version
    **--cmd-create**            Create extend command
    **--cmd-edit**              Edit extended command
    **--cmd-path-ext**          Path to extend commands
    **--conf-add**              Add config value
    **--conf-del**              Delete config value
    **--conf-export**           Export the current configuration values used
    **--conf-import**           Import the configuration values new
    **--conf-values**           Displays the current configuration values used

Questions? Requests?
---------------------

Fork the project and start contributing.

If you have any ideas or suggestions send me an email: jmonteroc at gmail dot com
