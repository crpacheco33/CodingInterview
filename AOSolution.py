def AOSolution(array):

    if array == [0]:
        print("empty array")

    else:
        counter = [1] #assumption: not empty array. Initial Condition: 1
        max_value_list = []
        for i in range(1, len(array)):
                j=i
                if array[j] == array[j-1] + 1: 
                    counter.append(1) # 1- Boundary Condition(BC) satisfied- in case more than one Boundary Condition: Partial Boundary Condition
                else:
                    counter = [0] # 0 - condition not satisfied - limit reached.
                max_value_list.append(len(counter))  #max_value_list stores outer Boundary Condition value or all Partial Boundary Condition values(in case they exist)
        return print(max(max_value_list))
        

#Test
#array = [0]
            
array = [-20,-19,-18,-14,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,13,14,15]
AOSolution(array)