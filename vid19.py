# Break Statements in Python :
for i in range(1, 101, 1):
    print(i, end=" ")
    if i == 50:
        break
    else:
        print("Mississippi")
print("Thank you")
# Continue statements in python :
for i in [2, 3, 4, 6, 8, 0]:
    if i % 2 != 0:
        continue
    print(i)
