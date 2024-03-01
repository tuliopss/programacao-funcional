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


qntdEnergia = lambda m:(m * pow(300000000, 2))

dicX = {"Rafael": [100, 200], "Maria":[50, 50]}
dicY = {"Luiz": [300, 100], "Rubens":[150, 450]}

consulta = (lambda dic1, dic2: list(dic1.keys()) + list(dic2.keys()))

print(consulta(dicX, dicY))