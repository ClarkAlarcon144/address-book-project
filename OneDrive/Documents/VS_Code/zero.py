def is_palindrome(text): 
    result = ""

    for char in text.replace(" ", "").lower():
        if char.isalpha():
            result += char

    return result == result[::-1]