#!/usr/local/bin/python3

# you can use help($libraryname) in python REPL to look at syntax of a library or help($libraryname.functioncall) for a
# function.

#example: help(sys.argv) in REPL
# google is your friend

import sys
import webbrowser # library to open a web page

page = 'https://google.com/maps/place/'
args = sys.argv[1:]
joined_string = "+".join(args)
print(joined_string)
webbrowser.open(page+joined_string)
