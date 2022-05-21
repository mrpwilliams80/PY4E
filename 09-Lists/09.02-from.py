# PY4E 09-Lists 09.02-from.py

# Open the file mbox-short.txt and read it line by line. When you find a line 
# that starts with 'From ' like the following line:
# 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# You will parse the From line using split() and print out the second word in 
# the line (i.e. the entire address of the person who sent the message). Then 
# print out a count at the end.
# Output should be:
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# [...]
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word

# start new counter
count = 0

# open file handle
file = open("mbox-short.txt", 'r')

# find, print & count 'From ' lines
for line in file:
    if line.startswith('From '):
        print(line.split()[1])
        count +=1

# print result
print("There were", count, "lines in the file with From as the first word")