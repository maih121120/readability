def main():
    getText = input("Text: ")
    charactersNum = chara(getText)
    sentencesNum = sentence(getText)
    wordsNum = word(getText)

    charactersAve = charactersNum / wordsNum
    sentencesAve = sentencesNum / wordsNum

    S = sentencesAve * 100
    L = charactersAve * 100
   
    ind = 0.0588 * L - 0.296 * S - 15.8
    index = round(float(ind))

# grade
    if index >= 16:
        print("Grade 16+")

    elif index < 1:
        print("Before Grade 1")

    else:
        print(f"Grade {index}")

# 語数


def word(text):
    count = 1
    for i in range(len(text)):
        if text[i] == " ":
            count += 1
    return count

# 字数


def chara(text):
    count = 0
    for i in range(len(text)):
        if (text[i].isalpha()):
            count += 1

    return count

# 文数


def sentence(text):
    count = 0
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            count += 1
    return count
    

main()
