#!/usr/local/bin/python3

import re
import os
search_string = '(\S+)\.'

filelist = os.listdir()

for item in filelist:
    if item != 'instructions.txt' and item != 'rename.py':
        match_object = re.search(search_string,item)
        command = f'mv {item} {match_object.group(1)}'
        os.system(command)
