# creation of the range function

# len() returns the number of characters in a text string.

def range_simple_list(n): # I rewrite the range() function
    
    k= 0
    range_list = []
    if n >= k:
        while n != k:
            range_list.append(k)
            k += 1
            
    elif n == k:
        range.append(0)
    elif n <= k:
        while n != k:
            range_list.append(k)
            k -= 1
            

    return print(range_list)    

x = 67

range_simple(x)

r = range(x)
r_list = []
for x in r:
    r_list.append(x)

