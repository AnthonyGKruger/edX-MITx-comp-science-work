def findAll(wordList, lStr):
    """assumes: wordList is a list of words in lowercase.
                lStr is a str of lowercase letters.
                No letter occurs in lStr more than once
       returns: a list of all the words in wordList that contain
                each of the letters in lStr exactly once and no
              letters not in lStr."""

    newList = []
    for word in wordList:
        list_lStr = list(lStr)
        marker = True
        for letter in word:
            if letter in list_lStr:
                list_lStr.remove(letter)
            else:
                marker = False
                break
        if marker == True:
            newList.append(word)
    print(newList)


findAll(['hello', 'goodbye', 'safe'], 'yfaeswzxolleh')


