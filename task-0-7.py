def celsius_to_fahrenheit(temp_in_celsius):
    
    temp_in_fahrenheit = temp_in_celsius * (9 / 5) + 32

    return temp_in_fahrenheit

def fahrenheit_to_celsius(temp_in_fahrenheit):
    
    temp_in_celsius = (temp_in_fahrenheit - 32) * (5 / 9)

    return temp_in_celsius

first_return = celsius_to_fahrenheit(300)
second_return = fahrenheit_to_celsius(240)

print(first_return)
print(second_return)