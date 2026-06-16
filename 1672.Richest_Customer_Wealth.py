def richestcustomerwealth(num):
    max_wealth = 0
    
    for i in num:
        result = 0
        for j in i:
            result += j
        
        if result > max_wealth:
            max_wealth = result
        
    return max_wealth
        
        
print(richestcustomerwealth([[1,5],[7,3],[3,5]]))