def distance_from_zero(p):    #defining the function
    if type (p) == int or type (p) == float:
        return abs(p)         # returning absolute value of the arguement
        
    else:
        return "Nope"
        
distance_from_zero (-10)  # calling the function
