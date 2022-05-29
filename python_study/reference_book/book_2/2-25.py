def fibonacci(n):
  fib = [1, 1]
  for i in range(2, n):
    fib.append(fib[i - 2] + fib[i - 1])
  print(fib)  
  return fib[n - 1]

print(fibonacci(8))