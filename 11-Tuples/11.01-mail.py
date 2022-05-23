# PY4e 11-Tuples 11.01-mail.py

# Write a program to read through the mbox-short.txt and figure out the 
# distribution by hour of the day for each of the messages. You can pull the 
# hour out from the 'From ' line by finding the time and then splitting the 
# string a second time using a colon.
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour.
# Output should be:
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1

# open file handle
file = open("mbox-short.txt", 'r')
# create new dictionary
counts = dict()

for line in file:
    if line.startswith("From "):

        # Procedural Algorithm to extract hours from line
        words = line.split()
        time = words[5]
        hour = time.split(':')[0]

        # Lambda Equivalent to extract hours from line
        # hour = line.split()[5].split(':')[0]

        # count and record instances for each hour
        counts[hour] = counts.get(hour, 0) + 1

# Procedural Algorithm to create, populate & sort list
lst = list()
for k, v in counts.items():
    temp = (k, v)
    lst.append(temp)
lst.sort();

# Lambda Equivalent to create, populate & sort list
# lst = sorted([ (k, v) for k, v in counts.items() ])

# print list
for k, v in lst:
    print(k, ' ', v)
