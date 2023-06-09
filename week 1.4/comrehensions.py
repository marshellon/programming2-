class List_composition:
    def __init__(self,data:list,*functions):
        self.data = data
        self.functions = functions

    def composition(self):
        results = []
        for func in self.functions:
            results.append([func(x) for x in self.data])
        print(results) # for testing
        return results

# functions
x_2 = lambda x : x *2
x_4= lambda x : x *4

# testing
test = [1,2,3,4,5]
composition = List_composition(test,x_2,x_4).composition() # works



