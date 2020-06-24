def ex33(limit, numbers, incr):
    
    i = 0
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + incr
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

numbers = []
limit = int(input("Enter the limit: "))
incr  = int(input("Enter the incr:  "))

ex33(limit, numbers, incr)

print("The numbers: ")

for num in numbers:
    print(num)