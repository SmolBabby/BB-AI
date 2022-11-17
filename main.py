# PyCharm help at https://www.jetbrains.com/help/pycharm
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3

engine = pyttsx3.init()

chatbot = ChatBot('BB')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

engine.say("BB is operational.")
engine.runAndWait()

# Get a response to an input statement
stop = False
while not stop:
    Q = input()
    if Q == "stop":
        stop = True
        break
    if Q.__contains__("task"):
        print("Task demanded")
    else:
        answer = chatbot.get_response(Q)
        print(answer)
        engine.say(answer)
        engine.runAndWait()




