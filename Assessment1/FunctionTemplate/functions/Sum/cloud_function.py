def cloud_function(json_input):
    occurence_list = json_input["OccurenceArr"]
    
    # Processing
    result = sum(occurence_list)
    # return the result
    res = {
        "totalOccurence": result
    }
    return res
