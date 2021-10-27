def print_values(a, b, c):
    if a > b:
        if b > c:
            print(a+","+b+","+c)
        else:
            if a > c:
                print(a+","+c+","+b)
            else:
                print(c+","+a+","+b)
    else:
        if b > c:
            print()
        else:
            print(c+","+b+","+a)


a_value = input("Please enter the a value: ")
b_value = input("Please enter the b value: ")
c_value = input("Please enter the c value: ")

print_values(a_value, b_value, c_value)
