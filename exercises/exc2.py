print("Enter numbers that you like(type any letter to exit): ")
foo = 'foo'
bar = 'bar'
while True:
    number = input()
    try:
        number = int(number)
    except ValueError:
        break 
    if number % 77 == 0:
        print(foo+bar)
    elif number % 11 == 0:
        print(bar)
    elif number % 7 == 0:
        print(foo)

