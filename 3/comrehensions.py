


func = lambda x : x*2 # function for testing
func2 =  lambda x : x*3 # for fun


test_list = [1,2,3,4,5] # the list given be the assignment

def multiplier (List:list, func):
    """
    function takes a List and a lambda function. 

    Return:
            a list with the values given by the function
    """
    new_list = [func(x) for x in List] 
    return new_list

print(multiplier(test_list,func)) # testing the multiplier function



def anhanced_multiplier(a_list:list, *funcs):
    """ 
    function takes a List and a lambda function or multiples. 

    Return:
            a list with the values given by the function and if more functions
            are given it will return a list of list with every function
    
    """
    results = []
    for func in funcs:
        anwers = [func(x) for x in a_list]
        results.append(anwers)

    return results             
      
print(anhanced_multiplier(test_list,func,func2)) # testing tha thing



