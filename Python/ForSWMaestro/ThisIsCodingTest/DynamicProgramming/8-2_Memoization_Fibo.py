import time

d = [0] * 200

def memoization_fibonacci(i):
    if i == 0 or i == 1:
        return 1
    
    if d[i] != 0:
        return d[i]
    
    d[i] = memoization_fibonacci(i-2) + memoization_fibonacci(i-1)
    return d[i]

num = int(input("Enter a number : "))

start_time = time.perf_counter()
result = memoization_fibonacci(num)
end_time = time.perf_counter()

execution_time = end_time - start_time

print(f"Execution time : {execution_time:.6f} seconds")
print(f"Fibonacci result : {result}")