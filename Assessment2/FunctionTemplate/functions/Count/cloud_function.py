def cloud_function(json_input):
    textBatch = json_input["textBatch"]
    pattern = json_input["pattern"]
    
    # Processing
    result = textBatch.count(pattern)
    # return the result
    res = {
        "Occurence": result
    }
    return res
