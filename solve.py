def brute_force(M , pizzas):
    """
    Input M : amount of slices wanted
    pizzas : vector containing elements si where si is the amount of slices 
    in pizza i
    
    Returns a 0 - 1 vector containing the
    final solution's choice of pizzas.
    """
    return solveR( M , pizzas , len(pizzas))

def solveR(M , pizzas, n):
    # Base Case 
    if n == 0 or M == 0 : 
        return []
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (pizzas[n-1] > M): 
        return solveR(M , pizzas , n-1) + [0]
  
    # return the maximum of two cases: 
    else: 
        sol1 = solveR(M - pizzas[n-1] , pizzas , n-1) + [1]
        sol2 = solveR(M, pizzas , n-1) + [0]
        
        slices1 = sum([x * y for x , y in zip(sol1 , pizzas)])
        slices2 = sum([x * y for x , y in zip(sol2 , pizzas)])
        if(slices1 > slices2):
            return sol1
        else:
            return sol2
