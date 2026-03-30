def analyze_string(text):
    uppercase = 0
    lowercase = 0
    digits = 0

    for char in text:
        if char.isalpha():

            if char.isupper():
                uppercase += 1

            if char.islower():
                lowercase += 1

        elif char.isdigit():
            digits += 1

    return {
        "original": text,
        "reversed": text[::-1],
        "length": len(text),
        "uppercase": uppercase,
        "lowercase": lowercase,
        "digits": digits
    }