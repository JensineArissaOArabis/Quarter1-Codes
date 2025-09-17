import math
pi_value = math.pi
radius = float(input("Enter the radius of the circle: "))

area = pi_value * (radius ** 2)
print("The area of the circle is:{:.2f}".format(area))