def replace_words():
    str = "Hi guys, I am mbio peter and i am a python developer"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_words()