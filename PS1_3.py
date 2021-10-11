def pascal_triangle(k):
    line = [1]
    for i in range(k):
        line.append(int(line[i]*(k-i)/(i+1)))
    return line

k = int(input("Please enter the k value: "))
print(pascal_triangle(k))
