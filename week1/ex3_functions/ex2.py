
import sys


def is_anagram(word_1: str, word_2: str) -> bool:
    if set(word_1) == set(word_2):
        return True
    return False


def main():
    try:
        first_word = str(input("Please enter the first word to the Anagram Checker: "))
        second_word = str(input("Please enter the second word to the Anagram Checker: "))

    except Exception:
        sys.exit("Oops, please try again - only enter a single word!")
    
    if is_anagram(first_word, second_word):
        print("These are anagrams")
    else:
        print("These are not anagrams")



if __name__ =="__main__":
    main()
