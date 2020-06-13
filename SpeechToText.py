import speech_recognition as sr 
import pyttsx3  

lines = []

r = sr.Recognizer()  

# Function to convert text to speech 
def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 
    
while(1):     
    try: 
        with sr.Microphone() as source2: 
            # r.adjust_for_ambient_noise(source2, duration=0.2) 
            audio2 = r.listen(source2) 
              
            # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 

            if MyText == "finish code":
                break

            print(MyText) 
            lines.append(MyText)
    except: 
        pass

print(lines)
SpeakText("Done")







