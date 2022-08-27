
# Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# a. Use Case:
# i. Given numbers in an array: [5, 17, 77, 50]
# ii. Target: 55

# (1) create a function that takes in an arroy and a target value
# (2) Create a loop that performs calcuation with each index in the array
# (3) create a loop inside of the first loop that takes in the index of the first loop and adds it to each index of the array and compares it to the target value
# (4) if one of the index combinations produces the target value return those indexes


list_1 = [1,2,3,4,5,6,7]
list_2 = [1,1,1,1,1,1,1]
list_3 = [5,5,3,2,4,5,6,3,2,6]
list_4 = [5, 17, 77, 50]
list_5 = ['d', 'dd']

def sum_of_indicies(list: list[int], target_value: int) -> tuple:
    for num in list:
        for index in list:
            if index == num:
                continue
            elif index + num == target_value:
                answer = (num, index)
                print(f'{num} + {index} = {target_value}')
                return answer
    print("No index pair added to target value.")


sum_of_indicies(list_1, 10)
sum_of_indicies(list_2, 10)
sum_of_indicies(list_3, 10)
sum_of_indicies(list_4, 55)
