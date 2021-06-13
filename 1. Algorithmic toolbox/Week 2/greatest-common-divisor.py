# Uses python3
import sys

def gcd_naive(a, b):
    if b == 0:
        return a
    
    a2 = a % b    

    return gcd_naive(b, a2)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
