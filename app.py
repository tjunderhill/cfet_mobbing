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
        print(strNumber[c])
        if strNumber[c] == '3':
            result += "Foo"
        if strNumber[c] == '5':
            result += "Bar"
        if strNumber[c] == '7':
            result += "Qix"
    return result

print(fooBarQix(5))