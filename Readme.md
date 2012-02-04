* PyDiskMonitor *

A tiny Qt-based application that monitors UDisks for new removable devices,
matches them against a set of rules and executes custom scripts.

The rules consist of multiple lines, each one of which might be a list of
comma-delimited key-value pairs. If a device matches all the key-value pairs on
any line, it matches that rule and the whole ruleset. 

The valid rule keys are `fs_label`, `fs_uuid`, `mount_path`, `model`, `vendor`,
and `dev_file`. 

* Requirements *

Requires: PyQt4, dbus-python, pyparsing
