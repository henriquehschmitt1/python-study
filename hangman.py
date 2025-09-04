#If letter is correct, show like: a _ _ _ _, if not correct, lives -1
# use word = list(apple.lower()) easier to check

def hangman():
    lives = 10
    word = "apple"
    wordCompletion = "_" * len(word)
    guessed = False
    wordList = list(word.lower())
    wordCompletionList = list(wordCompletion)
    guessedLetters = []
    input("Welcome to Hangman! Press enter to start playing!")
    print(wordCompletion + "The word has " + str(len(word)) + " letters")

    while not guessed and lives > 0:
        guessWord = input("Enter a letter! ").lower()
        if guessWord in guessedLetters:
            print("You already guesses that letter!")
            continue
        elif guessWord not in wordList:
            lives -= 1
            print("Wrong letter, you lost a life. You now have " + str(lives) + " lives left")
            guessedLetters.append(guessWord)
        else:
            guessedLetters.append(guessWord)
            print("You're right!")
            for i in range(len(wordList)):
                if wordList[i] == guessWord:
                    wordCompletionList[i] = guessWord
            print((wordCompletionList))
            if "_" not in wordCompletionList:
                guessed = True
    
    if guessed:
        print("You won! You had " + str(lives) + " lives left")
        print("The word was " + word)
    else:
        print("You lost! The word was " + word)

hangman()