number = 1 
while number <= 100:
    match (number % 7 == 0, "7" in str(number)):
        case (True, True):
            print("FizzBuzz")
        case (True, False):
            print("Fizz")
        case (False, True):
            print("Buzz")
        case (False, False):
            print(number)
    number += 1