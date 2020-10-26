def unique_strings(string_list):
    unique_strings = []
    n_occurences = {}
    
    for x in string_list:
        if x not in n_occurences:
            n_occurences[x] = 1
        else:
            n_occurences[x] += 1
                
    return n_occurences