def common_characters(first_word, second_word):
    
    input_set = list(set(first_word.lower()) & set(second_word.lower()))

    print("common letter(s) are:")

    for common_letters in input_set:
        print(common_letters)

common_characters("Hezekiel", "Modjela")