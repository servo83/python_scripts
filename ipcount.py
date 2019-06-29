import os
import collections
import re

#construct an empty counter
c = collections.Counter()

#open the txt file as f
with open('/home/servo77/Documents/ip.txt') as f:
    line = f.read().splitlines() #eliminate new line characters and splits the strings into a list

#updates the counter for each line in the txt file
c.update(line)
#prints the list of ips and the count
print(c)

#close the file
f.close()