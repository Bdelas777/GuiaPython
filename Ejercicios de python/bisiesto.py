
b = int(input("Dime el año: "))
if(b%4==0 and b%100!=0 or b%400==0):
    print("Si es bisiesto")
else:
    print("No es bisiesto")
