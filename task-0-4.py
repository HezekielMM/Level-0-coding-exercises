def even_or_odd(number):
    
    x = number % 2

    if x > 0:
        return "odd"
    else:
        return "even"


returned_value = even_or_odd(1)
print(returned_value)