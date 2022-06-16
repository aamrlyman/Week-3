def reverse_string(string):
    reversed_string = ''
    for index in range(len(string)-1, -1, -1):
        reversed_string += string[index]
    return reversed_string

print(reverse_string('Hello'))


