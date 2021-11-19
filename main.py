def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    less = []
    greater = []
    base = numbers.pop()
    for number in numbers:
        if number < base:
            less.append(number)
        else:
            greater.append(number)
    return quick_sort(less) + [base] + quick_sort(greater)


numbers = [9, 4, 5, 3]
print(quick_sort(numbers))
