def cloud_function(json_input):
    originalStr = json_input["originalStr"]
    w = json_input["w"]
    
    # Processing
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
    
    # return the result
    res = {
        "stringArray": sum_list
    }
    return res
