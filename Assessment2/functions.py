
"""
Divide function

Input: 
    original (string) - the string to divide
    w (number) - Size (number of words) of each batch
Returns: 
    (list of strings) - list containing the strings of batches
"""
from cgitb import text


def Divide(originalStr,w):

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
Sum function

Input:
    Occurence_arr (numbers list) - the list of the numbers to sum
Output:
    (Number) : Sum
"""
def Sum(occurence_list):
    return sum(occurence_list)

"""
Clean function

Input: 
    original (string) - the string to clean
    pattern (string) - the searched string
    m (number) - threshold
    totalOccurence (number) -  Total Occurence
Returns: 
    modifiedStr (string) - the cleaned string
"""


def Clean(originalStr,pattern,m,totalOccurence):

    if ( totalOccurence > m ):
        modifiedStr= originalStr.replace(pattern,"ml&23QS4",m)
        modifiedStr= modifiedStr.replace(pattern,"")
        modifiedStr= modifiedStr.replace("ml&23QS4",pattern)
        modifiedStr = " ".join(modifiedStr.split())
        
    return modifiedStr