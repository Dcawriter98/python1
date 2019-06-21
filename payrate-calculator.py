# This first line is provided for you

hrs = input("Enter Hours:")
float(hrs)

#Enter pay rate of worker
payrate = input("Enter pay rate:")

float(payrate)
#Work out the gross pay
grosspay = (float(hrs)* float(payrate))

#Print result on screen
print("For", float(hrs),  "hours and the pay rate of",float(payrate), ", the amount of pay is", float (grosspay))