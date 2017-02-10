#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  file = open(filename, 'r')
  html_to_string = file.read() # read the whole file as a single string
  file.close()

  name_list = []

  match_year = re.search('Popularity\sin\s(\d\d\d\d)', html_to_string)  # got the year out of it~
  if not match_year:
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1) # what does 1 mean???
  year = match_year.group(1)
  name_list.append(year) # first put the year in the list... then...

  # find the year first, then find the rank, and then find the name... well kind a tricky to find the rank for girl...

  tuples_name_rank_pairs = re.findall( '<td?>(\d+)</td?><td?>(\w+)</td?><td?>(\w+)</td?>', html_to_string) # put the boy and girl name together in one list of tuples..
  # according to the html file, the rank is already sorted... so the following code works without have to sort again...

  name_rank_dict = {} # create an empty dictionary to put the new tuples in...
  for tuple in tuples_name_rank_pairs:
    (rank, boyname, girlname) = tuple # unpack 1 tuple into 3 parts...
    if boyname not in name_rank_dict:
      name_rank_dict[boyname] = rank
    else:
      name_rank_dict[girlname] = rank

  sorted_names = sorted(name_rank_dict.keys()) # sometimes indentation causes problems!!!!! gua

  for name in sorted_names:
    name_list.append(name+' '+ name_rank_dict[name])

  return name_list

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:] ### get the commends input into a list? ok...

  if not args:
    print 'usage: [--summaryfile] file [file ...]' # --summaryfile baby*.html runs on all baby files...
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  # do the summary file function here
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # do the normal file function here
  for filename in args:
    name_rank_list = extract_names(filename) # get the result from our function above.

    # make the result plan text file:

    text_name_rank = '\n'.join(name_rank_list) # what is the join function do? i guess it puts each pair in a new line...

    if summary:
      # write a summary file
      output_summary_file = open(filename+'.summary', 'w')
      output_summary_file.write(text_name_rank + '\n') # why do we need a '\n' in the end???????????
      output_summary_file.close()
    else:
      print text_name_rank


  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  
if __name__ == '__main__':
  main()
