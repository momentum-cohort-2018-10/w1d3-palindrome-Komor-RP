import re
import math

phrase = input("Input a phrase: ")

def sanitize_text(phrase):

    only_letters = re.compile('[a-zA-Z]')
    all_low = phrase.lower()
    no_puntuation = re.findall(only_letters, all_low)
    
    return no_puntuation




def palindromeIterative(phrase):

    if (isinstance(phrase, str)):
        print("sanitizes phrase of punctuation and makes all lowercase once")
        phrase = sanitize_text(phrase)
        print(phrase)

    for i in range(len(phrase) // 2 ):
        print("checks if the two ends match and returns False if they don't")
        if (phrase[i] != phrase[len(phrase) - i - 1]):
            print("Elements don't match")
            print("is not a palindrome")
            return False
    
    print("all elements passed check")
    print("is a palindrome")
    return True
    

def palindromeRecursive(phrase):
    
    if (isinstance(phrase, str)):
        print("sanitizes phrase of punctuation and makes all lowercase once")
        phrase = sanitize_text(phrase)
        print(phrase)

    #base case
    if (len(phrase) < 2):
        print("0 or 1 elements left in phrase (so true)")
        print("is a palindrome")
        return True
    
    while (len(phrase) > 1):
        print("Checks if ends match and removes them if they do")

        if (phrase[0] == phrase[len(phrase)-1]):
            end = len(phrase) - 1
            phrase.pop(end)
            phrase.pop(0)
            print("remaining letters: ")
            print(phrase)
            palindromeRecursive(phrase)
            
        else:
            print("returns false if two items don't match")
            print("is not a palindrome")
            return False


palindromeRecursive(phrase)
    