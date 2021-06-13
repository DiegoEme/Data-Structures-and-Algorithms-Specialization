# Uses python3
def calc_fib(n):

    arr = [0,1]

    if n < 2:
        arr = [0,1]

    if n >= 2:  
        for x in range(2, 9999999):
            arr.append((arr[x-1] + arr[x-2]) % 10)
    
    return arr[n]

n = int(input())
print(calc_fib(n))
