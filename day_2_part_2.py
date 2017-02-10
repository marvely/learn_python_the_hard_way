#bash????? what is bash?
import os #operation system
"""""
dir()
help(os.listdir())
#directories?
"""""
#get the code from hello.py:
import sys
import commands

# get the current directory stuffs:
def List(dir):
    cmd = '[s -]' + dir
    print 'about to do this:', cmd
    return
    (status, output) = commands.getstatusoutput(cmd)
    # to see if this thing failed
    if status:
        sys.stderr.write('there was an error:' + output) #syntax for writing to another filehandle~~~~
        sys.exit(1)
    print output

"""""
    filenames = os.listdir(dir)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print path
        print os.path.abspath(path)

""""""
# check if a dir is existing:
os.path.exists('path')

import shutil   # this does the file copying for you...
shutil.copy(source, destiny) # input the path...

"""""
# launch an external process and waiting for it to finish...

"""""
import commands

getstatusoutput(cmd) # return a tuple of length 2 (status, output)

"""""
# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  List(sys.argv[1])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
