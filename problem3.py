def swap_case(s):
    word = ""
    for c in s:
        if c.isupper():
            word += c.lower()
        else:          
            word += c.upper() 
        
        
    return word