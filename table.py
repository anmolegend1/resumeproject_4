a=int(input("Enter Number for which you want table: "))
b=int(input("Enter the range till which you want the multiplication table: "))
def table(a,b):
    for i in range(1,b+1):
        c=a*i
        print(f'{a} x {i}= {c}')

table(a,b)