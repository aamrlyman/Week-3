def reverse_string(string):
    reversed_string = ''
    for index in range(len(string)-1, -1, -1):
        reversed_string += string[index]
    return reversed_string

print(reverse_string('Hello'))


def capitalize_words_in_string(string):
    if "  " in string:
            print('invalid entry string contains 2 consecutive spaces')
    new_str = ''
    temp = 0
    for index in range(len(string)):
        if index == 0:
            new_str += string[index].upper()
        elif string[index -1] == " ":
            new_str += string[index].upper()
        else:
            new_str += string[index]
        
    return new_str

print(capitalize_words_in_string('hello'))
print(capitalize_words_in_string('hello goodbye'))
print(capitalize_words_in_string('hello goodbye thanks'))
print(capitalize_words_in_string('hello goodbye  thanks'))


def compress_string(string):
    temp = ''
    new_string = ''
    counter = 0

    for index in range(len(string)):
        if index == 0:
            counter += 1 
            temp = string[index]
        elif index == (len(string)-1) and temp == string[index]:
            counter += 1 
            new_string += str(counter) + temp 
            return new_string 
        elif index == (len(string)-1) and temp != string[index]:
            counter = 0
            counter +=1
            new_string += str(counter) + temp 
            return new_string 
        elif temp == string[index]:
            counter += 1
        elif temp != string[index]:
            new_string += str(counter) + temp
            counter = 0
            temp = string[index] 
            counter += 1
    return new_string


print(compress_string('aaa'))
print(compress_string('aaabbaa'))
print(compress_string('aaabbcc'))
print(compress_string("aaabbbbbccccaacccbbbaaabbbaaa"), "3a5b4c2a3c3b3a3b3a")

def is_palindrome(string):
    reversed_string = ''
    for index in range(len(string) -1, -1, -1):
        reversed_string += string[index]
    
    return string == reversed_string

print(is_palindrome('madam'))


original_string = 'aaabbbbbccccaacccbbbaaabbbaaa'

def word_compressor(string):
    final_result = ''
    letter_counter = 1
    for index in range(len(string)):
        if index == len(string) - 1:
            final_result += str(letter_counter) + string[index]
        elif string[index] == string[index + 1]:
            letter_counter += 1
        elif string[index] != string[index + 1]:
            final_result += str(letter_counter) + string[index]
            letter_counter = 1
    return final_result

print(word_compressor(original_string)) 
         
