#!/usr/local/bin/python3

# imports the re module for regular expressions
import re 





#
# There are a couple of different ways to open files in python.
# You could open the file, do things, and then close it manually
# or you could use what is called a context manager.
#
# Here is a traditional file open/close scheme:
#   f = open('file.txt','r')
#   do_stuff()
#   f.close()
#
# Here is an example of a context manager. Note that the context mananager closes the file automatically under the with() header
# Without this, you would have to call open() on the file, then close() on the file manually
#
#   with open('source_material.html','r') as f:
#       do_stuff()
#
