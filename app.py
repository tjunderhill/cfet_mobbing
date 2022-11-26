def fooBarQix(number):

    non_zero_replacements = {
        3: "Foo",
        5: "Bar",
        7: "Qix"
    }
    digits = [int(d) for d in str(number)]

    # find out if anything needs replaced or appended
    replacements_needed = False
    for key in non_zero_replacements.keys():
        if (number % key == 0) or (key in digits):
            replacements_needed = True
            break

    if not replacements_needed:
        # return number with zeros substituded in place
        return str(number).replace('0', '*')

    # do the replacing and appending
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
