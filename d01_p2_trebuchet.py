# note: using a class is only necessary if you want to store data at each node.
# otherwise, you can implement a trie using only hash maps.
class TrieNode:
    def __init__(self):
        # you can store data at nodes if you wish
        self.values = {}
        self.children = {}


def build_trie():
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    root = TrieNode()
    for word, value in digits.items():
        print(word, value)
        curr = root
        for i, c in enumerate(word):
            if c not in curr.children:
                curr.children[c] = TrieNode()
            if i == len(word) - 1:
                curr.values[word] = value
            curr = curr.children[c]
        # at this point, you have a full word at curr
        # you can perform more logic here to give curr an attribute if you want

    return root


def trebuchet(data: list[str]):
    """
    data: list[str]

    for each str the first digit + last digit = calibration val
    return the sum of all calibration values
    spelt word also counts as a number
    """
    trie = build_trie()
    res = 0

    print(trie)
    for s in data:
        calibration_val = 0
        i = 0
        while not calibration_val and i < len(s):
            if s[i].isdigit():
                calibration_val = int(s[i])
                break
            j = i

            t = trie
            word = ""
            while s[j].isalpha():
                if s[j] in t.children:
                    word += s[j]
                    if word in t.values:
                        calibration_val = t.values[word]
                        break
                    t = t.children[s[j]]
                    j += 1
                else:
                    break

            i += 1

        second = 0
        while i < len(s):
            if s[i].isdigit():
                second = int(s[i])

            j = i
            t = trie
            word = ""
            while s[j].isalpha():
                if s[j] in t.children:
                    word += s[j]
                    if word in t.values:
                        second = t.values[word]
                        break
                    t = t.children[s[j]]
                    j += 1
                else:
                    break
            i += 1

        calibration_val = calibration_val * 10 + second
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
