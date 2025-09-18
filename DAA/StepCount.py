def sum_with_steps(A):
    n = len(A)
    step = 0

    step += 1
    
    total = 0
    step += 1  


    for i in range(n):
        step += 1  
        
        total = total + A[i]
        step += 2  

    
    step += 1  

   
    step += 1  

    return total, step



if __name__ == "__main__":
    A = [5, 2, 9, 1, 7]
    s, steps = sum_with_steps(A)
    print("Sum:", s)
    print("Step count:", steps)
