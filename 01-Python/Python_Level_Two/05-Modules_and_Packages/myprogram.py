################
# Example Three:
################
# Uncomment this and comment everything else to run!

import mymodule
mymodule.func_in_mymodule()

################
# Example Two:
################
# Uncomment this and comment everything else to run!

import mymodule as mm
mm.func_in_mymodule()

################
# Example Three:
################
# Uncomment this and comment everything else to run!

from mymodule import func_in_mymodule
func_in_mymodule()

################
# Example Four:
################
# Uncomment this and comment everything else to run!

# This is posisble but frowned upon, often causes poorly readable code because
# you don't know what functions come from mymodule

from mymodule import *
func_in_mymodule()

##########################
# Packages and SubPackages

from MainPackage import some_main_script
from MainPackage.SubPackage import mysubscript

# import the functions from the module and/or package
some_main_script.report_main()
mysubscript.sub_report()

from MainPackage.some_main_script import report_main
