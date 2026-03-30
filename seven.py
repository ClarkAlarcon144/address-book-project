
def is_prime(number):
    if number <= 0:
        return False

    if number == 1:
        return False

    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    for x in range(3, int(number**0.5)+1, 2):
        if number % x == 0:
            return False
        
    return True

