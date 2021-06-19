# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1, 5, 10]
    change = []

    for i in range(len(coins)-1, -1, -1):
             
        
        if m == coins[i]:
            change.append(1) 
            return len(change) 

        while m >= coins[i]:
            m = m - coins[i]
            change.append(coins[i])

    return len(change)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
