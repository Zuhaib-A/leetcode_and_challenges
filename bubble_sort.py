#Bubble sorting
#An exercise in allowing a custom list of numbers to be bubble sorted.

bub_sort=[]
#Generating list
length=int(input("How many numbers do you wish to bubble sort?\n"))
to_zero=0
while to_zero != length:
    if  (length - to_zero)> 1:
        print("Your list has space for " + str(length - to_zero) + " more numbers...")
    elif (length - to_zero) == 1:
        print("Your list has space for " + str(length - to_zero) + " more number...")
    to_zero=to_zero+1
    number=int(input("Enter: "))
    bub_sort.append(number)
#Bubble sorting the list
print(" ")
for i in range(len(bub_sort)-1):
    for j in range(len(bub_sort)-1):
        if bub_sort[j]>bub_sort[j+1]:
            bub_sort[j], bub_sort[j + 1] = bub_sort[j + 1], bub_sort[j]
            print(*bub_sort)
    print(" ")
