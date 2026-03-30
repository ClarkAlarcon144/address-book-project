def calculate_stats(numbers):
    if not numbers:
        return

    average = sum(numbers)/len(numbers)

    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": average,
        "max": max(numbers),
        "min": min(numbers)
    }

