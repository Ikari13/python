yourname = input("Please enter your Name")
characterCount = 0
wordCount = 1
for i in yourname:
    characterCount = characterCount+1
    if (i ==''):
        wordCount = wordCount+1
print (wordCount)