score = input("Enter Score: ")
s = float(score)

#Set grade levels

if s > 1.0:
    print ("The number you entered", s , "is out of range.")
elif 1.0 > s >= 0.9:
    print ("A")
elif 0.899 > s > 0.7999:
    print ("B")
elif 0.798 > s > 0.6999:
    print ("C")
elif 0.698 > s > 0.5999:
    print ("D")
    