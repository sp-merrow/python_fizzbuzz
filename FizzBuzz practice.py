fizzBuzz = {3 : 'Fizz', 5 : 'Buzz'}

for i in range(1, 101):
    charStr = ''
    for f in fizzBuzz.keys():
        if i % f == 0:
            charStr += fizzBuzz[f]
    if not charStr:
        print(i)
    else:
        print(charStr)
