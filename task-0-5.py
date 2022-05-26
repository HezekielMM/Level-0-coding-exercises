def area_of_triangle(first_side, second_side, third_side):
 
    s = (first_side + second_side + third_side) * (1 / 2)

    area = (s*(s-first_side)*(s-second_side)*(s-third_side))**(0.5)

    return area

returned = area_of_triangle(52, 75, 80)
print(returned)