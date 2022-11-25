def fooBarQix(number):
    result = ""

    if number % 3 == 0:
        result += "Foo"
    if number % 5 == 0:
        result += "Bar"
    if number % 7 == 0:
        result += "Qix"
    return result

print(fooBarQix(30))