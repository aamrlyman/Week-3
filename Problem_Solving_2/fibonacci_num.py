# declare a list []
# create user input for a num
# append input num twice
# use a for num in range loop (based on the desired length of the pattern)
# start the loop at 2. With each iteration, add list[index] + list[index -1].
# Save the sum to a variable. 
# Append the variable to the list

def fibonacci_nums(num):
    fibonaccis_list = []
    fibonaccis_list.append(num)
    fibonaccis_list.append(num)
    fibonaccis_list.append(num + num)

    for number in range(2, 9):
        next_fib_num = fibonaccis_list[number] + fibonaccis_list[number -1]
        fibonaccis_list.append(next_fib_num)
    return fibonaccis_list

print(fibonacci_nums(int(input('enter a number: '))))