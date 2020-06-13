TEXT = "hello equals five new line print string five new line print hello new line for i in range(10) new line print i"

TEXT = "x equals 5 new line print x * x"

lines = [x.strip() for x in TEXT.split("new line")]

print(lines)

word_to_num = {"one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}

addTab = 0
for i in range(len(lines)):
    words = lines[i].split()
    # print(words)
    if words[0] == "back" and words[1] == "tab":
        lines[i] = ""
        addTab-=1
    elif words[0] == "print" and words[1] == "string":
        lines[i] = "\t"*addTab + "print(\"" + " ".join(words[2:]) + "\")"
    elif words[0] == "print":
        # print(words[1])
        # print(word_to_num(words[1]))
        try:
            lines[i] = "\t"*addTab + "print(" + str(word_to_num[words[1]]) + ")"
        except:
            lines[i] = "\t"*addTab + "print(" + " ".join(words[1:]) + ")"
    elif words[1] == "equals" and words[2] == "string":
        lines[i] = "\t"*addTab + words[0] + " = " + "'" + ' '.join(words[3:]) + "'"
    elif words[1] == "equals":
        try:
            lines[i] = "\t"*addTab + words[0] + \
                " = " + str(word_to_num[words[2]])
        except:
            lines[i] = "\t"*addTab + words[0] + " = " + " ".join(words[2:])
    elif words[0] == "if" and words[2] == "equals" and words[3] == "string":
        words[2] = "=="
        lines[i] = "\t"*addTab + " ".join(words[:3]) + " '" + ' '.join(words[4:]) + "'" + ":"
        addTab +=1

    elif words[0] == "if" and words[2] == "equals":
        words[2] = "=="
        lines[i] = "\t"*addTab + " ".join(words) + ":"
        addTab +=1
    elif words[0] == "for" and words[3] == "range":
        lines[i] = "\t"*addTab + " ".join(words[:4]) + "(" + ' '.join(words[4:]) + ")" + ":"
        addTab += 1
    elif words[0] == "for":
        lines[i] = "\t"*addTab + " ".join(words) + ":"
        addTab += 1


# print("\n".join(lines))

toParse = "\n".join([x for x in lines if x != ""])

print(toParse)


# eval(toParse)

# print('exec')

exec(toParse)