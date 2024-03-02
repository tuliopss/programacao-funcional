from functools import reduce


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

# =============================
qntdEnergy= lambda m:(m * pow(300000000, 2))

# =============================
dicX = {"Rafael": [100, 200], "Maria":[50, 50]}
dicY = {"Luiz": [300, 100], "Rubens":[150, 450]}
query = (lambda dic1, dic2: list(dic1.keys()) + list(dic2.keys()))
    
# =============================
strawberries = [2,1,3,10,5,8]

values = list(map(lambda m: 8*m, strawberries))
payments = list(filter(lambda m: m<=40, values))
paymentsListComp = [x for x in values if x<=40]
total = reduce(lambda x, y: x + y, payments)

# =============================

emprestimos = []
with open(file='./programacaoFuncional/credito.csv', mode='r', encoding='utf8') as fp:
  fp.readline() # cabeçalho
  linha = fp.readline()
  while linha:
    linha_emprestimo = {}
    linha_elementos = linha.strip().split(sep=',')
    linha_emprestimo['id_vendedor'] = linha_elementos[0]
    linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
    linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
    linha_emprestimo['data'] = linha_elementos[3]
    emprestimos.append(linha_emprestimo)
    linha = fp.readline()

#Aplique a função map na lista de emprestimos para extrair os valores da chave valor_emprestimos na lista valor_emprestimos_lista. Faça também a conversão de str para float.
list_values_loan = list(map(lambda emp: float(emp["valor_emprestimos"]), emprestimos))
list_values_positive = list(filter(lambda v: v>=0, list_values_loan))
sum_values_positive = reduce(lambda x, y: x+y, list_values_positive)

media_sum_values_positive = reduce(lambda x, y: sum_values_positive/len(list_values_positive), list_values_positive)
print(media_sum_values_positive)
