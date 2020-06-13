import speech_recognition as sr 
import pyttsx3  
import pyaudio

lines = []

r = sr.Recognizer()  

# Function to convert text to speech 
def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
    
addTab = 0
while(1):     
    try: 
        with sr.Microphone() as source2: 
            # r.adjust_for_ambient_noise(source2, duration=0.2) 
            audio2 = r.listen(source2) 
              
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 

            if MyText == "run code":
                break

            print(MyText) 
            word_to_num = {"one": 1, "two": 2, "three": 3, "four": 4,
                           "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}

            words = MyText.split()
            response = ""
            # print(words)
            if words[0] == "back" and words[1] == "tab":
                response = ""
                addTab -= 1
            elif words[0] == "print" and words[1] == "string":
                response = "\t"*addTab + \
                    "print(\"" + "".join(words[2:]) + "\")"
            elif words[0] == "print":
                print(words[1])
                # print(word_to_num(words[1]))
                try:
                    response = "\t"*addTab + \
                        "print(" + str(word_to_num[words[1]]) + ")"
                except:
                    response = "\t"*addTab + \
                        "print(" + " ".join(words[1:]) + ")"
            elif words[1] == "equals":
                try:
                    response = "\t"*addTab + words[0] + \
                        " = " + str(word_to_num[words[2]])
                except:
                    response = "\t"*addTab + \
                        words[0] + " = " + " ".join(words[2:])
            elif words[0] == "if" and words[2] == "equals":
                words[2] = "=="
                response = "\t"*addTab + " ".join(words) + ":"
                addTab += 1
            elif words[0] == "for":
                response = "\t"*addTab + " ".join(words) + ":"
                addTab += 1


            # print("\n".join(lines))

            # toParse = "\n".join([x for x in lines if x != ""])
            if response != "":
                print(response)
                lines.append(response)
    except: 
        pass

# print(lines)
SpeakText("Done")


# print("\n".join(lines))

toParse = "\n".join([x for x in lines if x != ""])

print(toParse)

print("\n\n\nPARSING YOUR CODE\n\n\n")
try:
    exec(toParse)
except:
    print("There was an error running your code")
