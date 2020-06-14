let inp = "function printhello empty parenthesis colon\nprint HELLO\nback tab\nif x equals yay\nprint string yay";
// let words = event.results[i][0].transcript.split(" ");

const word_to_num = {
    "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10
}
// console.log(word_to_num["one"]);
let addTab = 0;

let lines = inp.split("\n");

const getPython = (inp) => {
let words = inp.split(" ");
console.log(words);
let str = "";
for (let i = 0; i < addTab; ++i) str+="\t";

if (words[0] == "back" && words[1] == "tab") {
    addTab--;
} else if (words[0] == "print" && words[1] == "string") {
    words.shift();
    words.shift();
    str += "print(\"" + words.join(" ") + "\")"
} else if (words[0] == "print") {
    if (word_to_num[words[1]]) {
        str += "print(" + (word_to_num[words[1]]) + ")";
    } else {
        words.shift();
        str += "print(" + words.join(" ") + ")"
    }
} else if ((words[1] == "equals" || words[1] == "=") && words[2] == "string") {
    let first = words.shift();
    words.shift();
    words.shift();
    str+=first + " = " + "'" + words.join(" ") + "'";
} else if ((words[1] == "equals" || words[1] == "=") && words[2] == "list") {
    let first = words.shift();
    words.shift();
    str += first + " = [";
    let j = 1;
    while (j < words.length) {
        if (words[j] == 'string'){
            str += "'" + words[j + 1] + "', ";
            j += 2;
        }
        else {
            str += words[j] + ", ";
            j ++;
        }
    }
    str = str.substring(0, str.length-2) + "]";
} else if (words[1] == "equals" || words[1] == "=")  {
    if (word_to_num[words[2]]) {
        str+= words[0] + " = " + word_to_num[words[2]];
    } else {
        let first = words.shift();
        words.shift();
        str+=first + " = " + words.join(" ");
    }
} else if (words[0] == "if" && (words[2] == "equals" || words[2] == "=") && words[3] == "string") {
    words[2] = "=="
    let words1 = words;
    str += words1.slice(0, 3).join(" ") + " \'" + words.slice(4, words.length).join(" ") + "\':";
    addTab += 1
} else if (words[0] == "if" && (words[2] == "equals" || words[2] == "=")) {
    words[2] = "==";
    str += words.join(" ") + ":";
    addTab++;
} else if (words[0] == "for" && words[3] == "range") {
    let words1 = words;
    str+=words1.slice(0, 4).join(" ") + "(" + words.slice(4, words.length).join(" ") + "):";
    addTab++;
} else if (words[0] == "for") {
    str+=words.join(" ") + ":";
    addTab++;
} else if (words[0] == "function" && words.length == 2) {
    str+="def " + words[1] + "():"
    addTab++;
} else if (words[0] == "function" && words.length > 2) {
    str+="def " + words[1] + "(";
    for (let j = 3; j < words.length; j++) {
        str+=words[j] + ", ";
    }
    str = str.substring(0, str.length - 2) + "):";
    addTab++;
} else if (words[0] == "call" && words.length == 2) {
    str+=words[1] + "()";
} else if (words[0] == "call" && words.length > 2) {
    str+=words[1] + "(";
    for (let j = 3; j < words.length; ++j) {
        str+=words[j] + ", ";
    }
    str = str.substring(0, str.length - 2) + ")";
} else {
    str += "# " + words.join(" ");
}

console.log(str);

}


for (let i = 0; i < lines.length; ++i) {
    // console.log(lines[i]);
    getPython(lines[i]);
}