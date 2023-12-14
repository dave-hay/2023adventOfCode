"""
left most digit
"""


def trebuchet(data: list[str]):
    """
    data: list[str]

    for each str the first digit + last digit = calibration val
    return the sum of all calibration values
    """
    res = 0

    for s in data:
        calibration_val = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                calibration_val = int(s[i])
                break
            i += 1

        j = len(s) - 1

        while j > -1:
            if s[j].isdigit():
                calibration_val = calibration_val * 10 + int(s[j])
                break
            j -= 1

        res += calibration_val

    return res


def getData():
    res = []
    with open("./inputs/01_trebuchet.txt", "r") as data:
        for d in data:
            res.append(d)
    return res


data = getData()
print(trebuchet(data))
