# Write a function to check if a string is a palindrome.

import re
import unicodedata

input_1 = "madam"
input_2 = "racecar"
input_3 = "hello"

# Special Cases
input_4 = "Madam"
input_5 = "RaceCar"
input_6 = "Python"

input_7 = "A man, a plan, a canal: Panama"
input_8 = "No lemon, no melon"
input_9 = "Was it a car or a cat I saw?"
input_10 = "Not a palindrome!"

input_11 = "àbbà"
input_12 = "ß"
input_13 = "reifier"
input_14 = "été"
input_15 = "mañana"

input_16 = ""
input_17 = " "
input_18 = "a"
input_19 = "aa"
input_20 = "ab"
input_21 = "!!??!!"

input_22 = "a"*1_000_000
input_23 = "a"*500_000 + "b" + "a"*500_000
input_24 = "a"*500_000 + "b" + "c"*500_000

def is_palindrome(word: str) -> bool:
   
    input = unicodedata.normalize("NFC", word.casefold())
    input = "".join([i for i in input[:] if i.isalnum()])

    # using Regular expression
    # reverse = "".join(
    #     [re.match("[a-zA-Z]", i).group() for i in input[::-1]]
    # )
    return input == input[::-1]

def is_palindrome_two_pointer(word: str) -> bool:
    
    word = unicodedata.normalize("NFC", word)
    
    left, right = 0, len(word)-1
    
    while left < right:
        
        if not word[left].isalnum():
            left += 1
            continue
        if not word[right].isalnum():
            continue
        
        if word[left].casefold() != word[right].casefold():
            return False

        left += 1
        right += 1
    return True

def display_result(word: str, result: bool) -> None:
    
    word_len = len(word)
    if word_len > 200:
        word = word[:10] + '...' + word[word_len-10:]
    print(f"\"{word} is a Palindrome ✅" if result else f"\"{word}\" is not a Palindrome ❌")

display_result(input_1, is_palindrome(input_1))
display_result(input_2, is_palindrome(input_1))
display_result(input_3, is_palindrome(input_3))

display_result(input_4, is_palindrome(input_4))
display_result(input_5, is_palindrome(input_5))
display_result(input_6, is_palindrome(input_6))

display_result(input_7, is_palindrome(input_7))
display_result(input_8, is_palindrome(input_8))
display_result(input_9, is_palindrome(input_9))
display_result(input_10, is_palindrome(input_10))

display_result(input_11, is_palindrome(input_11))
display_result(input_12, is_palindrome(input_12))
display_result(input_13, is_palindrome(input_13))
display_result(input_14, is_palindrome(input_14))

display_result(input_15, is_palindrome(input_15))
display_result(input_16, is_palindrome(input_16))
display_result(input_17, is_palindrome(input_17))
display_result(input_18, is_palindrome(input_18))
display_result(input_19, is_palindrome(input_19))
display_result(input_20, is_palindrome(input_20))
display_result(input_21, is_palindrome(input_21))

display_result(input_22, is_palindrome(input_22))
display_result(input_23, is_palindrome(input_23))
display_result(input_24, is_palindrome(input_24))

