for x in range(1, 101):
    if x % 7 == 0 and "7" in str(x):
        print("FizzBuzz")
    elif x % 7 == 0:
        print("Fizz")
    elif "7" in str(x):
        print("Buzz")
    else:
        print(x)