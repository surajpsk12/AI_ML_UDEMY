'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario:
Factorial Calculation
Factorial calculations, especially for large numbers, involve significant computational work. Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance.

'''

import multiprocessing 
import time 
import math 
import sys

sys.set_int_max_str_digits(1000000)  # Increase the maximum number of digits for integer string conversion


#fun  to calculate factorial of a number
def calculate_factorial(n):
    print(f"Calculating factorial of {n}...")
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result


if __name__ == "__main__":
    numbers = [1000, 2000, 30000]  # Large numbers for factorial calculation
    t=time.time()
    with multiprocessing.Pool() as pool:
        pool.map(calculate_factorial, numbers)

    print("All factorial calculations are done!")
    print(f"Execution time: {time.time() - t} seconds") 