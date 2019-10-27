#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  special_paths = [] 
  for filename in os.listdir(dir):
    match = re.search(r'\w*__\w+__\w*',filename)
    if match:
      special_paths.append(os.path.abspath(os.path.join(dir,filename)))
  return special_paths

def copy_to(paths,dir):
  
  # check if target dir exits. if not create it.
  if not os.path.exists(dir):
    os.mkdir(dir)

  for path in paths:
    shutil.copy(path, dir)

def zip_paths(paths,zipfile):
  
  cmd = 'zip -j ' + zipfile + ' '
  for path in paths:
    cmd += path + ' '

  (status, output) = commands.getstatusoutput(cmd)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for dir in args:
    special_paths = get_special_paths(dir)

    if todir:
      copy_to(special_paths,todir)
      sys.exit(0)

    if tozip:
      zip_paths(special_paths,tozip)
      sys.exit(0)
  
    for path in special_paths:
      print path
  
if __name__ == "__main__":
  main()
