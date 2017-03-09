#!/usr/bin/env python

import os
rootDir = "scss"
fileSet = set()

for dir_, _, files in os.walk(rootDir):
    for fileName in files:
        relDir = os.path.relpath(dir_, rootDir)
        if relDir == '.':
            relDir = 'scss'
        else:
            relDir = 'scss/' + relDir
        relFile = os.path.join(relDir, fileName)
        print "'" + relFile + "',"
        fileSet.add(relFile)
