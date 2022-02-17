
"""
Divide function

Input: 
    original (string) - the string to divide
Returns: 
    (list of strings) - list containing the strings of batches
"""
from cgitb import text


def divide(originalStr,w):

    list1 = originalStr.split()

    sum_list = []
    list = []
    i = 0
    for item1 in list1:
            i = i + 1 
            if i%w == 0 :
                list.append(item1)
                sum_list.append(" ".join(list))
                list.clear()
            else:
                 list.append(item1)

    if list:
        sum_list.append(" ".join(list))
    

    return sum_list

"""
Count function

Input:
    textBatch (string) - the batch
    pattern (string) - the searched string
Output:
    (int) - Occurence
"""
def Count(textBatch, pattern):
    
    result = textBatch.count(pattern)

    return result

"""
Total function

Input:
    Occurence_arr (numbers list) - the list of the numbers to sum
Output:
    (Number) : Sum
"""
def Sum(occurence_list):
    return sum(occurence_list)

