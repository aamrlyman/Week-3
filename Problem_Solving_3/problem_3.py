# 3. Given a list of integers, return a bool that represents whether or not all integers in the list can form a sequence of incrementing integers
#     a. Use case:
#          i. {5, 7, 3, 8, 6} à false (no 4 to complete the sequence)
#          ii. {17, 15, 20, 19, 21, 16, 18} à true

# (1) find the smallest number in the sequence and the next smallest number in the sequence (maybe sort the list smallest to largest)
# (2) 2nd smallest number - smallest number 
# (3) add the differnce to the 2nd smallest number and see if it equals the 3rd number in the sequence
# (4) If not, return False. If it does test if the 3rd num + the difference = the 4th number and so on until the sequence is proven true or false  