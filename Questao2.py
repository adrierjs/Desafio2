def verificar(array):
  for i in range(len(array)):
    if array[i] == n:
      return True
  return False
  
  

n = int(input("Digite um número: "))
t1 = 0
t2 = 1
cont = 3 
array = []
while cont <= n:
    t3 = t1 + t2
    array.append(t3)
    t1 = t2
    t2 = t3
    cont +=1

if n == 1 or n ==2:
  print("O número pertence a sequência de Fibonacci")
else:
  retorno = verificar(array)
  if retorno:
    print("O número pertence a sequência de Fibonacci")
  else:
     print("O número não pertence a sequência de Fibonacci")
  
  
