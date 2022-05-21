# PY4E 10-Dictionaries 10.01-mail.py

# Write a program to read through the mbox-short.txt and figure out who has sent 
# the greatest number of mail messages. The program looks for 'From ' lines and 
# takes the second word of those lines as the person who sent the mail. The 
# program creates a Python dictionary that maps the sender's mail address to a 
# count of the number of times they appear in the file. After the dictionary is 
# produced, the program reads through the dictionary using a maximum loop to 
# find the most prolific committer.
# The output should be 'cwen@iupui.edu 5'

# create dictionary
addressFreq = dict()

# read file handle
file = open("mbox-short.txt", 'r')

for line in file:
    if line.startswith("From "):
        # get email in "From " line
        word = line.split()[1]
        # add/increment dictionary
        addressFreq[word] = addressFreq.get(word, 0) + 1

# find & print most prolific committer
mostProlific = max(addressFreq, key=addressFreq.get)
print(mostProlific, addressFreq[mostProlific])