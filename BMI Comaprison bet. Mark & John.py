print("BMI Comparison Between Mark and John")
# From Data 1
# suppose x1 and x2 will be the weight
# y1 and y2 will be the height
# x1 & y1 be the Mark's weight & height
# x2 & y2 be the John's weight & height

x1 = 78
y1 = 1.69

x2 = 92
y2 = 1.95

# Now, From Data 2
# suppose, a1 & a2 as weight
# b1 & b2 be the height
# a1 & b1 be the  Mark's weight & height
# a2 & b2 be the John's weight & height

a1 = 95
b1 = 1.88

a2 = 85
b2 = 1.76

# BMI of Mark & John from data 1 be the d1 & d2
# and BMI from data 2 be the e1 & e2

d1 = x1 / y1 ** 2
d2 = x2 / y2 ** 2

e1 = a1 / b1 ** 2
e2 = a2 / b2 ** 2

print("BMI of Mark from data 1 = ", d1)
print("BMI of John from data 1 = ", d2)
print("BMI of Mark from data 2 = ", e1)
print("BMI of John from data 2 = ", e2)

# c1 & c2 be the BMI comparison from Data 1 And Data 2
c1 = d1 > d2
c2 = e1 > e2

print("From Data 1\nMark has higher BMI than John is", c1)
print("From Data 2\nMark has higher BMI than John is", c2)
