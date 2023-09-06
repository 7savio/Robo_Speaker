import os
import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")
if __name__=="__main__":
    print("Welcome to RoboSpeaker 1.1 Created By Savio Fernando")
    while True:
        savio=input("Enter What you want to Speak:-")
        if savio=="bye":
            speak.speak("bye bye friend")
            break
        command=f"{savio}"
        speak.speak(command)


