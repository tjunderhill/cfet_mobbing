def fooBarQix(number):
    result = ""

    if number % 3 == 0:
        result += "Foo"
    if number % 5 == 0:
        result += "Bar"
    if number % 7 == 0:
        result += "Qix"

    strNumber = str(number)
    for c in range(0, len(strNumber)):
        if strNumber[c] == '3':
            result += "Foo"
        if strNumber[c] == '5':
            result += "Bar"
        if strNumber[c] == '7':
            result += "Qix"
        if strNumber[c] == '0':
            result += "*"
            
    if len(result) == 0:
        result+=str(number)
    return result

print(fooBarQix(101))

assert fooBarQix(1) == "1", fooBarQix(1)
assert fooBarQix(2) == "2"
assert fooBarQix(3) == "FooFoo"
assert fooBarQix(4) == "4"
assert fooBarQix(5) == "BarBar"
assert fooBarQix(6) == "Foo"
assert fooBarQix(7) == "QixQix"
assert fooBarQix(8) == "8"
assert fooBarQix(9) == "Foo"
assert fooBarQix(10) == "Bar"
assert fooBarQix(13) == "Foo"
assert fooBarQix(15) == "FooBarBar"
assert fooBarQix(21) == "FooQix"
assert fooBarQix(33) == "FooFooFoo"
assert fooBarQix(51) == "FooBar"
assert fooBarQix(52) == "Bar"
assert fooBarQix(53) == "BarFoo"
assert fooBarQix(101) == "1*1"
assert fooBarQix(303) == "FooFoo*Foo"
assert fooBarQix(105) == "FooBarQix*Bar"
assert fooBarQix(10101) == "FooQix**"
