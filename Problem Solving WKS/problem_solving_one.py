# def reverse_string(string):
#     reversed_string = ''
#     for index in range(len(string)-1, -1, -1):
#         reversed_string += string[index]
#     return reversed_string

# print(reverse_string('Hello'))


def capitalize_words_in_string(string):
    if "  " in string:
            print('invalid entry string contains 2 consecutive spaces')
    new_str = ''
    temp = 0
    for index in range(len(string)):
        if index == 0:
            new_str += string[index].upper()
        elif index == temp:
            continue
        elif string[index] == " ":
            new_str += string[index] + string[index + 1].upper()
            temp = index + 1
        else:
            new_str += string[index]
        
    return new_str

print(capitalize_words_in_string('hello'))
print(capitalize_words_in_string('hello goodbye'))
print(capitalize_words_in_string('hello goodbye thanks'))
print(capitalize_words_in_string('hello goodbye  thanks'))

