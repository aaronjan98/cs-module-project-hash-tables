ignored_char = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
word_counter = {}

def word_count(s):
    # turn string to all lower case
    lower_s = s.lower()
    # splits the input string into an array of words
    arr_of_words = lower_s.split()

    # loop through the array of words and formats everything correctly
    # and have a new arr of the correctly formatted words

    for word in arr_of_words:
        # loop through each letter of each word
        for letter in range(len(word)):
            # print(i[letter])
            # if a letter in the word is a special char, delete it
            if word[letter] in ignored_char:
                # delete special character
                # print('delete:', word[letter])
                new_word = word.replace(word[letter], '')
                print('new_word:', new_word)

        # after looping through each letter in a word check if it exists in word_counter
        value = arr_of_words.count(i)
        word_counter.update({i: value})

    print('after:', arr_of_words)
    return word_counter


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))