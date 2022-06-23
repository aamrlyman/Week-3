# define function
# 1. If the number is less than 10, (while loop) multipy it by itself and save the product in a variable
# 2. Repeat step 1 until the number is more than 1 digit
# 3. convert the number to a string 
# 4. loop through the indivudal characters converting them back to numbers and squaring them and adding them together
# 5. If the sum = 1 return "happy number" 
# 6. If the sum = the starting number return "sad number" 
# 7. If the sum != 1 repeat the loop using the new sum 

def happy_number(num):
    temp = 0
    function_num = num 
    while function_num > -1:
        for char in str(function_num):
            temp += int(char)* int(char)
        if temp == 1:
            return 'Happy Number'
        elif temp == num or temp == 4:
            return 'sad number'
        else:
            function_num = temp
            temp = 0

print(happy_number(36))

        
