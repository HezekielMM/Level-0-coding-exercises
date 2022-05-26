def maximum_number(first_num, second_num, third_num):
    
    if first_num > second_num and first_num > third_num:
        return first_num
    elif second_num > first_num and second_num > third_num:
        return second_num
    else:
        return third_num

returned_value = maximum_number(6, 7, 8)
print(returned_value)