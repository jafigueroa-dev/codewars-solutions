def fib(n):
  a, b = 0, 1
  for i in range(abs(n)):
      a, b = b, a+b
  
  if n < 0 and n % 2 == 0: a *= -1
  return a