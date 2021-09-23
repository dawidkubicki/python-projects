def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number%i==0:
            is_prime = False
    if is_prime:
        print("This is prime number")
    else:
        print("This is not a prime number")

n = int(input("Check this number: "))
prime_number(number=n)
