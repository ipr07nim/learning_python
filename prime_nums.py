number = int(input("What's the number? "))
def check_prime(x):
    for y in range(2, int(x/2)):
        if x%y != 0:
            continue
        else:
            return False
        return True
if number < 3:
    print(f"There are no prime numbers below {number}.")

else:
    factors = []
    for x in range(5, number):
        if check_prime(x) is False:
            continue
        else:
            factors.append(x) #is prime

    if number == 3:
        factors = [2]
        print("There is 1 prime number below 3.")
        print("It is: [2]")
    else:
        factors.insert(0, 3)
        factors.insert(0, 2)
        print(f"There are {(len(factors))} prime numbers below {number}.")
        print(f"They are: {factors}.")