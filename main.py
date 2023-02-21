import sys
import threading
import tkinter as tk

import pyttsx3 as tts
import speech_recognition as sr

from  neuralintents import GenericAssistant

class Assistant:
    
    def __init__(self) -> None:
        self.recognition = sr.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)
        
        self.assistant = GenericAssistant("intent.json", intent_methods={"file": self.create_file})
        self.assistant.train_modal()
        
        self.root = tk.Tk
        self.label = tk.Label(text="🤖", font=("Arial", 120, "bold"))
        self.label.pack()
        
        threading.Thread(target=self.run_assinstant).start()
        
        self.root.mainloop()
        
        def create_file(self):
            with open("somefile.txt", "w") as f:
                f.write("Hello World!")
        
        def run_assistant(self):
            while True:
                try:
                    with sr.Microphone() as mic:
                        self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                        audio = self.recognizer.listen(mic)
                        
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        
                        if "hey bot" in text:
                            self.label.config(fg="red")
                            audio = self.recognizer.listen(mic)
                            text = self.recognizer.recognize_google(audio)
                            text = text.lower()
                            if text == "stop":
                                self.speaker.say("bye")
                                self.speaker.runAndWait()
                                self.speaker.stop()
                                self.speaker.destroy()
                                sys.exit()
                            else:
                                if text is not None:
                                    response = self.assistant.requast(text)
                                    if response is not None: 
                                        self.speaker.say(response)
                                        self.speaker.runAndWait()
                                    self.label.config(fg="black")
                except:
                    self.label.config(fg="black")
                    continue                
                
Assistant()