#FizzBuzz 1 to 100
# By Thomas Thirtle

def fizz():
    "Print Fizz"
    print("Fizz", end = "")
    return()

def buzz():
    "Print buzz"
    print("Buzz", end = "")
    return()
    
def number(int):
    "prnt number"
    print(int, end = "")
    return()
    
counter = 1
while (counter <= 100):
    if (counter % 3 == 0):
        fizz()
    if (counter % 5 == 0):
        buzz()
    if (counter % 3 != 0) and (counter % 5 != 0):
        number(counter)
    print ("\n", end = "")
    counter += 1