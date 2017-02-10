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
def get_special_paths(dir): # returns a list of the absolute paths of the special files in the given directory
  """"
  cmd = '[s -]' + dir
  print 'about to do this:', cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write('there was an error:' + output)  # syntax for writing to another filehandle~~~~
    sys.exit(1)
  print output
  """
  filenames = os.listdir(dir)
  change_filenames_to_string = '\n'.join(filenames)
  #find the files which matches the special pattern and return them in a new list...
  match_name = re.findall('\w+__+\.\w+', change_filenames_to_string)
  abspath = []
  for name_of_file in match_name:
    path = os.path.join(dir, name_of_file)
    abspath.append(os.path.abspath(path))
  return abspath


def copy_to(todir, special_name_file_paths): # given a list of paths, copies those files into the given directory

# check if the path exists first: if yes, just copy the files to there, if not, create the path then add files to there.
  if not os.path.exists(todir):
    os.mkdir(todir, 0755)
  for each_path in special_name_file_paths:
    frame = os.path.basename(each_path)
    shutil.copy(each_file, os.path.join(todir, frame))




#def zip_to(paths, zippath): # given a list of paths, zip those files up into the given zipfile


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
  tozip = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
    for path in args:
      copy_to(todir, path)

  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # make a new empty list for the paths of these special name files:
  special_name_file_paths = []
  for dir in args:
    special_name_file_paths.extend(get_special_paths(dir)) # add the paths for each file into the list
  if todir:
    copy_to(todir,special_name_file_paths)



if __name__ == "__main__":
  main()
