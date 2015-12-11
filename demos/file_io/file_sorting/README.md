# File Sorting

The [BFS_IP_Sort.py](BFS_IP_Sort.py) demo shows how to open a file for read, sort the contents of the file then write the sorted data back out to the file.  

The file used is [BFS_SpamIPs.txt](BFS_SpamIPs.txt) which has a single IP address on each line.

File i/o commands used in this program:

## open()

`open()` takes 2 parameters: the name of the file and the read or write mode.
Some important modes are:

* 'w' : open the file for writing (will delete any contents first)
* 'r' : open the file for reading
* 'a' : open the file for writing, but will append new data to the old

`open()` returns a 'file handle' which is why I shorten it to `fh` in the
examples. The file handle is the bit that lets us read or write.

## write()

`write()` takes one parameter: the data to write. It can be anything. If you
want to write strings on separate lines you'll need to add the newline character
`\n` or all the lines will be joined together.

## readlines()

`readlines()` reads the whole file into a list, with each line as a separate
element in a list.

## close()

`close()` closes the file handle, which is good practice but often not
necessary; as Python will close all open files when the program ends.
