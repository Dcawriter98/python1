#define variables

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

#define the computepay function

def computepay(h,r):
    if h <= 40:
        p = float(h*r)
        return (p)

    else:
	    p= float(40*r) + float(((h-40)*r)*1.5)
	    return (p)

#call computepay function

print (computepay (h,r))