a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))
d = int(input("Enter side D: "))
e = int(input("Enter side E: "))

#formula to use to find the area is length * width
#area of right triangle (where side E is) is 0.5 * base * height

areaOne = 1.0 * a * b  #l * w
areaTwo = (a-c) * (d-e-b)
areaThree = 0.5 * (a-c) * e  #0.5 * b * h

print() 
#this is to keep a space between the input statements on top and the total room area
print("Room Area: " + str(areaOne + areaTwo + areaThree))