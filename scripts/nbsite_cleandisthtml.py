#!/usr/bin/env python

"""_Title.ipynb -> The Title



"""

import os
import shutil
import sys

# if only someone had made a way to handle parameters
output = sys.argv[1]
htmldir = os.path.abspath(output)
dry_run =  not (len(sys.argv)>2 and sys.argv[2] == 'take_a_chance')

def IGetFiles(d):
    for thing in os.scandir(d):
        if thing.is_dir():
            yield from IGetFiles(thing.path)
        else:
            yield thing.path

# I think it's ok to assume these exist for a sphinx site...

# (.doctrees in build folder by default only for sphinx<1.8)
for folder in (".doctrees", "_sources"):
    d = os.path.join(htmldir,folder)
    try:
        if dry_run:
            print("would remove %s"%d.split(output)[-1])
        else:
            print("removing %s"%d)
            shutil.rmtree(d)
    except:
        pass

for file_ in ("objects.inv",):
    f = os.path.join(htmldir,file_)
    try:
        if dry_run:
            print("would remove %s"%f.split(output)[-1])
        else:
            print("removing %s"%f)
            os.remove(f)
    except:
        pass

for path in IGetFiles(htmldir):
    if os.path.splitext(path)[1].lower() == '.ipynb':
        if dry_run:
            print("would remove %s"%path.split(output)[-1])
        else:
            print("removing %s"%path)
            os.remove(path)
