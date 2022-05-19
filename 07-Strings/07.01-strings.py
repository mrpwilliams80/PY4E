# PY4E 07-Strings 07.01-strings.py

# Write code using find() and string slicing (see section 6.10) to extract the 
# number at the end of the line below. Convert the extracted value to a floating 
# point number and print it out.
# The output should be '0.8475'

# line of text
text = "X-DSPAM-Confidence:    0.8475"
# find first space character
spcPos = text.find(' ')
# slice from first space to end
text = text[spcPos: ]
# strip whitespace
text = text.strip()
# print final result
print(text)

# NOTE: str methods create new strings and must be assigned.