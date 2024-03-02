def factorial(n):
    if(n>1):
        return n*factorial(n-1)
    else: return 1    

# print(factorial(3))

def factorialImp(n):
    prod =1
    while(n>1):
        prod *= n
        n -= 1
    return prod


qntdEnergy= lambda m:(m * pow(300000000, 2))

    
dicX = {"Rafael": [100, 200], "Maria":[50, 50]}
dicY = {"Luiz": [300, 100], "Rubens":[150, 450]}
query = (lambda dic1, dic2: list(dic1.keys()) + list(dic2.keys()))
    


strawberries = [2,1,3,10,5,8]

values = list(map(lambda m: 8*m, strawberries))

payments = list(filter(lambda m: m<=40, values))

print(payments)