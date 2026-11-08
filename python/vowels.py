def main():
    # ask for the word with input, save it in a variable
    word = input("Please enter a word: ")
    # call count_vowels with that variable, save the result
    count = count_vowels(word)
    # print the result
    print ("The number of vowels in the input string is:", count)

def count_vowels(word):
    # your vowels list
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # your counter starting at 0
    vowel_count = 0
    # your for loop with the if
    for char in word:
        if char in vowels:
            total += 1
    # return the counter
    return total


main()