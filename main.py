import pyttsx3, aiml

engine = pyttsx3.init()
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

while True:
    user = input("=> ")
    response = kernel.respond(user)
    print(response)
    engine.say(response)
    engine.runAndWait()