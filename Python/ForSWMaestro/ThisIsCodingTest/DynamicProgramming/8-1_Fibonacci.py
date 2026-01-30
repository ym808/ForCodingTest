import time

def fibonacci(i):
    if i == 1 or i == 2:
        return 1
    return fibonacci(i-2) + fibonacci(i-1)
num = int(input("Enter a number : "))
start_time = time.perf_counter()
result = fibonacci(num)
end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Execution time : {execution_time:.6f} seconds.")
print(f"Fibonacci result : {result}")