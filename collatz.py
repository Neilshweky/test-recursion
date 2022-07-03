import time

# This map stores a mapping from starting points to chain lengths.
result_map = { 1: 1 }

# Calculates the number of operations it takes to get to 1.
#
# @param [ Integer ] n The starting number.
#
# @return [ Integer ] The length of the chain.
def collatz(n):
  if n in result_map:
    return result_map[n]

  res = n // 2 if n % 2 == 0 else 3 * n + 1
  chain_length = 1 + collatz(res)
  result_map[n] = chain_length
  return chain_length


max = 0
max_i = 0
start = time.time()
for i in range(1, 1_000_000):
  if i not in result_map:
    result = collatz(i)
    if result > max:
      max = result
      max_i = i
end = time.time()
print("The maximum chain is " + str(max_i) + " and it took " + str(max) + " steps.")
print("It took " + str(end - start) + " seconds.")

