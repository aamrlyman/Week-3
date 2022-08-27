#Palindrome is a word, phrase, or sequence that reads the same backward as forward i.e. madam. 
# Write code that takes a user input and checks to see if it is a Palindrome and reports the result.
# You must handle spaces.



from ast import Not
from codecs import charmap_build


def palindrome_checker(charfield: str) -> bool:
    reversed_charfield = ''
    if type(charfield) != str:
        charfield = str(charfield)
    for char in range(len(str(charfield)) -1, -1, -1):
        reversed_charfield += charfield[char]

    is_palindrome = f'{charfield} is a palindrome!' if reversed_charfield == charfield else f'{charfield} is not a palindrome :(...'
    print(is_palindrome)  
    return reversed_charfield == charfield 


palindrome_checker('aaaaaa')
palindrome_checker('12344321')
palindrome_checker('madam')
palindrome_checker('xdfgsdhfgsgfh')
palindrome_checker('abc123321cba')


