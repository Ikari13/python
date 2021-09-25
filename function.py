def wordCount():
    filename = input("filename:")
    numberOfWords = 0
    file = open(filename, 'r+')
    for line in file: 
        words = line.split()
        numberOfWords = numberOfWords+len(words)
    print("numberOfWords: ")
    print(numberOfWords)
wordCount()