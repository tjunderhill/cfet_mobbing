def fooBarQix(number):

    non_zero_replacements = {
        3: "Foo",
        5: "Bar",
        7: "Qix"
    }

    return_number = True
    digits = [int(d) for d in str(number)]
    for key in non_zero_replacements.keys():
        if (number % key == 0) or (key in digits):
            return_number = False
            break

    if return_number:
        return str(number).replace('0', '*')

    result = ""

    for key in non_zero_replacements.keys():
        if number % key == 0:
            result += non_zero_replacements[key]

    for d in digits:
        if d in non_zero_replacements:
            result += non_zero_replacements[d]
        elif d == 0:
            result += "*"

    return result
