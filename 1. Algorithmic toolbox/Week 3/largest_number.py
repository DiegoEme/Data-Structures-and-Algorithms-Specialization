# Uses python3

import sys

def largest_number(a):
    # write your code here
    ans = [] 
    

    while len(a) > 0:
      max = 0
      for i in range(len(a)):
        if str(a[i]) + str(max) >= str(max) + str(a[i]):
          max = a[i]

      ans.append(max)
      a.remove(max)
      
      string_ints = [str(int) for int in ans]
      str_of_ints = "".join(string_ints)


    return str_of_ints


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]  
    print(largest_number(a))
