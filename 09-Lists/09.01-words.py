# PY4E 09-Lists 09.01-words.py

# Open the file romeo.txt and read it line by line. For each line, split the 
# line into a list of words using the split() method. The program should build a 
# list of words. For each word on each line check to see if the word is already 
# in the list and if not append it to the list. When the program completes, sort 
# and print the resulting words in alphabetical order.
# Output should be:
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 
# 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 
# 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

# new empty list
uniqueWords = list()

# open file handle
file = open("romeo.txt", 'r')
# iterate lines in file
for line in file:
    # put words from line in list
    wordsInLine = line.split()
    # iterate words in list
    for word in wordsInLine:
        # add new words to final list
        if word not in uniqueWords:
            uniqueWords.append(word)
# sort final list
uniqueWords.sort()
# print final list
print(uniqueWords)