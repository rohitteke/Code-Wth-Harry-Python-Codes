import time
timestamp = time.strftime('%I:%M:%S:%p')
print(timestamp)
timestamp = int(time.strftime('%H'))
print("Hii")
if 5<=timestamp<11:
    print("Good Morning ")
elif 12<=timestamp<16:
    print("Good Afternoon ")
elif 16<=timestamp<20:
    print(("Good Evening "))
else:
    print("Good Night ")

print("Bye!!")

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
