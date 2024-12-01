# Function to generate Fibonacci series up to 50 using lambda
from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
								range(n-2), [0, 1])

print(fib(10))
  # Fibonacci limit is 50


