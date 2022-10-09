#greatest_common_factor
#Using the modulus operator in python to find the greatest common factor between two numbers
number_1=int(input("Input a number:\n"))
number_2=int(input("Input another number:\n"))
numbers=(number_1, number_2)
def gcf():
    numbs=sorted(numbers, reverse=True)
    big=numbs[0]
    small=numbs[1]
    mod=big%small
    while mod != 0:
        mod=big%small
        print(big)
        print(small)
        print(mod)
        big=small
        small=mod
    print("The greatest common factor between " + str(numbs[0]) + " and " + str(numbs[1]) + " is " + str(big) + ".")
gcf()
