hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

if h <= 40:
    grosspay = (h*r)
    print(grosspay)
    
else:
    grosspay = ((h-40)*(r*1.5))+(40*r)
    print(grosspay)