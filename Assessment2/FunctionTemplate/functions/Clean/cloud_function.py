def cloud_function(json_input):
    originalStr = json_input["originalStr"]
    pattern = json_input["pattern"]
    m = json_input["m"]
    totalOccurence = json_input["totalOccurence"]
    
    
    # Processing
    if ( totalOccurence > m ):
        modifiedStr= originalStr.replace(pattern,"ml&23QS4",m)
        modifiedStr= modifiedStr.replace(pattern,"")
        modifiedStr= modifiedStr.replace("ml&23QS4",pattern)
        modifiedStr = " ".join(modifiedStr.split())
        
    result = modifiedStr    
    # return the result
    res = {
        "modifiedStr": result
    }
    return res
