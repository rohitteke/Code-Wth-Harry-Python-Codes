i = int(input("Enter the number: "))
print(i)
while(i<=38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")

# count = 5
# while (count > 0):
#   print(count)
#   count = count - 1
# else:
#   print("I am inside else")

# Do-While Loop in python

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break
# Another Example of Do-While Loop :

i = 0
while True:
  print(i)
  i = i + 1
  if(i%100 == 0):
    break
