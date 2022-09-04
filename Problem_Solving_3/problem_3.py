# 3. Given a list of integers, return a bool that represents whether or not all integers in the list can form a sequence of incrementing integers
#     a. Use case:
#          i. {5, 7, 3, 8, 6} à false (no 4 to complete the sequence)
#          ii. {17, 15, 20, 19, 21, 16, 18} à true

# (1) find the smallest number in the sequence and the next smallest number in the sequence (maybe sort the list smallest to largest)
# (2) 2nd smallest number minus smallest number 
# (3) add the differnce to the 2nd smallest number and see if it equals the 3rd number in the sequence
# (4) If not, return False. If it does test if the 3rd num + the difference = the 4th number and so on until the sequence is proven true or false  

list_1 = [4,2,1,3]
list_2 = [17, 15, 20, 19, 21, 16, 24]
list_3 = [1,3,5,7,9,11]
list_4 = [5,10,15,20,25,30,35]
list_5 = [.5,1,1.5,2]
list_6 = [0,0,0]
list_7 = [2,2,2]
list_8 = [-3, -2, -4, -5]

def is_sequence(list: list[int])-> None:
    list.sort()
    increment = list[1] - list[0]    
    for index in range(len(list)-1):
        if list[index] + increment == list[index + 1] != list[index]:
            is_sequence = (True, 'Yes')
        else:
            is_sequence = (False, 'No')
            return print(f'Is {list} a sequence? {is_sequence[1]}') 
    return print(f'Is {list} a sequence? {is_sequence[1]}. It increments by {increment}s.')   
        


is_sequence(list_1)
is_sequence(list_2)
is_sequence(list_3)
is_sequence(list_4)
is_sequence(list_5)
is_sequence(list_6)
is_sequence(list_8)