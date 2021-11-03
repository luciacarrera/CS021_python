
sentence = ""
while "quit" not in sentence:
    sentence = input("Please type a sentence. When you are done entering sentences, enter a sentence containing the word quit: ")
    sentence = sentence.lower()
    words = sentence.split()
    myChars = 0
    for word in words:
        myChars += len(word)

    cnt = len(words)
    avg = myChars / cnt
    print(f"That sentence contains {cnt} words with an average word length of {avg:.1f}")
