import time
from main import countWellFormedParenthesis

def performance_test():
    print("Performance test for countWellFormedParenthesis(n):")
    for n in range(1, 16):
        start = time.time()
        result = countWellFormedParenthesis(n)
        end = time.time()
        duration = end - start
        print(f"n = {n:2d} → {result:7d} combinations, time: {duration:.6f} seconds")

if __name__ == "__main__":
    performance_test()