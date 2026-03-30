def sum_even_numbers(numbers):
    new_list = []

    for number in numbers:
        if number % 2 == 0:
            new_list.append(number)
            
    if new_list:
        return sum(new_list)
    
    else:
        return 0
        