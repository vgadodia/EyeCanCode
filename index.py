TEXT = "print string words new line x equals []"

lines = [x.strip() for x in TEXT.split("new line")]

print(lines)

word_to_num = {"one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}

for i in range(len(lines)):
    words = lines[i].split()
    print(words)
    if words[0] == "print" and words[1] == "string":
        lines[i] = "print(\"" + "".join(words[2:]) + "\")"
    elif words[0] == "print":
        lines[i] = "print(" + " ".join(words[1:]) + ")"
    elif words[1] == "equals":
        try:
            lines[i] = words[0] + " = " + str(word_to_num[words[2]])
        except:
            lines[i] = words[0] + " = " + " ".join(words[2:])

print("\n".join(lines))

toParse = "\n".join(lines)
