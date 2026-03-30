def fibonacci(n):
    if n == 0:
        return []
        
    if n == 1:
        return [0]

    num_list = [0]
    
    num1 = 0
    num2 = 1
    sum = 1

    for x in range(n-1):
        num_list.append(sum)
        sum = num1 + num2
        num1 = num2
        num2 = sum

    return num_list

print(fibonacci(5))





