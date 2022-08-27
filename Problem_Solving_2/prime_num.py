# make a range loop that loops through 1-100
# declare an is_prime boolean
# declaure a prime num list variable 
# make a second loop that divivides the first loop number by each element of the prime num list
# with each iteration: if the modulus value = 0 break the loop and is_prime = false
# If statement: if is_prime == true append num to the list
# append 1 to list because having it in the list will mess up calcuations 
# return the list

def prime_nums():
    is_prime = False
    prime_num_list = [2]
    for num in range(2, 101):
        for element in prime_num_list:
                if num % element == 0:
                    is_prime = False
                    break
                else: 
                    is_prime = True 
        if is_prime == True:
            prime_num_list.append(num)
    prime_num_list.insert(0,1)
    return prime_num_list






