def verificar(n):
  t1 = 0
  t2 = 1
  cont = 3 
  while cont <= n:
      t3 = t1 + t2
      if t3 == n:
        return True
      t1 = t2
      t2 = t3
      cont +=1
  return False
  
n = int(input("Digite um número: "))

if n == 1 or n ==2 or n ==3 or n ==5 or verificar(n):
  print("O número pertence a sequência de Fibonacci")
else:
  print("O número não pertence a sequência de Fibonacci")
  
  
