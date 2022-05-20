# PY4E 08-Files 08.01-files.py

# Write a program that prompts for a file name, then opens that file and reads 
# through the file, looking for lines of the form:
# `X-DSPAM-Confidence:    0.8475`
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# The output should be 'Average spam confidence: 0.7507185185185187'

# open file handle
file = open("mbox-short.txt", 'r')

# set counters to zero
numberOfSpamLines = 0
totalSpamConfidence = 0.0

for line in file:
    if line.startswith("X-DSPAM-Confidence:"):

        # increment line counter
        numberOfSpamLines += 1

        # extract float from string
        '''
        v0.1.1 & v0.1.2
        '''
        # spcPos = line.find(' ')
        '''
        v0.1.1
        '''
        # line = line[spcPos: ]
        # line = line.strip()
        # totalConfidence += float(line)
        '''
        v0.1.2
        '''
        #totalSpamConfidence += float(line[spcPos: ].strip())
        '''
        v0.1.3
        '''
        totalSpamConfidence += float(line[line.find(' '): ]. strip())



print("Average spam confidence: ", totalSpamConfidence/numberOfSpamLines)

# NOTE: strip is a method and needs ()

'''
All of the above version work as intended. The difference is one of code 
consolidation and readability.
While v0.1.3 seems more elegant - summarising the whole process of obtaining a 
float from the iterated string in just one line; it is probably harder for a 
human to parse & more error prone in the event future changes are needed.
'Best Practice' is probably just one instruction per line of code (see v0.1.1)
'''