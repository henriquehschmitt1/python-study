# import sys

def wordCount(fileName):
    allWords = {}
    try:
        openFile = open(fileName, "r")
        text = openFile.read()
        words = text.split()
        for word in words:
            if word in allWords:
                allWords[word] += 1
            else:
                allWords[word] = 1
        sorted_dict = dict(sorted(allWords.items(), key=lambda item: item[1], reverse=True))
        with open("test-output.txt", "w") as f:
            f.writelines(f"{key}: {value}\n" for key, value in sorted_dict.items())
    except FileNotFoundError:
        print("File not found")

wordCount("test.txt")