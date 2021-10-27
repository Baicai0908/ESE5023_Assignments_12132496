def Least_moves(n):
    if n%2 == 0:
        print(int(n/2))
    else:
        print(int((n+1)/2))

k=int(input("Please select a number from 1 to 100: "))
Least_moves(k)
