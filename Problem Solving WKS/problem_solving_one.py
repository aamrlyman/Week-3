# def reverse_string(string):
#     reversed_string = ''
#     for index in range(len(string)-1, -1, -1):
#         reversed_string += string[index]
#     return reversed_string

# print(reverse_string('Hello'))


# def capitalize_words_in_string(string):
#     if "  " in string:
#             print('invalid entry string contains 2 consecutive spaces')
#     new_str = ''
#     temp = 0
#     for index in range(len(string)):
#         if index == 0:
#             new_str += string[index].upper()
#         elif index == temp:
#             continue
#         elif string[index] == " ":
#             new_str += string[index] + string[index + 1].upper()
#             temp = index + 1
#         else:
#             new_str += string[index]
        
#     return new_str

# print(capitalize_words_in_string('hello'))
# print(capitalize_words_in_string('hello goodbye'))
# print(capitalize_words_in_string('hello goodbye thanks'))
# print(capitalize_words_in_string('hello goodbye  thanks'))

# def compress_string(string):
#     temp1 = ''
#     temp2= ''
#     new_string = ''
#     counter = 0
#     for char in string:
#         #counter += 1
#         if temp1 == char:
#             continue
#         temp1 = char

#         for index in range(len(string)):
#             if string[index] == temp2:
#                 continue
#             if string[index] == temp1 and index == (len(string) - 1):
#                 counter += 1
#                 new_string+= str(counter) + temp1
#                 return new_string
#             elif string[index] == temp1:
#                 counter += 1
#             elif string[index] != temp1 or string[index] != temp2:
#                 new_string += str(counter) + temp1
#                 counter = 0
#                 temp2 = temp1
#                 break        
    
#     return new_string




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